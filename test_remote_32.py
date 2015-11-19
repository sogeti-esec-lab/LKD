from dbginterface import RemoteDebugger
import code
from simple_com import COMInterface, IDebugEventCallbacks
from breakpoint import WinBreakpoint
import functools
from dbgdef import *


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
        #print("Breakpoint have been triggered <{0} | {1}>".format(self.s, filename))
        #if filename.endswith(".exe"):
        #    print("OPPENING TXT FILE")
        return DEBUG_STATUS_BREAK
        #return DEBUG_STATUS_GO



connect_string = r"com:pipe,port=\\.\pipe\ware_windows_8,resets=0,reconnect"
print(connect_string)
rdbg = RemoteDebugger(connect_string)


bp = MyBreakPoint("SUCE")
rdbg.add_breakpoint(bp)

bp.set_offset("nt!NtCreateFile")
bp.enable()

bp.AddFlags(DEBUG_BREAKPOINT_GO_ONLY + DEBUG_BREAKPOINT_ADDER_ONLY)

print(bp)



#addr = rdbg.get_symbol_offset("nt!NtCreateFile")
#bp.set_offset("nt!NtCreateFile")

#bp.set_command("u eip")

bp.enable()
print("Setup breakpoint at nt!NtCreateFile")

print("CONTINUE")

print("Status = {0}".format(hex(rdbg.get_execution_status())))
rdbg.cont()
print("Status = {0}".format(hex(rdbg.get_execution_status())))
rdbg.cont()
print("Status = {0}".format(hex(rdbg.get_execution_status())))


def next_bp():
    rdbg.set_execution_status(DEBUG_STATUS_STEP_INTO)
    rdbg.cont()
    rdbg.set_execution_status(DEBUG_STATUS_GO)
    rdbg.cont()

reg = rdbg.registers

#next_bp()

print("BYE")


x = rdbg.read_ptr(rdbg.registers['esp'] + 0xc)

t = rdbg.get_type("nt", '_OBJECT_ATTRIBUTES')

z = t(x)

p = rdbg.current_process()

peb = rdbg.current_peb()

import windows

rdbg.read_memory = rdbg.read_virtual_memory
peb = windows.winobject.RemotePEB(peb, rdbg)

rdbg.bitness = 32
reload(windows.pe_parse); v = windows.pe_parse.PEFile(0x8e5d8000, target=rdbg)

import pdb
import sys


print(v.sections)

nto = windows.pe_parse.PEFile(rdbg.get_symbol_offset("nt"), target=rdbg)





#bp.disable()
#rdbg.cont()


#rdbg.detach()