from __future__ import print_function
import os
from os.path import realpath, dirname
import ctypes
from ctypes import byref, WINFUNCTYPE, HRESULT, WinError
import struct

import windows
import windows.winproxy as winproxy
from windows.generated_def.winstructs import *
import resource_emulation

from dbgdef import *
from base import BaseKernelDebugger, KernelDebugger32, KernelDebugger64
from base import experimental, IS_SPHINX_BUILD
from base import IDebugClient, IDebugControl, IDebugDataSpaces2, IDebugSymbols3

import driver_upgrade
from driver_upgrade import DU_MEMALLOC_IOCTL, DU_KCALL_IOCTL, DU_OUT_IOCTL, DU_IN_IOCTL

import simple_com
from simple_com import IDebugOutputCallbacksVtable


class DummyIATEntry(ctypes.Structure):
    _fields_ = [
        ("value", DWORD)]

    @classmethod
    def create(cls, addr, dll, name):
        self = cls.from_address(addr)
        self.addr = addr
        self.hook = None
        self.nonhookvalue = windows.utils.get_func_addr(dll, name)
        return self

    def set_hook(self, callback, types=None):
        hook = windows.hooks.IATHook(self, callback, types)
        self.hook = hook
        hook.enable()
        return hook


@windows.hooks.GetModuleFileNameWCallback
def EmulateWinDBGName(hModule, lpFilename, nSize, real_function):
    if hModule is not None:
        return real_function()
    ptr_addr = ctypes.cast(lpFilename, ctypes.c_void_p).value
    v = (c_char * 100).from_address(ptr_addr)
    path = "C:\\windbg.exe"
    path_wchar = "\x00".join(path) + "\x00\x00\x00"
    v[0:len(path_wchar)] = path_wchar
    return len(path_wchar)


def require_upgraded_driver(f):
    if IS_SPHINX_BUILD:
        if f.__doc__.strip().startswith("| "):
            nextline = ""
        else:
            nextline = "| "
        # Strip all leading space for rst parsing by sphinx
        new_doc = "| <require upgraded driver>\n" + nextline + f.__doc__ + "\n"
        new_doc = "\n".join([l.strip() for l in new_doc.split("\n")])
        f.__doc__ = new_doc
        return f
    @functools.wraps(f)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'upgrader') or not self.upgrader.is_upgraded:
            raise ValueError('Cannot call {0} without upgraded driver'.format(f.__name__))
        return f(self, *args, **kwargs)
    return wrapper

class LocalKernelDebuggerBase(BaseKernelDebugger):
    DRIVER_FILENAME = None
    DRIVER_RESOURCE = None

    def __init__(self, quiet=True):
        self.quiet = quiet
        self._output_string = ""
        self._output_callback = None
        self._load_debug_dll()
        self.DebugClient = self._do_debug_create()
        self._do_kernel_attach()
        self._ask_other_interface()
        self._setup_symbols_options()
        self.set_output_callbacks(self._standard_output_callback)
        self._wait_local_kernel_connection()
        self._load_modules_syms()
        self.reload()
        self._init_dbghelp_func()
        self._upgrade_driver()

    def _setup_driver_resource(self, dbgengmod, k32import):
        raise NotImplementedError("_setup_driver_resource")

    def _setup_name_imposture(self, dbgengmod, k32import):
        raise NotImplementedError("_setup_name_imposture")

    # Change current process name via GetModuleFileNameW hook
    def _setup_windbg_imposture(self):
        dbgengmod = [i for i in windows.current_process.peb.modules if i.name == "dbgeng.dll"][0]
        k32import = dbgengmod.pe.imports['kernel32.dll']
        self._setup_driver_resource(dbgengmod, k32import)
        self._setup_name_imposture(dbgengmod, k32import)

    def _do_kernel_attach(self):
        self._setup_windbg_imposture()
        res = self.DebugClient.AttachKernel(DEBUG_ATTACH_LOCAL_KERNEL, None)
        if res:
            raise WinError(res)

    def _get_kldbgdrv_handle(self):
        if not hasattr(self, "_kldbgdrv_handle"):
            self._kldbgdrv_handle = windows.winproxy.CreateFileA("\\\\.\\kldbgdrv", GENERIC_READ | GENERIC_WRITE, FILE_SHARE_WRITE | FILE_SHARE_READ)
        return self._kldbgdrv_handle
        
    def detach(self):
        """End the Debugging session and detach the COM interface"""
        self.DebugClient.EndSession(DEBUG_END_PASSIVE)
        self.DebugClient.DetachProcesses()
        self.DebugClient.Release()
        del self.DebugClient
        self.DebugSymbols.Release()
        del self.DebugSymbols
        self.DebugControl.Release()
        del self.DebugControl
        self.DebugDataSpaces.Release()
        del self.DebugDataSpaces

    def current_processor(self):
        """:returns: The number of the processor we are currently on -- :class:`int`"""
        return windows.winproxy.GetCurrentProcessorNumber()

    def set_current_processor(self, proc_nb):
        """Set the processor we want to be executed on

          :param proc_nb: the number of the processor
          :type proc_nb: int"""
        return windows.winproxy.SetThreadAffinityMask(dwThreadAffinityMask=(1 << proc_nb))

    def number_processor(self):
        """:returns: The number of processors on the machine -- :class:`int`"""
        return self.read_dword("nt!KeNumberProcessors")

    def on_each_processor(self):
        """Iter execution on every processor

           :yield: current processor number"""
        for nb_proc in self.number_processor():
            self.set_current_processor(nb_proc)
            yield nb_proc

    @require_upgraded_driver
    def kcall(self, target, *args):
        """| Call target in kernel mode with given arguments.
           | KCall respect the calling convention but YOU must
           | pass the correct number of argument or the kernel
           | will likely crash.
           | (see :func:`map_page_to_userland`) for an example

           :param target: the Symbol to call
           :type target: Symbol
           :param args: the arguments of the call
           :type args: list of int
           :returns: :class:`int`
        """
        raise NotImplementedError("bitness dependent")

    # do_in | do_out
    # There is already a COM API: WriteIo and ReadIo but it seems that
    # these API check for some alignment in the port and the size.
    # A ReadIo(size=4) must be on a port aligned on 4.
    # It may caused by a bad call from use in write_io | read_io
    # Anyway we implemented our own bypass in upgrade driver

    @require_upgraded_driver
    def do_in(self, port, size):
        """| Perform an IN operation

           :param port: port to read
           :param size: size to read
           :type port: int
           :type size: int - 1, 2 or 4
           :returns: the value read -- :class:`int`
        """
        raise NotImplementedError("bitness dependent")

    @require_upgraded_driver
    def do_out(self, port, value, size):
        """| Perform an OUT operation

           :param port: port to write
           :param size: size to write
           :type port: int
           :type size: int - 1, 2 or 4
           :returns: the number of bytes written -- :class:`int`
        """
        raise NotImplementedError("bitness dependent")

    @require_upgraded_driver
    def alloc_memory(self, size=0x1000):
        """Allocate **size** of NonPaged kernel memory"""
        raise NotImplementedError("bitness dependent")

    @require_upgraded_driver
    def map_page_to_userland(self, virtual_addr, size):
        """Map **size** bytes of kernel memory **virtual_addr** in the current address space

          :param virtual_addr: kernel virtual addr
          :param size: size to map
          :type virtual_addr: int
          :type size: int
          :returns: address of the page in current process -- :class:`int`
        """

        # Check if all exports are known before calling everything
        IoAllocateMdl = self.resolve_symbol("IoAllocateMdl")
        MmBuildMdlForNonPagedPool = self.resolve_symbol("MmBuildMdlForNonPagedPool")
        MmMapLockedPagesSpecifyCache = self.resolve_symbol("MmMapLockedPagesSpecifyCache")
        mdl = self.kcall(IoAllocateMdl, virtual_addr, size, False, False, None)
        self.kcall(MmBuildMdlForNonPagedPool, mdl)
        mapped_addr = self.kcall(MmMapLockedPagesSpecifyCache, mdl, UserMode, MmNonCached, None, False, NormalPagePriority)
        return mapped_addr

class LocalKernelDebugger32(LocalKernelDebuggerBase, KernelDebugger32):
    DRIVER_FILENAME = os.path.join(realpath(dirname(__file__)), "..\\bin\\windbg_driver_x86.sys")
    DRIVER_RESOURCE = resource_emulation.Ressource(DRIVER_FILENAME, 0x7777, 0x4444)

    # In our 32bits dll, GetModuleFileNameW and FindResourceW are not in IAT
    # There is a safe and secure lazy resolution, so let's just hook this jump table
    GetModuleFileNameW_addr_jump_offset = 0x3374bc
    FindResourceW_addr_jump_offset = 0x3374a0

    # read_ptr and write_ptr real implementation (bitness dependant)
    read_ptr = LocalKernelDebuggerBase.read_dword
    read_ptr_p = LocalKernelDebuggerBase.read_dword_p
    write_ptr = LocalKernelDebuggerBase.write_dword
    write_ptr_p = LocalKernelDebuggerBase.write_dword_p

    # Setup DRIVER_RESOURCE as a resource using hooks
    def _setup_driver_resource(self, dbgengmod, k32import):
        SizeofResourceIAT = [x for x in k32import if x.name == "SizeofResource"][0]
        LoadResourceIAT = [x for x in k32import if x.name == "LoadResource"][0]
        LockResourceIAT = [x for x in k32import if x.name == "LockResource"][0]

        FindResourceW_addr_jump = dbgengmod.DllBase + self.FindResourceW_addr_jump_offset
        DummyFindResourceWIAT = DummyIATEntry.create(FindResourceW_addr_jump, "kernel32.dll", "FindResourceW")

        # Add our driver to emulated resources
        resource_emulation.resource_list.append(self.DRIVER_RESOURCE)
        # Setup Resource emulation into dbgeng.dll
        DummyFindResourceWIAT.set_hook(resource_emulation.FindResourceWHook)
        SizeofResourceIAT.set_hook(resource_emulation.SizeofResourceHook)
        LoadResourceIAT.set_hook(resource_emulation.LoadResourceHook)
        LockResourceIAT.set_hook(resource_emulation.LockResourceHook)

    def _setup_name_imposture(self, dbgengmod, k32import):
        GetModuleFileNameW_addr_jump = dbgengmod.DllBase + self.GetModuleFileNameW_addr_jump_offset
        DummyGetModuleFileNameWIAT = DummyIATEntry.create(GetModuleFileNameW_addr_jump, "kernel32.dll", "GetModuleFileNameW")
        DummyGetModuleFileNameWIAT.set_hook(EmulateWinDBGName)

    # Driver upgrade stuff
    def _upgrade_driver(self):
        self.upgrader = driver_upgrade.DriverUpgrader32(self)
        self.upgrader.upgrade_driver()

    # upgraded driver API
    @require_upgraded_driver
    def kcall(self, target, *args):
        """Call target in kernel mode with given arguments"""
        target = self.trim_ulong64_to_address(self.resolve_symbol(target))
        args = [arg if arg is not None else 0 for arg in args]
        buffer = struct.pack("<" + "I" * (len(args) + 1), target, *args)
        h = self._get_kldbgdrv_handle()
        res = DWORD(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_KCALL_IOCTL, buffer, len(buffer), byref(res), ctypes.sizeof(res))
        return res.value

    @require_upgraded_driver
    def do_in(self, port, size):
        """Perform IN instruction in kernel mode"""
        if size not in [1, 2, 4]:
            raise ValueError("Invalid IN size: {0}".format(size))
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<II", size, port)
        res = DWORD(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_IN_IOCTL, buffer, len(buffer), byref(res), ctypes.sizeof(res))
        return res.value

    @require_upgraded_driver
    def do_out(self, port, value, size):
        """Perform OUT instruction in kernel mode"""
        if size not in [1, 2, 4]:
            raise ValueError("Invalid OUT size: {0}".format(size))
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<III", size, port, value)
        windows.winproxy.DeviceIoControl(h, DU_OUT_IOCTL, buffer, len(buffer), 0, 0)
        return None

    @require_upgraded_driver
    def alloc_memory(self, size=0x1000, type=0, tag=0x45544942):
        """Allocation <size> of NonPaged kernel memory"""
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<III", type, size, tag)
        res = DWORD(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_MEMALLOC_IOCTL, buffer, len(buffer), byref(res), 4)
        return res.value


class LocalKernelDebugger64(LocalKernelDebuggerBase, KernelDebugger64):
    DRIVER_FILENAME = os.path.join(realpath(dirname(__file__)), "..\\bin\\windbg_driver_x64.sys")
    DRIVER_RESOURCE = resource_emulation.Ressource(DRIVER_FILENAME, 0x7777, 0x4444)

    read_ptr = LocalKernelDebuggerBase.read_qword
    read_ptr_p = LocalKernelDebuggerBase.read_qword_p
    write_ptr = LocalKernelDebuggerBase.write_qword
    write_ptr_p = LocalKernelDebuggerBase.write_qword_p

    # Setup DRIVER_RESOURCE as a resource using hooks
    def _setup_driver_resource(self, dbgengmod, k32import):
        SizeofResourceIAT = [x for x in k32import if x.name == "SizeofResource"][0]
        LoadResourceIAT = [x for x in k32import if x.name == "LoadResource"][0]
        LockResourceIAT = [x for x in k32import if x.name == "LockResource"][0]
        FindResourceWIAT = [x for x in k32import if x.name == "FindResourceW"][0]

        # Add our drive to emulated resources
        resource_emulation.resource_list.append(self.DRIVER_RESOURCE)
        # Setup Resource emulation into dbgeng.dll
        FindResourceWIAT.set_hook(resource_emulation.FindResourceWHook)
        SizeofResourceIAT.set_hook(resource_emulation.SizeofResourceHook)
        LoadResourceIAT.set_hook(resource_emulation.LoadResourceHook)
        LockResourceIAT.set_hook(resource_emulation.LockResourceHook)

    def _setup_name_imposture(self, dbgengmod, k32import):
        GetModuleFileNameWIAT = [x for x in k32import if x.name == "GetModuleFileNameW"][0]
        GetModuleFileNameWIAT.set_hook(EmulateWinDBGName)

    def _upgrade_driver(self):
        self.upgrader = driver_upgrade.DriverUpgrader64(self)
        self.upgrader.upgrade_driver()


    @require_upgraded_driver
    def alloc_memory(self, size=0x1000, type=0, tag=0x45544942):
        """Allocation <size> of NonPaged kernel memory"""
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<QQQ", type, size, tag)
        res = c_uint64(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_MEMALLOC_IOCTL, buffer, len(buffer), byref(res), sizeof(res))
        return res.value

    @require_upgraded_driver
    def kcall(self, target, *args):
        """Call target in kernel mode with given arguments"""
        target = self.trim_ulong64_to_address(self.resolve_symbol(target))
        args = [arg if arg is not None else 0 for arg in args]
        buffer = struct.pack("<" + "Q" * (len(args) + 1), target, *args)
        h = self._get_kldbgdrv_handle()
        res = c_uint64(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_KCALL_IOCTL, buffer, len(buffer), byref(res), ctypes.sizeof(res))
        return res.value

    @require_upgraded_driver
    def do_in(self, port, size):
        """Perform IN instruction in kernel mode"""
        if size not in [1, 2, 4]:
            raise ValueError("Invalid IN size: {0}".format(size))
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<QQ", size, port)
        res = DWORD(0x44444444)
        windows.winproxy.DeviceIoControl(h, DU_IN_IOCTL, buffer, len(buffer), byref(res), ctypes.sizeof(res))
        return res.value

    @require_upgraded_driver
    def do_out(self, port, value, size):
        """Perform OUT instruction in kernel mode"""
        if size not in [1, 2, 4]:
            raise ValueError("Invalid OUT size: {0}".format(size))
        h = self._get_kldbgdrv_handle()
        buffer = struct.pack("<QQQ", size, port, value)
        windows.winproxy.DeviceIoControl(h, DU_OUT_IOCTL, buffer, len(buffer), 0, 0)
        return None


class LocalKernelDebuggerError(Exception):
    pass


def LocalKernelDebugger(quiet=True):
    """| Check that all conditions to Local Kernel Debugging are met
       | and return a LKD (subclass of :class:`LocalKernelDebuggerBase`
    """
    if not windows.utils.check_debug():
        raise LocalKernelDebuggerError("Cannot perform LocalKernelDebugging on kernel not in DEBUG mode")
    if not windows.utils.check_is_elevated():
        raise LocalKernelDebuggerError("Cannot perform LocalKernelDebugging from non-Admin process")
    windows.utils.enable_privilege(SE_DEBUG_NAME, True)
    if windows.system.bitness == 64:
        if windows.current_process.is_wow_64:
            raise LocalKernelDebuggerError("Cannot perform LocalKernelDebugging from SysWow64 process (please launch from 64bits python)")
        return LocalKernelDebugger64(quiet)
    return LocalKernelDebugger32(quiet)