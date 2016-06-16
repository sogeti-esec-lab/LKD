from dbginterface import RemoteDebugger
from dbginterface.remote import DefaultEventCallback
import code
from simple_com import COMInterface, IDebugEventCallbacks
from breakpoint import WinBreakpoint
import functools
from dbgdef import *

import ctypes


def get_file():
    return rdbg.execute("du  poi (poi( poi(esp + 0xc) + 8) + 4)")

def get_fileaddr():
    x = rdbg.read_ptr(rdbg.registers['esp'] + 0xc)
    x = rdbg.read_ptr(x + 0x8)
    x = rdbg.read_ptr(x + 0x4)
    #print(hex(x))
    return rdbg.read_wstring(x)

class MyBreakPoint(WinBreakpoint):

    def __init__(self, s):
        super(MyBreakPoint, self).__init__()
        self.s = s
        self.ok = 0

    def trigger(self):
        filename = get_fileaddr()
        print("Breakpoint have been triggered <{0} | {1}>".format(self.s, filename))
        if filename.endswith(".exe"):
            print("OPPENING TXT FILE")
            return DEBUG_STATUS_BREAK
        return DEBUG_STATUS_GO



connect_string = r"com:pipe,port=\\.\pipe\ware_windows_8,resets=0,reconnect"
print(connect_string)
rdbg = RemoteDebugger(connect_string)

## BP STUFF ##
#bp = MyBreakPoint("SUCE")
#rdbg.add_breakpoint(bp)
#
#bp.set_offset("nt!NtCreateFile")
#bp.enable()
#
#bp.AddFlags(DEBUG_BREAKPOINT_GO_ONLY + DEBUG_BREAKPOINT_ADDER_ONLY)
#
#print(bp)

@ctypes.WINFUNCTYPE(ctypes.c_uint, ctypes.c_uint)
def my_stopper(x):
    print("STOPPER CTRL+C")
    rdbg.DebugControl.SetInterrupt(DEBUG_INTERRUPT_ACTIVE)
    print("STOPPER EXIT")
    return True

import windows
windows.winproxy.SetConsoleCtrlHandler(my_stopper, True)


#addr = rdbg.get_symbol_offset("nt!NtCreateFile")
#bp.set_offset("nt!NtCreateFile")

#bp.set_command("u eip")

#bp.enable()
#print("Setup breakpoint at nt!NtCreateFile")
#
#print("CONTINUE")
#
#print("Status = {0}".format(hex(rdbg.get_execution_status())))
#rdbg.cont()
#print("Status = {0}".format(hex(rdbg.get_execution_status())))
#rdbg.cont()
#print("Status = {0}".format(hex(rdbg.get_execution_status())))


def next_bp():
    rdbg.set_execution_status(DEBUG_STATUS_STEP_INTO)
    rdbg.cont()
    rdbg.set_execution_status(DEBUG_STATUS_GO)
    rdbg.cont()

reg = rdbg.registers

#next_bp()

print("BYE")

from windows.generated_def.winstructs import *

def disas(addr):
    size = 1000
    buffer = (ctypes.c_char * size)()
    res_size = ULONG()
    end = ULONG64()
    rdbg.DebugControl.Disassemble(addr, 0, buffer, size, byref(res_size), byref(end))
    return (buffer[:res_size.value].strip("\x00"), end.value)



suce = [0]

class MyEventCallback(DefaultEventCallback):

    def __init__(self, dbg, msg, **implem):
        super(MyEventCallback, self).__init__(dbg)
        self.msg = msg

    def Exception(self, *args):
        if rdbg.current_process().ImageFileName.as_str() == "python.exe":
            print("Python break <returning {0}".format(suce[0]))
            x = suce[0]
            suce[0] = x + 1
            return DEBUG_STATUS_GO_NOT_HANDLED
        print("Exception in {0}".format(rdbg.current_process().ImageFileName.as_str()))
        return DEBUG_STATUS_BREAK



rdbg.DebugClient.SetEventCallbacks(MyEventCallback(rdbg, "SUCE<3"))

### SETUP FILTER IGNORE

class Filters(object):
    def __init__(self, dbg):
        self.dbg = dbg

    def get_filter_text(self, filternb):
        return self.dbg.get_event_filter_text(filternb).strip("\x00")

    def get_all_filter_text(self):
        event, excep, _ = self.dbg.get_number_event_filters()
        return [self.get_filter_text(i) for i in range(event + excep)]

    def get_item_number(self, i):
        event, excep, _ = self.dbg.get_number_event_filters()
        if 0 <= i < event:
            return self.dbg.get_specific_filter_parameters(i)

        if event <= i < event + excep:
            x = self.dbg.get_exception_filter_parameters(i)
            x._exception_number = (i, x.ExceptionCode)
            return x

        raise NotImplementedError("Sorry arbitrary_except not implemented")

    def get_item_by_name(self, name):
        pos = self.get_all_filter_text().index(name)
        return self.get_item_number(pos)


    def setup_by_name(self, name, value):
        pos = self.get_all_filter_text().index(name)
        return self.setup_by_number(pos, value)


    def setup_by_number(self, i, item):
        if isinstance(item, DEBUG_EXCEPTION_FILTER_PARAMETERS):
            if hasattr(item, "_exception_number"):
                orig_i, orig_excep_code = item._exception_number
                if orig_excep_code == item.ExceptionCode and orig_i != i:
                    # TODO: better ? documents ?
                    raise ValueError("ExceptionCode doest not match the exception to set")
            return self.dbg.set_exception_filter_parameters(item)
        elif isinstance(item, DEBUG_SPECIFIC_FILTER_PARAMETERS):
            return self.dbg.set_specific_filter_parameters(i, item)
        else:
            raise ValueError("unexpected setup filter value {0}".format(item))

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.get_item_by_name(key)
        return self.get_item_number(key)

    keys = get_all_filter_text

    def __setitem__(self, key, value):
        if isinstance(key, str):
            return self.setup_by_name(key, value)
        return self.setup_by_number(key, value)









#x = rdbg.tst2(14)
#x.ExecutionOption = 3
#rdbg.SetExceptionFilterParameters(1, x)

f = Filters(rdbg)



# x = rdbg.read_ptr(rdbg.registers['esp'] + 0xc)
# t = rdbg.get_type("nt", '_OBJECT_ATTRIBUTES')
# z = t(x)
# p = rdbg.current_process()
# peb = rdbg.current_peb()
#
# import windows
#
# rdbg.read_memory = rdbg.read_virtual_memory
# peb = windows.winobject.RemotePEB(peb, rdbg)
#
# rdbg.bitness = 32
# reload(windows.pe_parse); v = windows.pe_parse.PEFile(0x8e5d8000, target=rdbg)
#
# import pdb
# import sys
#
#
# print(v.sections)
#
# nto = windows.pe_parse.PEFile(rdbg.get_symbol_offset("nt"), target=rdbg)



#bp.disable()
#rdbg.cont()


#rdbg.detach()