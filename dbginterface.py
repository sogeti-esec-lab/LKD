import os
from os.path import realpath, dirname
import struct
import itertools
import functools
import ctypes
from ctypes import byref, WINFUNCTYPE, HRESULT, WinError

from simple_com import COMInterface, IDebugOutputCallbacksVtable
import resource_emulation
import driver_upgrade
from driver_upgrade import DU_MEMALLOC_IOCTL, DU_KCALL_IOCTL, DU_OUT_IOCTL, DU_IN_IOCTL
import windows
import windows.hooks
import windows.winproxy as winproxy
from windows.generated_def.winstructs import *
from dbgdef import *
from dbgtype import DbgEngType

# Based on the trick used in PRAW
# http://stackoverflow.com/a/22023805
IS_SPHINX_BUILD = bool(os.environ.get('SPHINX_BUILD', '0'))

# The COM Interfaces we need for the LocalKernelDebugger
class IDebugClient(COMInterface):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, PVOID, PVOID)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff538145%28v=vs.85%29.aspx
        "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, c_char_p)(3, "AttachKernel"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff541851%28v=vs.85%29.aspx
        "DetachProcesses": WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff543004%28v=vs.85%29.aspx
        "EndSession": WINFUNCTYPE(HRESULT, c_ulong)(26, "EndSession"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff556751%28v=vs.85%29.aspx
        "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, c_void_p)(34, "SetOutputCallbacks"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff545475%28v=vs.85%29.aspx
        "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
    }


class IDebugDataSpaces(COMInterface):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, PVOID, PVOID)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554359%28v=vs.85%29.aspx
        "ReadVirtual": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(3, "ReadVirtual"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561468%28v=vs.85%29.aspx
        "WriteVirtual": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(4, "WriteVirtual"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554310%28v=vs.85%29.aspx
        "ReadPhysical": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(10, "ReadPhysical"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561432%28v=vs.85%29.aspx
        "WritePhysical": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(11, "WritePhysical"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff553573%28v=vs.85%29.aspx
        "ReadIo": WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(14, "ReadIo"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561402%28v=vs.85%29.aspx
        "WriteIo": WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(15, "WriteIo"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554289%28v=vs.85%29.aspx
        "ReadMsr": WINFUNCTYPE(HRESULT, ULONG, PULONG64)(16, "ReadMsr"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561424%28v=vs.85%29.aspx
        "WriteMsr": WINFUNCTYPE(HRESULT, ULONG, ULONG64)(17, "WriteMsr"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff553519%28v=vs.85%29.aspx
        "ReadBusData": WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(18, "ReadBusData"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561371%28v=vs.85%29.aspx
        "WriteBusData": WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(19, "WriteBusData"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554326%28v=vs.85%29.aspx
        "ReadProcessorSystemData": WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID, ULONG, PULONG)(22, "ReadProcessorSystemData"),
    }


class IDebugDataSpaces2(COMInterface):
    _functions_ = dict(IDebugDataSpaces._functions_)
    _functions_.update({
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff560335%28v=vs.85%29.aspx
        "VirtualToPhysical": WINFUNCTYPE(HRESULT, ULONG64, PULONG64)(23, "VirtualToPhysical"),
    })


# https://msdn.microsoft.com/en-us/library/windows/hardware/ff550856%28v=vs.85%29.aspx
class IDebugSymbols(COMInterface):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, PVOID, PVOID)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff556798%28v=vs.85%29.aspx
        "SetSymbolOption": WINFUNCTYPE(HRESULT, ctypes.c_ulong)(6, "SetSymbolOption"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547183%28v=vs.85%29.aspx
        "GetNameByOffset": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG, PULONG64)(7, "GetNameByOffset"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff548035%28v=vs.85%29.aspx
        "GetOffsetByName": WINFUNCTYPE(HRESULT, c_char_p, POINTER(ctypes.c_uint64))(8, "GetOffsetByName"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547927%28v=vs.85%29.aspx
        "GetNumberModules": WINFUNCTYPE(HRESULT, LPDWORD, LPDWORD)(12, "GetNumberModules"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547080%28v=vs.85%29.aspx
        "GetModuleByIndex": WINFUNCTYPE(HRESULT, DWORD, PULONG64)(13, "GetModuleByIndex"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547146%28v=vs.85%29.aspx
        "GetModuleNames": WINFUNCTYPE(HRESULT, DWORD, c_uint64,
                                      PVOID, DWORD, LPDWORD, PVOID, DWORD, LPDWORD, PVOID, DWORD, LPDWORD)(16, "GetModuleNames"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549408%28v=vs.85%29.aspx
        "GetTypeName": WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(19, "GetTypeName"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549376%28v=vs.85%29.aspx
        "GetTypeId": WINFUNCTYPE(HRESULT, ULONG64, c_char_p, PULONG)(20, "GetTypeId"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549457%28v=vs.85%29.aspx
        "GetTypeSize": WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG)(21, "GetTypeSize"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546763%28v=vs.85%29.aspx
        "GetFieldOffset": WINFUNCTYPE(HRESULT, ULONG64, ULONG, c_char_p, PULONG)(22, "GetFieldOffset"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549173%28v=vs.85%29.aspx
        "GetSymbolTypeId": WINFUNCTYPE(HRESULT, c_char_p, PULONG, PULONG64)(23, "GetSymbolTypeId"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff558815%28v=vs.85%29.aspx
        "StartSymbolMatch": WINFUNCTYPE(HRESULT, c_char_p, PULONG64)(36, "StartSymbolMatch"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547856%28v=vs.85%29.aspx
        "GetNextSymbolMatch": WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG, PULONG64)(37, "GetNextSymbolMatch"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff543008%28v=vs.85%29.aspx
        "EndSymbolMatch": WINFUNCTYPE(HRESULT, ULONG64)(38, "EndSymbolMatch"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554379%28v=vs.85%29.aspx
        "Reload": WINFUNCTYPE(HRESULT, c_char_p)(39, "Reload"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff556802%28v=vs.85%29.aspx
        "SetSymbolPath": WINFUNCTYPE(HRESULT, c_char_p)(41, "SetSymbolPath"),
    }


class IDebugSymbols2(COMInterface):
    _functions_ = dict(IDebugSymbols._functions_)
    _functions_.update({
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546747%28v=vs.85%29.aspx
        "GetFieldName": WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PVOID, ULONG, PULONG)(55, "GetFieldName"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546771%28v=vs.85%29.aspx
        "GetFieldTypeAndOffset": WINFUNCTYPE(HRESULT, ULONG64, ULONG, c_char_p, PULONG, PULONG)(105, "GetFieldTypeAndOffset"),
    })


class IDebugSymbols3(COMInterface):
    _functions_ = dict(IDebugSymbols2._functions_)
    _functions_.update({
    })


# https://msdn.microsoft.com/en-us/library/windows/hardware/ff550508%28v=vs.85%29.aspx
class IDebugControl(COMInterface):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, PVOID, PVOID)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release"),
        "GetInterrupt": ctypes.WINFUNCTYPE(HRESULT)(3, "GetInterrupt"),
        "SetInterrupt": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "SetInterrupt"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546675%28v=vs.85%29.aspx
        "GetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG)(49, "GetExecutionStatus"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff556693%28v=vs.85%29.aspx
        "SetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(50, "SetExecutionStatus"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff543208%28v=vs.85%29.aspx
        "Execute": ctypes.WINFUNCTYPE(HRESULT, ULONG, c_char_p, ULONG)(66, "Execute"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff537856%28v=vs.85%29.aspx
        "AddBreakpoint": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(72, "AddBreakpoint"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554487%28v=vs.85%29.aspx
        "RemoveBreakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "RemoveBreakpoint"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff561229%28v=vs.85%29.aspx
        "WaitForEvent": WINFUNCTYPE(HRESULT, DWORD, DWORD)(93, "WaitForEvent")
    }

# TEST DEBUG_VALUE #

class _DEBUG_VALUE_UNION(ctypes.Union):
        _fields_ = [
        ("I8", UCHAR),
        ("I16", USHORT),
        ("I32", ULONG),
        ("I64", ULONG64),
        ("RawBytes", UCHAR * 24)
    ]

class _DEBUG_VALUE(ctypes.Structure):
        VALUE_TRANSLATION_TABLE = {DEBUG_VALUE_INT8: "I8", DEBUG_VALUE_INT16: "I16",
            DEBUG_VALUE_INT32: "I32", DEBUG_VALUE_INT64: "I64"}

        _fields_ = [
        ("Value", _DEBUG_VALUE_UNION),
        ("TailOfRawBytes", ULONG),
        ("Type", ULONG),
    ]

        def get_value(self):
            if self.Type == 0:
                raise ValueError("DEBUG_VALUE at DEBUG_VALUE_INVALID")
            if self.Type not in self.VALUE_TRANSLATION_TABLE:
                # TODO: full _DEBUG_VALUE_UNION and implem other DEBUG_VALUE_XXX
                raise NotImplementedError("DEBUG_VALUE.Type == {0} (sorry)".format(self.Type))
            return getattr(self.Value, self.VALUE_TRANSLATION_TABLE[self.Type])

DEBUG_VALUE = _DEBUG_VALUE
PDEBUG_VALUE = POINTER(_DEBUG_VALUE)


# https://msdn.microsoft.com/en-us/library/windows/hardware/ff550825%28v=vs.85%29.aspx
class IDebugRegisters(COMInterface):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, PVOID, PVOID)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff547960%28v=vs.85%29.aspx
        "GetNumberRegisters": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetNumberRegisters"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546575%28v=vs.85%29.aspx
        "GetDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PULONG, PDEBUG_REGISTER_DESCRIPTION)(4, "GetDescription"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff546881%28v=vs.85%29.aspx
        "GetIndexByName": ctypes.WINFUNCTYPE(HRESULT, c_char_p, PULONG)(5, "GetIndexByName"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549476%28v=vs.85%29.aspx
        "GetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(6, "GetValue"),
        # https://msdn.microsoft.com/en-us/library/windows/hardware/ff556881%28v=vs.85%29.aspx
        "SetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(7, "SetValue"),

        # "GetValues": ctypes.WINFUNCTYPE(HRESULT)(8, "GetValues"),
        # "SetValues": ctypes.WINFUNCTYPE(HRESULT)(9, "SetValues"),

        "OutputRegisters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(10, "OutputRegisters"),
    }




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


# experimental decorator
# Just used to inform you that we are not sur if this code really works
# and that we are currently working on it
# (yes dbgengine type API is not simple nor complete)
def experimental(f):
    if IS_SPHINX_BUILD:
        f._do_not_generate_doc = True
    return f

class LocalKernelDebuggerBase(object):
    DEBUG_DLL_PATH = None
    DRIVER_FILENAME = None
    DRIVER_RESOURCE = None
    # Will be used if '_NT_SYMBOL_PATH' is not set
    DEFAULT_SYMBOL_PATH  = "SRV*{0}\\symbols*http://msdl.microsoft.com/download/symbols".format(realpath(dirname(__file__)))
    SYMBOL_OPT = None

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

    def _load_debug_dll(self):
        self.hmoduledbghelp = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "dbghelp.dll")
        self.hmoduledbgeng = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "dbgeng.dll")
        self.hmodulesymsrv = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "symsrv.dll")

    def _do_debug_create(self):
        DebugClient = IDebugClient(0)

        DebugCreateAddr = winproxy.GetProcAddress(self.hmoduledbgeng, "DebugCreate")
        DebugCreate = WINFUNCTYPE(HRESULT, PVOID, PVOID)(DebugCreateAddr)
        DebugCreate(IID_IDebugClient, byref(DebugClient))
        return DebugClient

    def _ask_other_interface(self):
        DebugClient = self.DebugClient
        self.DebugDataSpaces = IDebugDataSpaces2(0)
        self.DebugSymbols = IDebugSymbols3(0)
        self.DebugControl = IDebugControl(0)

        DebugClient.QueryInterface(IID_IDebugDataSpaces2, ctypes.byref(self.DebugDataSpaces))
        DebugClient.QueryInterface(IID_IDebugSymbols3, ctypes.byref(self.DebugSymbols))
        DebugClient.QueryInterface(IID_IDebugControl, ctypes.byref(self.DebugControl))

    def _wait_local_kernel_connection(self):
        self.DebugControl.WaitForEvent(0, 0xffffffff)
        return True

    def _setup_symbols_options(self):
        try:
            symbol_path = os.environ['_NT_SYMBOL_PATH']
        except KeyError:
            symbol_path = self.DEFAULT_SYMBOL_PATH
        self.DebugSymbols.SetSymbolPath(symbol_path)
        self.DebugSymbols.SetSymbolOption(self.SYMBOL_OPT)

    def get_number_modules(self):
        """Get the number of loaded and unloaded modules

           :returns: Number of loaded, unloaded modules -- int, int
        """
        numModulesLoaded = DWORD(0)
        numModulesUnloaded = DWORD(0)

        self.DebugSymbols.GetNumberModules(byref(numModulesLoaded), byref(numModulesUnloaded))
        return (numModulesLoaded.value, numModulesUnloaded.value)

    def get_module_by_index(self, i):
        """Get the base of module number **i**"""
        currModuleBase = ULONG64(0)

        self.DebugSymbols.GetModuleByIndex(i, byref(currModuleBase))
        return self.trim_ulong64_to_address(currModuleBase.value)

    def get_module_name_by_index(self, i):
        """Get the name of module number **i**"""
        currModuleBase = ULONG64(0)
        currModuleName = (c_char * 1024)()
        currImageName = (c_char * 1024)()
        currLoadedImageName = (c_char * 1024)()
        currModuleNameSize = DWORD(0)
        currImageNameSize = DWORD(0)
        currLoadedImageNameSize = DWORD(0)

        self.DebugSymbols.GetModuleByIndex(i, byref(currModuleBase))
        self.DebugSymbols.GetModuleNames(i, currModuleBase, byref(currImageName), 1023, byref(currImageNameSize),
                                         byref(currModuleName), 1023, byref(currModuleNameSize), byref(currLoadedImageName),
                                         1023, byref(currLoadedImageNameSize))
        return (currImageName.value, currModuleName.value, currLoadedImageName.value)

    def _load_modules_syms(self):
        currModuleName = (c_char * 1024)()
        currImageName = (c_char * 1024)()
        currLoadedImageName = (c_char * 1024)()
        currModuleNameSize = DWORD(0)
        currImageNameSize = DWORD(0)
        currLoadedImageNameSize = DWORD(0)
        currModuleBase = ULONG64(0)
        numModulesLoaded = DWORD(0)
        numModulesUnloaded = DWORD(0)

        self.DebugSymbols.GetNumberModules(byref(numModulesLoaded), byref(numModulesUnloaded))
        for i in range(numModulesLoaded.value):
            self.DebugSymbols.GetModuleByIndex(i, byref(currModuleBase))
            self.DebugSymbols.GetModuleNames(i, currModuleBase, byref(currImageName), 1023, byref(currImageNameSize),
                                             byref(currModuleName), 1023, byref(currModuleNameSize), byref(currLoadedImageName),
                                             1023, byref(currLoadedImageNameSize))
            self.DebugSymbols.Reload(currModuleName[:currModuleNameSize.value])

    # TODO: SymGetTypeInfo goto winfunc?
    def _init_dbghelp_func(self):
        # We need to hack our way to some dbghelp functions
        # Some info are not reachable through COM API
        # 0xf0f0f0f0 is the magic handler used by dbgengine for dbghelp

        dbghelp = ctypes.windll.DbgHelp
        SymGetTypeInfoPrototype = WINFUNCTYPE(BOOL, HANDLE, DWORD64, ULONG, IMAGEHLP_SYMBOL_TYPE_INFO, PVOID)
        SymGetTypeInfoParams = ((1, 'hProcess'), (1, 'ModBase'), (1, 'TypeId'), (1, 'GetType'), (1, 'pInfo'))
        self.SymGetTypeInfo_ctypes = SymGetTypeInfoPrototype(("SymGetTypeInfo", dbghelp), SymGetTypeInfoParams)

    # Internal helper
    def resolve_symbol(self, symbol):
        """| Return **symbol** if it's an :class:`int` else resolve it using :func:`get_symbol_offset`
           | Used by functions to either accept an :class:`int` or a windbg :class:`Symbol`"""
        if isinstance(symbol, (int, long)):
            return symbol
        x = self.get_symbol_offset(symbol)
        if x is None:
            raise ValueError("Unknow symbol <{0}>".format(symbol))
        return x

    def resolve_type(self, imodule, itype):
        """| Return **imodule** and **itype**  if they are an :class:`int` else
           | resolve then using respectively :func:`get_symbol_offset` and :func:`get_type_id`
           | Used by functions about types to either accept :class:`int` or windbg :class:`Symbol`
        """
        module = self.resolve_symbol(imodule)
        if isinstance(itype, (int, long)):
            return self.expand_address_to_ulong64(module), itype
        try:
            type = self.get_type_id(module, itype)
        except WindowsError:
            raise ValueError("Unkown type: <{0}!{1}>".format(imodule, itype))
        return self.expand_address_to_ulong64(module), type

    def _get_kldbgdrv_handle(self):
        if not hasattr(self, "_kldbgdrv_handle"):
            self._kldbgdrv_handle = windows.winproxy.CreateFileA("\\\\.\\kldbgdrv", GENERIC_READ | GENERIC_WRITE, FILE_SHARE_WRITE | FILE_SHARE_READ)
        return self._kldbgdrv_handle

    # Actual Interface
    def execute(self, str, to_string=False):
        r"""| Execute a windbg command
            | if **to_string** is False, use the current output callback
            | (see :file:`example\\output_demo.py`)
        """
        if to_string:
            old_output = self._output_callback
            self._init_string_output_callback()
        self.DebugControl.Execute(0, str, 0)
        if to_string:
            if old_output is None:
                old_output = self._standard_output_callback
            self.set_output_callbacks(old_output)
            return self._output_string
        return None

    def _standard_output_callback(self, x, y, msg):
        if not self.quiet:
            print msg,
        return 0

    def _init_string_output_callback(self):
        self._output_string = ""
        self.set_output_callbacks(self._string_output_callback)

    def _string_output_callback(self, x, y, msg):
        self._output_string += msg
        return 0

    def set_output_callbacks(self, callback):
        r"""| Register a new output callback, that must respect the interface of
           | :func:`IDebugOutputCallbacks::Output` `<https://msdn.microsoft.com/en-us/library/windows/hardware/ff550815%28v=vs.85%29.aspx>`_.
           | (see :file:`example\\output_demo.py`)
        """
        self._output_callback = callback
        my_idebugoutput_vtable = IDebugOutputCallbacksVtable.create_vtable(Output=callback)
        my_debugoutput_obj = ctypes.pointer(my_idebugoutput_vtable)
        res = self.DebugClient.SetOutputCallbacks(ctypes.addressof(my_debugoutput_obj))
        # Need to keep reference to these object else our output callback will be
        # garbage collected leading to crash
        # Update self.keep_alive AFTER the call to SetOutputCallbacks because
        # SetOutputCallbacks may call methods of the old my_debugoutput_obj
        self.keep_alive = [my_idebugoutput_vtable, my_debugoutput_obj]
        return res

    def get_modules(self):
        """Return a list of (currModuleName, currImageName, currLoadedImageName)"""
        self.reload("")
        currModuleName = (c_char * 1024)()
        currImageName = (c_char * 1024)()
        currLoadedImageName = (c_char * 1024)()
        currModuleNameSize = DWORD(0)
        currImageNameSize = DWORD(0)
        currLoadedImageNameSize = DWORD(0)
        currModuleBase = ULONG64(0)
        numModulesLoaded = DWORD(0)
        numModulesUnloaded = DWORD(0)

        self.DebugSymbols.GetNumberModules(byref(numModulesLoaded), byref(numModulesUnloaded))
        res = []
        for i in range(numModulesLoaded.value):
            self.DebugSymbols.GetModuleByIndex(i, byref(currModuleBase))
            self.DebugSymbols.GetModuleNames(i, c_uint64(currModuleBase.value), byref(currImageName), 1023, byref(currImageNameSize),
                                             byref(currModuleName), 1023, byref(currModuleNameSize), byref(currLoadedImageName),
                                             1023, byref(currLoadedImageNameSize))
            # Removing trailing \x00
            res.append((currModuleName[:currModuleNameSize.value - 1], currImageName[:currImageNameSize.value - 1], currLoadedImageName[:currLoadedImageNameSize.value - 1]))
        return res

    def reload(self, module_to_reload=""):
        """Reload a module or all modules if **module_to_reload** is not specified"""
        return self.DebugSymbols.Reload(module_to_reload)

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

    # type stuff
    @experimental
    def get_type(self, module, typeid):
        module, typeid = self.resolve_type(module, typeid)
        return DbgEngType(module, typeid, self)

    def get_type_id(self, module, type_name):
        """Get the typeid of a type

        :param module: the module containing the type
        :type module: Symbol
        :param type_name: the name of the type
        :type type_name: str
        :rtype: int"""
        module = self.resolve_symbol(module)
        res = ULONG(0)

        self.DebugSymbols.GetTypeId(self.expand_address_to_ulong64(module), type_name, byref(res))
        return res.value

    def get_symbol_type_id(self, symtype):
        """Get the module and typeid of a symbol

        :param symtype: the name of the type
        :type symtype: str
        :rtype: int, int -- module ID, type ID"""
        typeid = ULONG(0)
        module = ULONG64(0)

        self.DebugSymbols.GetSymbolTypeId(symtype, byref(typeid), byref(module))
        return (module.value, typeid.value)

    def get_field_offset(self, module, typeid, field):
        """Get the offset of a field in a type

        :rtype: int"""
        module, typeid = self.resolve_type(module, typeid)
        res = ULONG(0)

        self.DebugSymbols.GetFieldOffset(module, typeid, field, byref(res))
        return res.value

    def get_type_name(self, module, typeid):
        """Get the name of a type

        :rtype: str"""
        module, typeid = self.resolve_type(module, typeid)
        buffer_size = 1024
        buffer = (c_char * buffer_size)()
        name_size = ULONG(0)

        self.DebugSymbols.GetTypeName(module, typeid, byref(buffer), buffer_size, byref(name_size))
        res = buffer[:name_size.value]
        if res[-1] == "\x00":
            res = res[:-1]
        return res

    def get_type_size(self, module, typeid):
        """Get the size of a type

        :rtype: int"""
        module, typeid = self.resolve_type(module, typeid)
        res = ULONG(0)

        self.DebugSymbols.GetTypeSize(module, typeid, byref(res))
        return res.value

    def get_field_name(self, module, typeid, fieldindex):
        """Get the name of a field in a type

            :param fieldindex: Index of the field to retrieve
            :type fieldindex: int
            :rtype: int"""
        module, typeid = self.resolve_type(module, typeid)
        buffer_size = 1024
        buffer = (c_char * buffer_size)()
        name_size = ULONG(0)

        self.DebugSymbols.GetFieldName(module, typeid, fieldindex, byref(buffer), buffer_size, byref(name_size))
        res = buffer[:name_size.value]
        if res[-1] == "\x00":
            res = res[:-1]
        return res

    def get_field_type_and_offset(self, module, typeid, fieldname):
        """Get the type and the offset of a field in a type

        :param fieldname: The name of the field we want
        :type fieldname: str
        :rtype: int, int -- type ID, field offset"""
        module, typeid = self.resolve_type(module, typeid)
        fieldtypeid = ULONG(0)
        fieldoffset = ULONG(0)

        self.DebugSymbols.GetFieldTypeAndOffset(module, typeid, fieldname, byref(fieldtypeid), byref(fieldoffset))
        return fieldtypeid.value, fieldoffset.value

    # Custom type functions, it seems that COM api does not return all informations
    # we may need to directly call Dbghelp

    @experimental
    def get_all_field_generator(self, module, typeid):
        for i in itertools.count(0):
            try:
                name = self.get_field_name(module, typeid, i)
            except WindowsError:
                if i == 0:  # Empty struct: Error in call args
                    raise
                return
            yield name

    @experimental
    def get_all_field(self, module, typeid):
        return list(self.get_all_field_generator(module, typeid))

    @experimental
    def get_all_field_type_and_offset(self, module, typeid):
        fields = self.get_all_field(module, typeid)
        return [(f,) + self.get_field_type_and_offset(module, typeid, f) for f in fields]

    # def old_tst(self, module, typeid):
    #     for name, type, offset in self.get_all_field_type_and_offset(module, typeid):
    #         type_name = self.get_type_name(module, type)
    #         #print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #         if type_name.endswith("[]"):
    #             try:
    #                 sub_module, sub_type = self.resolve_type(module, type_name[:-2]) # Get the subtype if not a basic C type
    #                 size_of_elt = self.get_type_size(sub_module, sub_type)
    #                 is_base_type = False
    #             except ValueError: # If it's an array of basic type
    #                 sub_module, sub_type = self.get_symbol_type_id(type_name[:-2])
    #                 size_of_elt = self.get_type_size(sub_module, sub_type)
    #                 is_base_type = True
    #             nb_elt = self.get_type_size(module, type) / size_of_elt
    #             print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #             print "ARRAY of {0} | {1}".format(nb_elt, "BASE_TYPE" if is_base_type else "NO BASE TYPE")
    #
    #             if not is_base_type:
    #                 print("PARSING {0}".format(type_name[:-2]))
    #                 self.tst(sub_module, sub_type)
    #             # use kdbg.get_symbol_type_id("nt!_KPRCB.HalReserved[0]") ?
    #             # or look at ctypes.windll.Dbghelp.SymGetTypeInfo ?

    # def tst(self, module, typeid):
    #     "Create Ctypes"
    #     next_offset = 0
    #     last_offset = -1
    #     for name, type, offset in self.get_all_field_type_and_offset(module, typeid):
    #         type_name = self.get_type_name(module, type)
    #
    #         if offset == 0x2dec:
    #             print("----")
    #             print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #             x = self.SymGetTypeInfo(module, type, TI_GET_BITPOSITION)
    #             print("TI_GET_BITPOSITION -> {0}".format(x))
    #             x = self.SymGetTypeInfo(module, type, TI_GET_LENGTH)
    #             print("TI_GET_LENGTH -> {0}".format(x))
    #
    #         #if type_name.endswith("[]"):
    #         #    print("-------")
    #         #    print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #         #    sub_type = self.SymGetTypeInfo(module, type, TI_GET_TYPE)
    #         #    print("ARRAY OF {0}".format(self.get_type_name(module, sub_type)))
    #
    #         x = self.SymGetTypeInfo(module, type, TI_GET_BITPOSITION)
    #         #print(x)
    #         if x:
    #             print("-------")
    #             print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #             print("BITFIELD POS {0}".format(x))
    #
    #
    #         # HANDLE ARRAY
    #         #if type_name.endswith("[]"):
    #         #    try:
    #         #        sub_module, sub_type = self.resolve_type(module, type_name[:-2]) # Get the subtype if not a basic C type
    #         #        size_of_elt = self.get_type_size(sub_module, sub_type)
    #         #        is_base_type = False
    #         #    except ValueError: # If it's an array of basic type
    #         #        sub_module, sub_type = self.get_symbol_type_id(type_name[:-2])
    #         #        size_of_elt = self.get_type_size(sub_module, sub_type)
    #         #        is_base_type = True
    #         #    nb_elt = self.get_type_size(module, type) / size_of_elt
    #         #    print("+{0} {1}: {2}({3})".format(hex(offset), name, type_name, type))
    #         #    print "ARRAY of {0} | {1}".format(nb_elt, "BASE_TYPE" if is_base_type else "NO BASE TYPE")
    #         #    # use kdbg.get_symbol_type_id("nt!_KPRCB.HalReserved[0]") ?
    #         #    # or look at ctypes.windll.Dbghelp.SymGetTypeInfo ?

    # Low level DbgHelp queries
    @experimental
    def SymGetTypeInfo(self, module, typeid, GetType, ires=None):
        # If not: result is a DWORD
        res = ires
        if res is None:
            if GetType == TI_FINDCHILDREN or GetType == TI_GET_VALUE:
                raise NotImplementedError("SymGetTypeInfo with GetType == TI_FINDCHILDREN need struct passed as argument")

            result_type = {
                TI_GET_SYMNAME: c_wchar_p, TI_GET_LENGTH: ULONG64,
                TI_GET_ADDRESS: ULONG64, TI_GTIEX_REQS_VALID: ULONG64,
            }
            res = result_type.get(GetType, DWORD)()

        module, typeid = self.resolve_type(module, typeid)
        self.SymGetTypeInfo_ctypes(0xf0f0f0f0, module, typeid, GetType, byref(res))
        if ires is None:
            return res.value
        return res

    @experimental
    def get_number_chid(self, module, typeid):
        module, typeid = self.resolve_type(module, typeid)
        return self.SymGetTypeInfo(module, typeid, TI_GET_CHILDRENCOUNT)

    @experimental
    def get_childs_types(self, module, typeid):
        nb_childs = self.get_number_chid(module, typeid)

        class res_struct(Structure):
            _fields_ = [("Count", ULONG), ("Start", ULONG), ("Types", (ULONG * nb_childs))]
            _fields_ = [("Count", ULONG), ("Start", ULONG), ("Types", (ULONG * nb_childs))]

        res = res_struct()
        res.Count = nb_childs
        self.SymGetTypeInfo(module, typeid, TI_FINDCHILDREN, ires=res)
        return res

    def trim_ulong64_to_address(self, addr):
        """ | Used to convert a symbol ULONG64 to the actual symbol.
            | Problem is that in a 32bits kernel the kernel address are bit expended
            | :file:`nt` in 32bits kernel would not be :file:`0x8xxxxxxx` but :file:`0xffffffff8xxxxxxx`
            """
        raise NotImplementedError("bitness dependent")

    def expand_address_to_ulong64(self, addr):
        """| Used to convert a symbol address to an ULONG64 requested by the API.
           | Problem is that in a 32bits kernel the kernel address are bit expended
           | :file:`nt` in 32bits kernel would not be :file:`0x8xxxxxxx` but :file:`0xffffffff8xxxxxxx`
           """
        raise NotImplementedError("bitness dependent")

    def get_symbol_offset(self, name):
        """Get the address of a symbol

        :param name: Name of the symbol
        :type name: str
        :rtype: int"""
        SymbolLocation = ctypes.c_uint64(0)
        try:
            self.DebugSymbols.GetOffsetByName(name, ctypes.byref(SymbolLocation))
        except WindowsError:
            return None
        return self.trim_ulong64_to_address(SymbolLocation.value)

    def get_symbol(self, addr):
        """Get the symbol and displacement of an address

        :param addr: The address to lookup
        :type addr: int
        :rtype: str, int -- symbol name, displacement"""
        addr = self.expand_address_to_ulong64(addr)
        buffer_size = 1024
        buffer = (c_char * buffer_size)()
        name_size = ULONG()
        displacement = ULONG64()
        try:
            self.DebugSymbols.GetNameByOffset(addr, byref(buffer), buffer_size, byref(name_size), byref(displacement))
        except WindowsError as e:
            if (e.winerror & 0xffffffff) == E_FAIL:
                return (None, None)
        return (buffer.value, displacement.value)

    def symbol_match(self, symbol_pattern):
        """| <generator>
           | List of symbol (name, address) that match a symbol pattern

           :param symbol_pattern: The symbol pattern (nt!Create*, *!CreateFile, ..)
           :type symbol_pattern: str
           :yield: str, int -- symbol name, symbol address
        """
        search_handle = ULONG64()
        buffer_size = 1024
        buffer = (c_char * buffer_size)()
        match_size = ULONG()
        symbol_addr = ULONG64()

        self.DebugSymbols.StartSymbolMatch(symbol_pattern, byref(search_handle))
        while True:
            try:
                self.DebugSymbols.GetNextSymbolMatch(search_handle, byref(buffer), buffer_size, byref(match_size), byref(symbol_addr))
            except WindowsError as e:
                if (e.winerror & 0xffffffff) == S_FALSE:
                    buffer_size = buffer_size
                    buffer = (c_char * buffer_size)()
                    continue
                if (e.winerror & 0xffffffff) == E_NOINTERFACE:
                    self.DebugSymbols.EndSymbolMatch(search_handle)
                    return
            yield (buffer.value, self.trim_ulong64_to_address(symbol_addr.value))

    def read_virtual_memory(self, addr, size):
        """Read the memory at a given virtual address

           :param addr: The Symbol to read from
           :type addr: Symbol
           :param size: The size to read
           :type size: int
           :returns: str
        """
        addr = self.resolve_symbol(addr)
        buffer = (c_char * size)()
        read = DWORD(0)

        self.DebugDataSpaces.ReadVirtual(c_uint64(addr), buffer, size, byref(read))
        return buffer[0:read.value]

    def write_virtual_memory(self, addr, data):
        """Write data to a given virtual address

           :param addr: The Symbol to write to
           :type addr: Symbol
           :param size: The Data to write
           :type size: str or ctypes.Structure
           :returns: the size written -- :class:`int`
        """
        try:
            # ctypes structure
            size = ctypes.sizeof(data)
            buffer = ctypes.byref(data)
        except TypeError:
            # buffer
            size = len(data)
            buffer = data
        written = ULONG(0)
        addr = self.resolve_symbol(addr)
        self.DebugDataSpaces.WriteVirtual(c_uint64(addr), buffer, size, byref(written))
        return written.value

    def write_pfv_memory(self, addr, data):
        """Write physical memory from virtual address
           Exactly the same as write_physical(virtual_to_physical(addr), data)
        """
        return self.write_physical_memory(self.virtual_to_physical(addr), data)

    def read_virtual_memory_into(self, addr, struct):
        """"Read the memory at a given virtual address into a ctypes Structure

           :param addr: The Symbol to read from
           :type addr: Symbol
           :param struct: The structure to fill
           :type size: ctypes.Structure
           :returns: the size read -- :class:`int`
        """
        addr = self.resolve_symbol(addr)
        size = ctypes.sizeof(struct)
        read = ULONG(0)

        self.DebugDataSpaces.ReadVirtual(c_uint64(addr), byref(struct), size, byref(read))
        return read.value

    def read_byte(self, addr):
        """Read a byte from virtual memory"""
        sizeof_byte = sizeof(BYTE)

        raw_data = self.read_virtual_memory(addr, sizeof_byte)
        return struct.unpack("<B", raw_data)[0]

    def read_byte_p(self, addr):
        """Read a byte from physical memory"""
        sizeof_byte = sizeof(BYTE)

        raw_data = self.read_physical_memory(addr, sizeof_byte)
        return struct.unpack("<B", raw_data)[0]

    def read_word(self, addr):
        """Read a word from virtual memory"""
        sizeof_word = sizeof(WORD)

        raw_data = self.read_virtual_memory(addr, sizeof_word)
        return struct.unpack("<H", raw_data)[0]

    def read_word_p(self, addr):
        """Read a word from physical memory"""
        sizeof_word = sizeof(WORD)

        raw_data = self.read_physical_memory(addr, sizeof_word)
        return struct.unpack("<H", raw_data)[0]

    def read_dword(self, addr):
        """Read a dword from virtual memory"""
        sizeof_dword = ctypes.sizeof(DWORD)

        raw_data = self.read_virtual_memory(addr, sizeof_dword)
        return struct.unpack("<I", raw_data)[0]

    def read_dword_p(self, addr):
        """Read a dword from physical memory"""
        sizeof_dword = ctypes.sizeof(DWORD)

        raw_data = self.read_physical_memory(addr, sizeof_dword)
        return struct.unpack("<I", raw_data)[0]

    def read_qword(self, addr):
        """Read a qword from virtual memory"""
        sizeof_qword = sizeof(ULONG64)

        raw_data = self.read_virtual_memory(addr, sizeof_qword)
        return struct.unpack("<Q", raw_data)[0]

    def read_qword_p(self, addr):
        """Read a qword from physical memory"""
        sizeof_qword = sizeof(ULONG64)

        raw_data = self.read_physical_memory(addr, sizeof_qword)
        return struct.unpack("<Q", raw_data)[0]

    def write_byte(self, addr, byte):
        """Read a byte to virtual memory"""
        return self.write_virtual_memory(addr, struct.pack("<B", byte))

    def write_byte_p(self, addr, byte):
        """write a byte to physical memory"""
        return self.write_physical_memory(addr, struct.pack("<B", byte))

    def write_word(self, addr, word):
        """write a word to virtual memory"""
        return self.write_virtual_memory(addr, struct.pack("<H", word))

    def write_word_p(self, addr, word):
        """write a word to physical memory"""
        return self.write_physical_memory(addr, struct.pack("<H", word))

    def write_dword(self, addr, dword):
        """write a dword to virtual memory"""
        return self.write_virtual_memory(addr, struct.pack("<I", dword))

    def write_dword_p(self, addr, dword):
        """write a dword to physical memory"""
        return self.write_physical_memory(addr, struct.pack("<I", dword))

    def write_qword(self, addr, qword):
        """write a qword to virtual memory"""
        return self.write_virtual_memory(addr, struct.pack("<Q", qword))

    def write_qword_p(self, addr, qword):
        """write a qword to physical memory"""
        return self.write_physical_memory(addr, struct.pack("<Q", qword))

    def read_ptr(self, addr):
        """Read a pointer from virtual memory"""
        raise NotImplementedError("bitness dependent")

    def read_ptr_p(self, addr):
        """Read a pointer from physical memory"""
        raise NotImplementedError("bitness dependent")

    def write_ptr(self, addr, value):
        """Write a pointer to virtual memory"""
        raise NotImplementedError("bitness dependent")

    def write_ptr_p(self, addr, value):
        """Write a pointer to physical memory"""
        raise NotImplementedError("bitness dependent")

    def write_msr(self, msr_id, value):
        """Write a Model Specific Register"""
        return self.DebugDataSpaces.WriteMsr(msr_id, value)

    def read_msr(self, msr_id):
        """Read a Model Specific Register"""
        msr_value = ULONG64()

        self.DebugDataSpaces.ReadMsr(msr_id, byref(msr_value))
        return msr_value.value

    def virtual_to_physical(self, virtual):
        """Get the physical address of a virtual one"""
        virtual = self.resolve_symbol(virtual)
        res = ULONG64(0)

        self.DebugDataSpaces.VirtualToPhysical(c_uint64(virtual), byref(res))
        return res.value

    def read_physical_memory(self, addr, size):
        """Read the physical memory at a given address

           :param addr: The Symbol to read from
           :type addr: Symbol
           :param size: The size to read
           :type size: int
           :returns: :class:`str`
        """

        buffer = (c_char * size)()
        read = DWORD(0)

        self.DebugDataSpaces.ReadPhysical(c_uint64(addr), buffer, size, byref(read))
        return buffer[0:read.value]

    def write_physical_memory(self, addr, data):
        """Write data to a given physical address

           :param addr: The Symbol to write to
           :type addr: Symbol
           :param size: The Data to write
           :type size: str or ctypes.Structure
           :returns: the size written -- :class:`int`
        """
        try:
            # ctypes structure
            size = ctypes.sizeof(data)
            buffer = ctypes.byref(data)
        except TypeError:
            # buffer
            size = len(data)
            buffer = data
        written = ULONG(0)
        self.DebugDataSpaces.WritePhysical(c_uint64(addr), buffer, size, byref(written))
        return written.value

    def read_processor_system_data(self, processor, type):
        """| Returns a :class:`DEBUG_PROCESSOR_IDENTIFICATION_X86` if type is :class:`DEBUG_DATA_PROCESSOR_IDENTIFICATION`
           | else returns an :class:`int`

           (see :func:`ReadProcessorSystemData` `<https://msdn.microsoft.com/en-us/library/windows/hardware/ff554326%28v=vs.85%29.aspx>`_.)
        """
        if type == DEBUG_DATA_PROCESSOR_IDENTIFICATION:
            buffer = DEBUG_PROCESSOR_IDENTIFICATION_ALL()
        elif type == DEBUG_DATA_PROCESSOR_SPEED:
            buffer = ULONG(0)
        else:
            buffer = ULONG64(0)
        data_size = ULONG(0)
        self.DebugDataSpaces.ReadProcessorSystemData(processor, type, byref(buffer), sizeof(buffer), byref(data_size))
        if type != DEBUG_DATA_PROCESSOR_IDENTIFICATION:
            buffer = buffer.value
        return buffer

    def read_bus_data(self, datatype, busnumber, slot, offset, size):
        r"""| Read on bus data, only current known use is to read on the PCI bus.
            | (see :file:`example\\simple_pci_exploration.py`)
        """
        buffer = (c_char * size)()
        read = ULONG(0)

        self.DebugDataSpaces.ReadBusData(datatype, busnumber, slot, offset, buffer, size, byref(read))
        return buffer[0:read.value]

    def write_bus_data(self, datatype, busnumber, slot, offset, data):
        r"""| Write on bus data, only current known use is to write on the PCI bus.
            | (see :file:`example\\simple_pci_exploration.py`)
        """
        size = len(data)
        written = ULONG(0)

        self.DebugDataSpaces.ReadBusData(datatype, busnumber, slot, offset, buffer, size, byref(written))
        return written.value

    def read_io(self, port, size):
        """| Perform an IN operation
           | might be subject to some restrictions
           | (see :file:`README.md` :file:`do_in | do_out VS read_io | write_io`)

           :param port: port to read
           :param size: size to read
           :type port: int
           :type size: int - 1, 2 or 4
           :returns: the value read -- :class:`int`
        """
        InterfaceType = 1  # Isa
        BusNumber = 0
        AddressSpace = 1
        Buffer = (c_char * size)()
        BytesRead = ULONG()
        self.DebugDataSpaces.ReadIo(InterfaceType, BusNumber, AddressSpace, port, Buffer, size, byref(BytesRead))
        format = {1: '<B', 2: '<H', 4: '<I'}[size]
        return struct.unpack(format, Buffer[:BytesRead.value])[0]

    def write_io(self, port, value, size=None):
        """| Perform an OUT operation
           | might be subject to some restrictions
           | (see :file:`README.md` :file:`do_in | do_out VS read_io | write_io`)

           :param port: port to write
           :param size: size to write
           :type port: int
           :type size: int - 1, 2 or 4
           :returns: the number of bytes written -- :class:`int`
        """
        InterfaceType = 1  # Isa
        BusNumber = 0
        AddressSpace = 1
        if size is None:
            size = len(value)
            Buffer = value
        else:
            format = {1: '<B', 2: '<H', 4: '<I'}[size]
            Buffer = struct.pack(format, value)
        BytesWritten = ULONG()
        self.DebugDataSpaces.WriteIo(InterfaceType, BusNumber, AddressSpace, port, Buffer, size, byref(BytesWritten))
        return BytesWritten.value

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

class LocalKernelDebugger32(LocalKernelDebuggerBase):
    DEBUG_DLL_PATH = os.path.join(realpath(dirname(__file__)), "bin\\DBGDLL\\")
    DRIVER_FILENAME = os.path.join(realpath(dirname(__file__)), "bin\\windbg_driver_x86.sys")
    DRIVER_RESOURCE = resource_emulation.Ressource(DRIVER_FILENAME, 0x7777, 0x4444)
    SYMBOL_OPT = (SYMOPT_NO_IMAGE_SEARCH + SYMOPT_AUTO_PUBLICS + SYMOPT_FAIL_CRITICAL_ERRORS +
                  SYMOPT_OMAP_FIND_NEAREST + SYMOPT_LOAD_LINES + SYMOPT_DEFERRED_LOADS +
                  SYMOPT_UNDNAME + SYMOPT_CASE_INSENSITIVE)

    # In our 32bits dll, GetModuleFileNameW and FindResourceW are not in IAT
    # There is a safe and secure lazy resolution, so let's just hook this jump table
    GetModuleFileNameW_addr_jump_offset = 0x3374bc
    FindResourceW_addr_jump_offset = 0x3374a0

    # read_ptr and write_ptr real implementation (bitness dependant)
    read_ptr = LocalKernelDebuggerBase.read_dword
    read_ptr_p = LocalKernelDebuggerBase.read_dword_p
    write_ptr = LocalKernelDebuggerBase.write_dword
    write_ptr_p = LocalKernelDebuggerBase.write_dword_p

    def expand_address_to_ulong64(self, addr):
        if addr is None:
            return None
        # bit expansion
        return (0xFFFFFFFF00000000 * (addr >> 31)) | addr

    def trim_ulong64_to_address(self, addr):
        if addr is None:
            return None
        return addr & 0xffffffff

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
        target = self.resolve_symbol(target)
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


class LocalKernelDebugger64(LocalKernelDebuggerBase):
    DEBUG_DLL_PATH = os.path.join(realpath(dirname(__file__)), "bin\\DBGDLL64\\")
    DRIVER_FILENAME = os.path.join(realpath(dirname(__file__)), "bin\\windbg_driver_x64.sys")
    DRIVER_RESOURCE = resource_emulation.Ressource(DRIVER_FILENAME, 0x7777, 0x4444)
    SYMBOL_OPT = (SYMOPT_NO_IMAGE_SEARCH + SYMOPT_AUTO_PUBLICS + SYMOPT_FAIL_CRITICAL_ERRORS +
                  SYMOPT_OMAP_FIND_NEAREST + SYMOPT_LOAD_LINES + SYMOPT_DEFERRED_LOADS +
                  SYMOPT_UNDNAME + SYMOPT_CASE_INSENSITIVE)

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

    def expand_address_to_ulong64(self, addr):
        return addr

    def trim_ulong64_to_address(self, addr):
        return addr

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
        target = self.resolve_symbol(target)
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

# # We are working on this part, we don't know if we will use it
# # We don't know if it really works
# # We keep that here for information purposes

DEBUG_INTERRUPT_ACTIVE  = 0
DEBUG_END_ACTIVE_DETACH = 0x00000002

DEBUG_BREAKPOINT_CODE = 0
DEBUG_BREAKPOINT_DATA = 1
DEBUG_BREAKPOINT_TIME = 2


# Breakpoint flags.
# Go-only breakpoints are only active when
# the engine is in unrestricted execution
# mode.  They do not fire when the engine
# is stepping.
DEBUG_BREAKPOINT_GO_ONLY  =  0x00000001
# A breakpoint is flagged as deferred as long as
# its offset expression cannot be evaluated.
# A deferred breakpoint is not active.
DEBUG_BREAKPOINT_DEFERRED = 0x00000002
DEBUG_BREAKPOINT_ENABLED  = 0x00000004
# The adder-only flag does not affect breakpoint
# operation.  It is just a marker to restrict
# output and notifications for the breakpoint to
# the client that added the breakpoint.  Breakpoint
# callbacks for adder-only breaks will only be delivered
# to the adding client.  The breakpoint can not
# be enumerated and accessed by other clients.
DEBUG_BREAKPOINT_ADDER_ONLY = 0x00000008
# One-shot breakpoints automatically clear themselves
# the first time they are hit.
DEBUG_BREAKPOINT_ONE_SHOT = 0x00000010

# Data breakpoint access types.
# Different architectures support different
# sets of these bits.
DEBUG_BREAK_READ    = 0x00000001
DEBUG_BREAK_WRITE   = 0x00000002
DEBUG_BREAK_EXECUTE = 0x00000004
DEBUG_BREAK_IO      = 0x00000008

DEBUG_ANY_ID = 0xffffffff

from breakpoint import WinBreakpoint

# TODO keep the register_info list in the object
class TargetRegisters(IDebugRegisters):
    """This class suppose that the list of registers does not change for a given target"""

    def get_number_registers(self):
        res = ULONG()
        self.GetNumberRegisters(ctypes.byref(res))
        return res.value

    def get_register_name(self, index):
        name_size = ULONG()
        self.GetDescription(index, None, 0, ctypes.byref(name_size), None)
        bsize = name_size.value
        buffer = (c_char * bsize)()
        self.GetDescription(index, buffer, bsize, ctypes.byref(name_size), None)
        return buffer[:name_size.value - 1]

    def list_registers(self):
        return [self.get_register_name(i) for i in range(self.get_number_registers())]

    def get_register_value(self, index):
        res = DEBUG_VALUE()
        self.GetValue(index, ctypes.byref(res))
        return res.get_value()

    def get_register_value_by_name(self, name):
        regs_name = self.list_registers()
        if name.lower() not in regs_name:
            raise ValueError("Unknown register <{0}>".format(name))
        return self.get_register_value(regs_name.index(name.lower()))

    __getitem__ = get_register_value_by_name

    def output(self):
        self.OutputRegisters(0, 0)


class RemoteDebugger(LocalKernelDebugger32):
    def __init__(self, connect_string):
        self.quiet = False
        self._load_debug_dll()
        self.DebugClient = self._do_debug_create()
        self._do_kernel_attach(connect_string)
        self._ask_other_interface()
        self._setup_symbols_options()
        self.set_output_callbacks(self._standard_output_callback)
        self.DebugControl.SetInterrupt(DEBUG_INTERRUPT_ACTIVE)
        self._wait_local_kernel_connection()
        self._load_modules_syms()
        self.reload()

    def _do_kernel_attach(self, str):
        DEBUG_ATTACH_LOCAL_KERNEL = 1
        DEBUG_ATTACH_KERNEL_CONNECTION = 0x00000000
        res = self.DebugClient.AttachKernel(DEBUG_ATTACH_KERNEL_CONNECTION, str)
        if res:
            raise WinError(res)

    def _ask_other_interface(self):
        super(RemoteDebugger, self)._ask_other_interface()
        DebugClient = self.DebugClient
        self.DebugRegisters = TargetRegisters(0)

        DebugClient.QueryInterface(IID_IDebugRegisters, ctypes.byref(self.DebugRegisters))
        self.registers = self.DebugRegisters



    def detach(self):
        self.DebugClient.EndSession(DEBUG_END_ACTIVE_DETACH)

    def get_execution_status(self):
        res = ULONG()
        self.DebugControl.GetExecutionStatus(ctypes.byref(res))
        return res.value

    def set_execution_status(self, status):
        return self.DebugControl.SetExecutionStatus(status)

    def add_breakpoint(self):
        bp = WinBreakpoint(0, self)
        self.DebugControl.AddBreakpoint(DEBUG_BREAKPOINT_CODE, DEBUG_ANY_ID, ctypes.byref(bp))
        return bp

    def cont(self):
        return self.DebugControl.WaitForEvent(0, 0xffffffff)

    def get_register_index(self, name):
        res = ULONG()
        self.DebugRegisters.GetIndexByName(name, ctypes.byref(res))
        return res.value




