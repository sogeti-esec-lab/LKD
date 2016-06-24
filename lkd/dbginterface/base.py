from __future__ import print_function

import os
from os.path import realpath, dirname
import struct
import itertools
import functools
import ctypes
from ctypes import byref, WINFUNCTYPE, HRESULT, WinError

import windows
import windows.winproxy as winproxy
from windows.generated_def.winstructs import *
from lkd.dbgdef import *
from lkd.dbgcom import *
from lkd.dbgtype import DbgEngType
import lkd.dbgfuncs

# Based on the trick used in PRAW
# http://stackoverflow.com/a/22023805
IS_SPHINX_BUILD = bool(os.environ.get('SPHINX_BUILD', '0'))


cast_to_char_p = lambda buff: ctypes.cast(byref(buff), ctypes.c_char_p)
# DBG function

class DbgEngProxy(windows.winproxy.ApiProxy):
    APIDLL = "dbgeng.dll"
    default_error_check = staticmethod(windows.winproxy.kernel32_zero_check)


class DbgHelpProxy(windows.winproxy.ApiProxy):
    APIDLL = "dbghelp.dll"
    default_error_check = staticmethod(windows.winproxy.kernel32_zero_check)


@DbgEngProxy("DebugCreate", deffunc_module=lkd.dbgfuncs)
def DebugCreate(InterfaceId, Interface):
    return DebugCreate.ctypes_function(InterfaceId, Interface)


@DbgHelpProxy("SymGetTypeInfo", deffunc_module=lkd.dbgfuncs)
def SymGetTypeInfo(hProcess, ModBase, TypeId, GetType, pInfo):
    return SymGetTypeInfo.ctypes_function(hProcess, ModBase, TypeId, GetType, pInfo)


# COM Vtable for python output
class CustomOuput(COMImplementation):
    IMPLEMENT = IDebugOutputCallbacks

    def __init__(self, output):
        super(CustomOuput, self).__init__()
        self.output_func = output

    def Output(self, this, x, msg):
        if self.output_func is not None:
            return self.output_func(this, x, msg)
        return 0
custom_ouput = CustomOuput(None)


# experimental decorator
# Just used to inform you that we are not sur if this code really works
# and that we are currently working on it
# (yes dbgengine type API is not simple nor complete)
def experimental(f):
    if IS_SPHINX_BUILD:
        f._do_not_generate_doc = True
    return f

class BaseKernelDebugger(object):
    # TODO: remove me
    _internal_offset_cache = {}
    # Will be used if '_NT_SYMBOL_PATH' is not set
    DEFAULT_SYMBOL_PATH  = "SRV*{0}\\symbols*http://msdl.microsoft.com/download/symbols".format(realpath(dirname(dirname(__file__))))
    SYMBOL_OPT = (SYMOPT_NO_IMAGE_SEARCH + SYMOPT_AUTO_PUBLICS + SYMOPT_FAIL_CRITICAL_ERRORS +
                  SYMOPT_OMAP_FIND_NEAREST + SYMOPT_LOAD_LINES + SYMOPT_DEFERRED_LOADS +
                  SYMOPT_UNDNAME + SYMOPT_CASE_INSENSITIVE)

    #def __init__(self, quiet=True):
    #    self.quiet = quiet
    #    self._output_string = ""
    #    self._output_callback = None
    #    self._load_debug_dll()
    #    self.DebugClient = self._do_debug_create()
    #    self._do_kernel_attach()
    #    self._ask_other_interface()
    #    self._setup_symbols_options()
    #    self.set_output_callbacks(self._standard_output_callback)
    #    self._wait_local_kernel_connection()
    #    self._load_modules_syms()
    #    self.reload()
    #    self._init_dbghelp_func()
    #    self._upgrade_driver()

    def _load_debug_dll(self):
        self.hmoduledbghelp = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "dbghelp.dll")
        self.hmoduledbgeng = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "dbgeng.dll")
        self.hmodulesymsrv = winproxy.LoadLibraryA(self.DEBUG_DLL_PATH + "symsrv.dll")

    def _do_debug_create(self):
        DebugClient = IDebugClient(0)
        DebugCreate(IDebugClient.IID, byref(DebugClient))
        return DebugClient

    def _ask_other_interface(self):
        DebugClient = self.DebugClient
        self.DebugDataSpaces = IDebugDataSpaces2(0)
        self.DebugSymbols = IDebugSymbols3(0)
        self.DebugControl = IDebugControl(0)

        DebugClient.QueryInterface(self.DebugDataSpaces.IID, byref(self.DebugDataSpaces))
        DebugClient.QueryInterface(self.DebugSymbols.IID, byref(self.DebugSymbols))
        DebugClient.QueryInterface(self.DebugControl.IID, byref(self.DebugControl))

    def _setup_symbols_options(self):
        symbol_path = os.environ.get('_NT_SYMBOL_PATH', self.DEFAULT_SYMBOL_PATH)
        self.DebugSymbols.SetSymbolPath(symbol_path)
        self.DebugSymbols.SetSymbolOptions(self.SYMBOL_OPT)

    def _wait_local_kernel_connection(self):
        self.DebugControl.WaitForEvent(0, 0xffffffff)
        return True

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
            self.DebugSymbols.GetModuleNames(i, currModuleBase, ctypes.cast(byref(currImageName), c_char_p), 1023, byref(currImageNameSize),
                                             ctypes.cast(byref(currModuleName), c_char_p), 1023, byref(currModuleNameSize), ctypes.cast(byref(currLoadedImageName), c_char_p),
                                             1023, byref(currLoadedImageNameSize))
            self.DebugSymbols.Reload(currModuleName[:currModuleNameSize.value])

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

    # TODO: SymGetTypeInfo goto winfunc?
    #def _init_dbghelp_func(self):
    #    # We need to hack our way to some dbghelp functions
    #    # Some info are not reachable through COM API
    #    # 0xf0f0f0f0 is the magic handler used by dbgengine for dbghelp
    #
    #    dbghelp = ctypes.windll.DbgHelp
    #    SymGetTypeInfoPrototype = WINFUNCTYPE(BOOL, HANDLE, DWORD64, ULONG, IMAGEHLP_SYMBOL_TYPE_INFO, PVOID)
    #    SymGetTypeInfoParams = ((1, 'hProcess'), (1, 'ModBase'), (1, 'TypeId'), (1, 'GetType'), (1, 'pInfo'))
    #    self.SymGetTypeInfo_ctypes = SymGetTypeInfoPrototype(("SymGetTypeInfo", dbghelp), SymGetTypeInfoParams)
    #    self.SymGetTypeInfo_ctypes.errcheck =  functools.partial(windows.winproxy.kernel32_error_check, "SymGetTypeInfo")

    # Internal helper
    def resolve_symbol(self, symbol):
        """| Return **symbol** if it's an :class:`int` else resolve it using :func:`get_symbol_offset`
           | Used by functions to either accept an :class:`int` or a windbg :class:`Symbol`"""
        if isinstance(symbol, (int, long)):
            return self.expand_address_to_ulong64(symbol)
        x = self.get_symbol_offset(symbol)
        if x is None:
            raise ValueError("Unknow symbol <{0}>".format(symbol))
        return self.expand_address_to_ulong64(x)

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

    def disas_one(self, addr):
        addr = self.resolve_symbol(addr)
        size = 1000
        buffer = (ctypes.c_char * size)()
        res_size = ULONG()
        end = ULONG64()
        self.DebugControl.Disassemble(addr, 0, buffer, size, byref(res_size), byref(end))
        return (buffer[:res_size.value].strip("\n\x00"), end.value)

    def disassemble(self, addr, nb_instr):
        res = []
        for i in range(nb_instr):
            x, addr = self.disas_one(addr)
            res.append(x)
        return res

    def print_disas(self, addr, nb_instr):
        for i in self.disassemble(addr, nb_instr):
            print(i)

    def _standard_output_callback(self, x, y, msg):
        if not self.quiet:
            print (msg, end='')
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
        custom_ouput.output_func = callback
        res = self.DebugClient.SetOutputCallbacks(custom_ouput)
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
            self.DebugSymbols.GetModuleNames(i, c_uint64(currModuleBase.value), cast_to_char_p(currImageName), 1023, byref(currImageNameSize),
                                             cast_to_char_p(currModuleName), 1023, byref(currModuleNameSize), cast_to_char_p(currLoadedImageName),
                                             1023, byref(currLoadedImageNameSize))
            # Removing trailing \x00
            res.append((currModuleName[:currModuleNameSize.value - 1], currImageName[:currImageNameSize.value - 1], currLoadedImageName[:currLoadedImageNameSize.value - 1]))
        return res

    def reload(self, module_to_reload=""):
        """Reload a module or all modules if **module_to_reload** is not specified"""
        return self.DebugSymbols.Reload(module_to_reload)

    def get_symbol_offset(self, name):
        """Get the address of a symbol

        :param name: Name of the symbol
        :type name: str
        :rtype: int"""
        print("[TODO]: REMOVE ME")
        if name in self._internal_offset_cache:
            return self._internal_offset_cache[name]
        print("[RESOLVING] {0}".format(name))
        SymbolLocation = ctypes.c_uint64(0)
        try:
            self.DebugSymbols.GetOffsetByName(name, byref(SymbolLocation))
        except WindowsError:
            return None
        self._internal_offset_cache[name] = self.trim_ulong64_to_address(SymbolLocation.value)
        return self.trim_ulong64_to_address(SymbolLocation.value)

    def get_symbol(self, addr):
        """Get the symbol and displacement of an address

        :param addr: The address to lookup
        :type addr: int
        :rtype: str, int -- symbol name, displacement"""
        import pdb;pdb.set_trace()
        addr = self.expand_address_to_ulong64(addr)
        buffer_size = 1024
        buffer = (c_char * buffer_size)()
        name_size = ULONG()
        displacement = ULONG64()
        try:
            self.DebugSymbols.GetNameByOffset(addr, cast_to_char_p(buffer), buffer_size, byref(name_size), byref(displacement))
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

    def read_virtual_memory_uncached(self, addr, size):
        """BLABAL TODO FIXME
        """
        addr = self.resolve_symbol(addr)
        buffer = (c_char * size)()
        read = DWORD(0)

        self.DebugDataSpaces.ReadVirtualUncached(c_uint64(addr), buffer, size, byref(read))
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
            buffer = byref(data)
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

    def read_string(self, addr):
        """Todo handle string at end of mmap memory that does not stop with a \x00  + DOC"""
        base = addr
        res = []
        for i in itertools.count():
            x = self.read_virtual_memory(base + (i * 0x100), 0x100)
            if "\x00" in x:
                res.append(x.split("\x00", 1)[0])
                break
            res.append(x)
        return "".join(res)


    def read_wstring(self, addr):
        """TODO: DOC"""
        base = addr
        res = []
        for i in itertools.count():
            x = self.read_virtual_memory(base + (i * 0x100), 0x100)
            utf16_chars = ["".join(c) for c in zip(*[iter(x)] * 2)]
            if "\x00\x00" in utf16_chars:
                res.extend(utf16_chars[:utf16_chars.index("\x00\x00")])
                break
            res.extend(x)
        try:
            return "".join(res).decode('utf16')
        except ValueError:
            return "".join(res)

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
        """write a byte to virtual memory"""
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
            buffer = byref(data)
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

        self.DebugSymbols.GetTypeName(module, typeid, cast_to_char_p(buffer), buffer_size, byref(name_size))
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
    sh_id = 0xf0f0f0f0

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
            res = result_type.get(GetType, DWORD)(0x42424242)

        module, typeid = self.resolve_type(module, typeid)
        SymGetTypeInfo(self.sh_id, module, typeid, GetType, byref(res))# == 0:
        #    print(hex(res.value))
        #    raise WindowsError("SymGetTypeInfo_ctypes")
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

        res = res_struct()
        res.Count = nb_childs
        self.SymGetTypeInfo(module, typeid, TI_FINDCHILDREN, ires=res)
        return res

    @experimental
    def shell(self):
        while True:
            cmd = raw_input("(dbg) ")
            if not cmd:
                break
            self.execute(cmd)

class KernelDebugger32(object):
    DEBUG_DLL_PATH = os.path.join(realpath(__file__), r"..\..\..", "bin\\DBGDLL\\")
    ptr_size = 4

    def expand_address_to_ulong64(self, addr):
        """| Used to convert a symbol address to an ULONG64 requested by the API.
           | Problem is that in a 32bits kernel the kernel address are bit expended
           | :file:`nt` in 32bits kernel would not be :file:`0x8xxxxxxx` but :file:`0xffffffff8xxxxxxx`
           """
        if addr is None:
            return None
        # bit expansion
        return (0xFFFFFFFF00000000 * (addr >> 31)) | addr

    def trim_ulong64_to_address(self, addr):
        """ | Used to convert a symbol ULONG64 to the actual symbol.
            | Problem is that in a 32bits kernel the kernel address are bit expended
            | :file:`nt` in 32bits kernel would not be :file:`0x8xxxxxxx` but :file:`0xffffffff8xxxxxxx`
            """
        if addr is None:
            return None
        return addr & 0xffffffff


class KernelDebugger64(object):
    DEBUG_DLL_PATH = os.path.join(realpath(dirname(dirname(__file__))), "bin\\DBGDLL64\\")
    ptr_size = 8

    def expand_address_to_ulong64(self, addr):
        return addr

    def trim_ulong64_to_address(self, addr):
        return addr