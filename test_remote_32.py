from dbginterface import RemoteDebugger
import code
from simple_com import COMInterface, IDebugEventCallbacks
from breakpoint import WinBreakpoint
import functools


DEBUG_STATUS_NO_CHANGE            = 0
DEBUG_STATUS_GO                   = 1
DEBUG_STATUS_GO_HANDLED           = 2
DEBUG_STATUS_GO_NOT_HANDLED       = 3
DEBUG_STATUS_STEP_OVER            = 4
DEBUG_STATUS_STEP_INTO            = 5
DEBUG_STATUS_BREAK                = 6
DEBUG_STATUS_NO_DEBUGGEE          = 7
DEBUG_STATUS_STEP_BRANCH          = 8
DEBUG_STATUS_IGNORE_EVENT         = 9
DEBUG_STATUS_RESTART_REQUESTED    = 10
DEBUG_STATUS_REVERSE_GO           = 11
DEBUG_STATUS_REVERSE_STEP_BRANCH  = 12
DEBUG_STATUS_REVERSE_STEP_OVER    = 13
DEBUG_STATUS_REVERSE_STEP_INTO    = 14

#define DEBUG_STATUS_MASK                0xf


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
        if filename.endswith(".txt"):
            print("OPPENING TXT FILE")
            return DEBUG_STATUS_BREAK
        return DEBUG_STATUS_GO



connect_string = r"com:pipe,port=\\.\pipe\ware_windows_8,resets=0,reconnect"
print(connect_string)
rdbg = RemoteDebugger(connect_string)


DEBUG_BREAKPOINT_ENABLED  = 0x00000004

DEBUG_BREAKPOINT_GO_ONLY = 0x00000001
DEBUG_BREAKPOINT_ADDER_ONLY = 0x00000008

bp = MyBreakPoint("SUCE")
rdbg.add_breakpoint(bp)

bp.set_offset("nt!NtCreateFile")
bp.enable()

bp.AddFlags(DEBUG_BREAKPOINT_GO_ONLY + DEBUG_BREAKPOINT_ADDER_ONLY)
print(bp)

rdbg.execute("dd nt")


#addr = rdbg.get_symbol_offset("nt!NtCreateFile")
#bp.set_offset("nt!NtCreateFile")

bp.set_command("u eip")
bp.enable()
print("Setup breakpoint at nt!NtCreateFile")

rdbg.execute("bl *")
print("CONTINUE")


print("Status = {0}".format(hex(rdbg.get_execution_status())))

rdbg.cont()

print("Status = {0}".format(hex(rdbg.get_execution_status())))

rdbg.cont()


print("Status = {0}".format(hex(rdbg.get_execution_status())))


print("CONTINUE END <3")

rdbg.execute("dd nt")

def next_bp():
    rdbg.set_execution_status(DEBUG_STATUS_STEP_INTO)
    rdbg.cont()
    rdbg.set_execution_status(DEBUG_STATUS_GO)
    rdbg.cont()

reg = rdbg.registers

print("Testing event callaback")

class MyEventCallback(IDebugEventCallbacks):
    def __init__(self, dbg, **implem):
        super(MyEventCallback, self).__init__(**implem)
        self.debugger = dbg

    def GetInterestMask(self, selfcom, mask):
        print("GetInterestMask CALLED")
        mask.contents.value = 1
        return 0

    def Breakpoint(self, selfcom, bpcom):
        print("BREAKPOINT")
        # Get a simple COM interface for the breakpoint
        basebp = WinBreakpoint(bpcom, self.debugger)
        # Get the real Python breakpoint object

        print(self.debugger.execute("bl *"))
        try:
            bp = self.debugger.breakpoints[basebp.id]
        except:
            print("FAIL")
            import pdb;pdb.set_trace()
        bp = self.debugger.breakpoints[basebp.id]
        if not hasattr(bp, "trigger"):
            return DEBUG_STATUS_BREAK
        return bp.trigger()

    def Exception(self, *args):
        return 0
        raise NotImplementedError()

    CreateThread = 0x11223344
    ExitThread = 0x11223345
    CreateProcess = 0x11223346
    ExitProcess = 0x11223347
    LoadModule = 0x11223348
    UnloadModule = 0x11223349
    SystemError = 0x1122334a
    SessionStatus = 0x1122334b
    ChangeDebuggeeState = Exception
    ChangeSymbolState = Exception

    def ChangeEngineState(self, *args):
        print("STATE")
        return 0




#def GetInterestMask(*args):
#    print("INTO GetInterestMask")
#    print(args)
#    print(args[0])
#    print(args[1])
#    print(hex(args[1].contents.value))
#    args[1].contents.value = 1
#    print("DONE")
#    return 0
#
#def bp_callback(*args):
#    print("BREAK EVENT CALL BACK<3")
#    print(args)
#    bp = WinBreakpoint(args[1], rdbg)
#    print(bp)
#    print(bp.id)
#    bp = rdbg.breakpoints[bp.id]
#    print(bp)
#    return bp.trigger()
#
#nop = lambda *args: 0
#
#callback_implem = {"GetInterestMask" : GetInterestMask, "Breakpoint" : bp_callback, "Exception": nop}
#
#import ctypes
#
#callback_object = IDebugEventCallbacks.create_vtable(**callback_implem)
#
#v = ctypes.addressof(callback_object)
#t = ctypes.pointer(callback_object)
#r  = ctypes.addressof(t)

b = MyEventCallback(rdbg)




#rdbg.DebugClient.SetEventCallbacks(callback_object)

rdbg.DebugClient.SetEventCallbacks(b)

next_bp()

print("BYE")







#bp.disable()
#rdbg.cont()


#rdbg.detach()