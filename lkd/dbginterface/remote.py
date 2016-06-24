from base import BaseKernelDebugger, KernelDebugger64, KernelDebugger32

import windows
import ctypes
import windows
from windows.generated_def.winstructs import *
from lkd.dbgdef import *
from lkd.breakpoint import WinBreakpoint
from functools import partial
from lkd.dbgcom import IDebugRegisters, IDebugEventCallbacks, IDebugSystemObjects4
from lkd.dbgcom import *

# TEST DEBUG_VALUE #

#class _DEBUG_VALUE_UNION(ctypes.Union):
#        _fields_ = [
#        ("I8", UCHAR),
#        ("I16", USHORT),
#        ("I32", ULONG),
#        ("I64", ULONG64),
#        ("RawBytes", UCHAR * 24)
#    ]

class EDEBUG_VALUE(DEBUG_VALUE):
        VALUE_TRANSLATION_TABLE = {DEBUG_VALUE_INT8: "I8", DEBUG_VALUE_INT16: "I16",
            DEBUG_VALUE_INT32: "I32", DEBUG_VALUE_INT64: "I64"}

    #    _fields_ = [
    #    ("Value", _DEBUG_VALUE_UNION),
    #    ("TailOfRawBytes", ULONG),
    #    ("Type", ULONG),
    #]

        def get_value(self):
            if self.Type == 0:
                raise ValueError("DEBUG_VALUE at DEBUG_VALUE_INVALID")
            if self.Type not in self.VALUE_TRANSLATION_TABLE:
                # TODO: full _DEBUG_VALUE_UNION and implem other DEBUG_VALUE_XXX
                raise NotImplementedError("DEBUG_VALUE.Type == {0} (sorry)".format(self.Type))
            return getattr(self.u, self.VALUE_TRANSLATION_TABLE[self.Type])

        def set_value(self, new_value):
            if self.Type == 0:
                raise ValueError("DEBUG_VALUE at DEBUG_VALUE_INVALID")
            if self.Type not in self.VALUE_TRANSLATION_TABLE:
                # TODO: full _DEBUG_VALUE_UNION and implem other DEBUG_VALUE_XXX
                raise NotImplementedError("DEBUG_VALUE.Type == {0} (sorry)".format(self.Type))
            return setattr(self.u, self.VALUE_TRANSLATION_TABLE[self.Type], new_value)




# TODO keep the register_info list in the object
class TargetRegisters(IDebugRegisters):
    """This class suppose that the list of registers does not change for a given target"""

    def get_number_registers(self):
        res = ULONG()
        self.GetNumberRegisters(byref(res))
        return res.value

    def get_register_name(self, index):
        name_size = ULONG()
        self.GetDescription(index, None, 0, byref(name_size), None)
        bsize = name_size.value
        buffer = (c_char * bsize)()
        self.GetDescription(index, buffer, bsize, byref(name_size), None)
        return buffer[:name_size.value - 1]

    def list_registers(self):
        return [self.get_register_name(i) for i in range(self.get_number_registers())]

    keys = list_registers

    def get_register_value(self, index):
        res = EDEBUG_VALUE()
        #import pdb;pdb.set_trace()
        self.GetValue(index, byref(res))
        return res.get_value()

    def get_register_value_by_name(self, name):
        regs_name = self.list_registers()
        if name.lower() not in regs_name:
            raise ValueError("Unknown register <{0}>".format(name))
        return self.get_register_value(regs_name.index(name.lower()))

    __getitem__ = get_register_value_by_name


    def set_register_value(self, index, value):
        res = EDEBUG_VALUE()
        self.GetValue(index, byref(res))
        res.set_value(value)
        return self.SetValue(index, byref(res))

    def set_register_value_by_name(self, name, value):
        regs_name = self.list_registers()
        if name.lower() not in regs_name:
            raise ValueError("Unknown register <{0}>".format(name))
        return self.set_register_value(regs_name.index(name.lower()), value)

    __setitem__ = set_register_value_by_name

    def output(self):
        self.OutputRegisters(0, 0)

    dump = output

LAST_EVENT_VALUES = {
 0x00000001: ("DEBUG_EVENT_BREAKPOINT", DEBUG_LAST_EVENT_INFO_BREAKPOINT),
 0x00000002: ("DEBUG_EVENT_EXCEPTION", DEBUG_LAST_EVENT_INFO_EXCEPTION),
 0x00000004: ("DEBUG_EVENT_CREATE_THREAD", None),
 0x00000008: ("DEBUG_EVENT_EXIT_THREAD", DEBUG_LAST_EVENT_INFO_EXIT_THREAD),
 0x00000010: ("DEBUG_EVENT_CREATE_PROCESS", None),
 0x00000020: ("DEBUG_EVENT_EXIT_PROCESS", DEBUG_LAST_EVENT_INFO_EXIT_PROCESS),
 0x00000040: ("DEBUG_EVENT_LOAD_MODULE", DEBUG_LAST_EVENT_INFO_LOAD_MODULE),
 0x00000080: ("DEBUG_EVENT_UNLOAD_MODULE", DEBUG_LAST_EVENT_INFO_UNLOAD_MODULE),
 0x00000100: ("DEBUG_EVENT_SYSTEM_ERROR", DEBUG_LAST_EVENT_INFO_SYSTEM_ERROR),
 0x00000200: ("DEBUG_EVENT_SESSION_STATUS", None),
 0x00000400: ("DEBUG_EVENT_CHANGE_DEBUGGEE_STATE", None),
 0x00000800: ("DEBUG_EVENT_CHANGE_ENGINE_STATE", None),
 0x00001000: ("DEBUG_EVENT_CHANGE_SYMBOL_STATE", None),
}

class LastEvent(object):
    def __init__(self, type, process_id, thread_id, raw_extra_information, raw_description):
        self.type = type
        self.process_id = process_id
        self.thread_id = thread_id

        if type not in LAST_EVENT_VALUES:
            raise ValueError("Unknow LastEvent if type {0}".format(hex(type)))
        self.event_name, extra_info_type = LAST_EVENT_VALUES[type]
        self.extra_information = extra_info_type.from_buffer_copy(raw_extra_information)
        self.description = raw_description[:].strip("\x00")

    def __repr__(self):
        return """<LastEvent {0} ({1})>""".format(self.event_name, self.description)


class BaseStackFrame(DEBUG_STACK_FRAME):
    """A subclass asigned to one debugger should be created using
       assigned_to_debugger
    """
    # The subclasses assigned will have a dbg variable not None
    dbg = None

    @classmethod
    def assigned_to_debugger(cls, the_dbg):
        class StackFrame(cls):
            dbg = the_dbg
        return StackFrame

    @property
    def instruction_offset(self):
        return self.dbg.trim_ulong64_to_address(self.InstructionOffset)

    @property
    def return_offset(self):
        return self.dbg.trim_ulong64_to_address(self.ReturnOffset)

    @property
    def frame_offset(self):
        return self.dbg.trim_ulong64_to_address(self.FrameOffset)

    @property
    def stack_offset(self):
        return self.dbg.trim_ulong64_to_address(self.StackOffset)

    @property
    def func_table_entry(self):
        raise NotImplementedError("TODO")

    @property
    def params(self):
        return [self.dbg.trim_ulong64_to_address(x) for x in self.Params]

    @property
    def virtual(self):
        return self.Virtual

    @property
    def frame_number(self):
        return self.FrameNumber

    def __repr__(self):
        sym, disp = self.dbg.get_symbol(self.instruction_offset)
        addr = hex(self.instruction_offset).strip("L")
        if sym is None:
            return "<StackFrame {0}>".format(addr)
        return "<StackFrame {0} {1}+{2}>".format(addr, sym, hex(disp).strip("L"))


import time
import cProfile, pstats, StringIO

# https://msdn.microsoft.com/en-us/library/windows/hardware/ff550550%28v=vs.85%29.aspx
class DefaultEventCallback(COMImplementation):
    IMPLEMENT = IDebugEventCallbacks


    def __init__(self, dbg, **implem):
        super(DefaultEventCallback, self).__init__(**implem)
        self.debugger = dbg

    def GetInterestMask(self, selfcom, mask):
        mask.contents.value = DEBUG_EVENT_BREAKPOINT + DEBUG_EVENT_EXCEPTION + DEBUG_EVENT_CREATE_PROCESS + DEBUG_EVENT_LOAD_MODULE
        return 0

    def _get_breakpoint_from_com_ptr(self, bpcom):
        # Get a simple COM interface for the breakpoint
        basebp = WinBreakpoint(bpcom, self.debugger)
        # Get the real Python breakpoint object
        bp = self.debugger.breakpoints[basebp.id]
        return bp

    def _dispatch_to_breakpoint(self, bp):
        if not hasattr(bp, "trigger"):
            return DEBUG_STATUS_BREAK
        return bp.trigger()

    def Breakpoint(self, selfcom, bpcom):
        #pr = cProfile.Profile()
        #pr.enable()
        try:
            bp = self._get_breakpoint_from_com_ptr(bpcom)
        except KeyError as e:
            return DEBUG_STATUS_BREAK
        x = self._dispatch_to_breakpoint(bp)
        #end = time.time()
        #pr.disable()
        #s = StringIO.StringIO()
        #sortby = 'tottime'
        #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        #ps.print_stats()
        #print("BP HANDLING STAT")
        #print s.getvalue()
        #import pdb;pdb.set_trace()
        return x


# ... do something ...





    def Exception(self, *args):
        print("Exception")
        return DEBUG_STATUS_BREAK

    def CreateThread(self, *args):
        return 0

    def ExitThread(self, *args):
        return 0


    def CreateProcess(self, *args):
        print("CreateProcess")
        import pdb;pdb.set_trace()
        return 0

    ExitProcess = ExitThread
    LoadModule = ExitThread
    UnloadModule = ExitThread
    SystemError = ExitThread
    SessionStatus = ExitThread

    def ChangeDebuggeeState(self, selfcom, flags, argument):
        return 0

    def ChangeEngineState(self, selfcom, flags, argument):
        return 0

    def ChangeSymbolState(self, selfcom, flags, argument):
        return 0



class BaseRemoteDebugger(BaseKernelDebugger):
    if windows.current_process.bitness == 32:
        DEBUG_DLL_PATH = KernelDebugger32.DEBUG_DLL_PATH
    else:
        DEBUG_DLL_PATH = KernelDebugger64.DEBUG_DLL_PATH

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
        self.breakpoints = {}

    def _do_kernel_attach(self, str):
        return self.DebugClient.AttachKernel(DEBUG_ATTACH_KERNEL_CONNECTION, str)

    def _ask_other_interface(self):
        super(BaseRemoteDebugger, self)._ask_other_interface()
        DebugClient = self.DebugClient
        self.DebugRegisters = TargetRegisters(0)
        self.DebugSystemObjects = IDebugSystemObjects4(0)

        DebugClient.QueryInterface(self.DebugRegisters.IID, byref(self.DebugRegisters))
        DebugClient.QueryInterface(self.DebugSystemObjects.IID, byref(self.DebugSystemObjects))
        self.registers = self.DebugRegisters

    def is_pointer_64bit(self):
        return not self.DebugControl.IsPointer64Bit()

    def print_stack(self, number_frame=0x1fff, print_option=0x1fff):
        return self.DebugControl.OutputStackTrace(0, None, 0x1fff , print_option)

    def detach(self):
        self.DebugClient.EndSession(DEBUG_END_ACTIVE_DETACH)

    def get_execution_status(self):
        res = ULONG()
        self.DebugControl.GetExecutionStatus(byref(res))
        return res.value

    def set_execution_status(self, status):
        return self.DebugControl.SetExecutionStatus(status)

    def add_breakpoint(self, bp=None):
        if bp is None:
            bp = WinBreakpoint(debugger=self)
        if bp.is_bind_to_debugger:
            raise ValueError("Cannot bind a debugger to multiple debugger")
        bp.dbg = self
        bp.is_bind_to_debugger = True
        self.DebugControl.AddBreakpoint(DEBUG_BREAKPOINT_CODE, DEBUG_ANY_ID, byref(bp))
        self.breakpoints[bp.id] = bp
        return bp

    def remove_breakpoint(self, bp):
        id = bp.id
        self.DebugControl.RemoveBreakpoint(bp)
        self.breakpoints[id].deleted = True
        del self.breakpoints[id]
        return True

    def cont(self, flag=None):
        if flag is not None:
            self.set_execution_status(flag)
        # Clear user interrupt if any
        self.DebugControl.GetInterrupt()
        x = self.DebugControl.WaitForEvent(0, 0xffffffff)
        print("WaitForEvent -> {0}".format(x))
        return x

    go =  lambda self: self.cont(flag=DEBUG_STATUS_GO)
    step =  lambda self: self.cont(flag=DEBUG_STATUS_STEP_INTO)
    step_over =  lambda self: self.cont(flag=DEBUG_STATUS_STEP_OVER)

    def get_register_index(self, name):
        res = ULONG()
        self.DebugRegisters.GetIndexByName(name, byref(res))
        return res.value

    def get_stack_trace(self):
        for i in range(1, 10):
            array_size = i * 100
            res = ULONG()
            array = (BaseStackFrame.assigned_to_debugger(self) * (array_size))()

            self.DebugControl.GetStackTrace(0, 0, 0, array, array_size, byref(res))
            if res.value < array_size:
                #for i in range(res.value):
                    # Assign the debugger to each one
                return array[0: res.value]

    backtrace = property(get_stack_trace)

    def get_last_event_information(self):
        extra_information_used = ULONG()
        description_used = ULONG()
        type = ULONG()
        ProcessId = ULONG()
        ThreadId = ULONG()

        self.DebugControl.GetLastEventInformation(byref(type), byref(ProcessId), byref(ThreadId), None, 0, byref(extra_information_used), None, 0, byref(description_used))
        extra_information = (ctypes.c_byte * extra_information_used.value)()
        description = (ctypes.c_char * description_used.value)()
        self.DebugControl.GetLastEventInformation(byref(type), byref(ProcessId), byref(ThreadId), extra_information, extra_information_used.value, byref(extra_information_used), description, description_used.value, byref(description_used))
        return LastEvent(type.value, ProcessId.value, ThreadId.value, extra_information, description)

    last_event = property(get_last_event_information)

    def current_thread(self):
        res = ULONG64()
        self.DebugSystemObjects.GetCurrentThreadDataOffset(byref(res))
        v = res.value
        return self.get_type("nt", "_ETHREAD")(self.trim_ulong64_to_address(v))

    def current_process(self):
        res = ULONG64()
        self.DebugSystemObjects.GetCurrentProcessDataOffset(byref(res))
        v = res.value
        return self.get_type("nt", "_EPROCESS")(self.trim_ulong64_to_address(v))

    def current_process_data(self):
        res = ULONG64()
        self.DebugSystemObjects.GetCurrentProcessDataOffset(byref(res))
        return res.value

    def current_process_name(self):
        size = 0x200
        buffer = ctypes.c_buffer(0x200)
        name_size = ULONG()
        self.DebugSystemObjects.GetCurrentProcessExecutableName(buffer, size, name_size)
        return buffer[:name_size.value]

    def current_peb(self):
        # TODO: TYPE
        res = ULONG64()
        self.DebugSystemObjects.GetCurrentProcessPeb(byref(res))
        return res.value


    # Filters stuff :)

    def get_event_filter_text(self, i):
        size = 1000
        buffer = (c_char * size)()
        textsize = ULONG()
        self.DebugControl.GetEventFilterText(i, buffer, size, byref(textsize))
        return buffer[:textsize.value]

    def get_specific_filter_parameters(self, start, count=1):
        if count == 1:
            res_val = DEBUG_SPECIFIC_FILTER_PARAMETERS()
            res = byref(res_val)
            ret = lambda : res_val
        else:
            res = (DEBUG_SPECIFIC_FILTER_PARAMETERS * count)()
            ret = lambda : res[:]

        self.DebugControl.GetSpecificFilterParameters(start, count, res)
        return ret()

    def get_exception_filter_parameters(self, start, count=1):
        if count == 1:
            res_val = DEBUG_EXCEPTION_FILTER_PARAMETERS()
            res = byref(res_val)
            ret = lambda : res_val
        else:
            res = (DEBUG_EXCEPTION_FILTER_PARAMETERS * count)()
            ret = lambda : res[:]

        self.DebugControl.GetExceptionFilterParameters(count, None, start, res)
        return ret()

    def set_exception_filter_parameters(self, i, value):
        return self.DebugControl.SetExceptionFilterParameters(i, byref(value))

    def get_number_event_filters(self):
        specific_event = ULONG()
        specific_execpt = ULONG()
        arbitrary_except = ULONG()
        self.DebugControl.GetNumberEventFilters(byref(specific_event), byref(specific_execpt), byref(arbitrary_except))
        return specific_event.value, specific_execpt.value, arbitrary_except.value

    def set_specific_filter_parameters(self, start, params, count=None):
        if count is None:
            if isinstance(params, ctypes.Array):
                count = params._length_
            else:
                count = 1
        return self.DebugControl.SetSpecificFilterParameters(start, count, byref(params))

    def set_exception_filter_parameters(self, params, count=None):
        if count is None:
            if isinstance(params, ctypes.Array):
                count = params._length_
            else:
                count = 1
        return self.DebugControl.SetExceptionFilterParameters(count, byref(params))



class RemoteKernelDebugger32(BaseRemoteDebugger, KernelDebugger32):
    read_ptr = BaseRemoteDebugger.read_dword
    read_ptr_p = BaseRemoteDebugger.read_dword_p
    write_ptr = BaseRemoteDebugger.write_dword
    write_ptr_p = BaseRemoteDebugger.write_dword_p

class RemoteKernelDebugger64(BaseRemoteDebugger, KernelDebugger64):
    read_ptr = BaseRemoteDebugger.read_qword
    read_ptr_p = BaseRemoteDebugger.read_qword_p
    write_ptr = BaseRemoteDebugger.write_qword
    write_ptr_p = BaseRemoteDebugger.write_qword_p

def RemoteDebugger(connection_string):
    rem = BaseRemoteDebugger(connection_string)
    print(rem.is_pointer_64bit())
    # Adapt the debugger class to the target bitness
    if rem.is_pointer_64bit():
        rem.__class__ = RemoteKernelDebugger64
    else:
        rem.__class__ = RemoteKernelDebugger32

    event_callback = DefaultEventCallback(rem)
    rem.DebugClient.SetEventCallbacks(event_callback)
    rem.event_callback = event_callback
    return rem





