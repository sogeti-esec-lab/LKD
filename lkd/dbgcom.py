from windows.generated_def.winstructs import *
from windows.generated_def.interfaces import *

class IDebugAdvanced(COMInterface):
    IID = generate_IID(0xF2DF5F53, 0x071F, 0x47BD, 0x9D, 0xE6, 0x57, 0x34, 0xC3, 0xFE, 0xD6, 0x89, name="IDebugAdvanced", strid="F2DF5F53-071F-47BD-9DE6-5734C3FED689")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetThreadContext -> Context:PVOID, ContextSize:ULONG
 "GetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(3, "GetThreadContext"),
 #SetThreadContext -> Context:PVOID, ContextSize:ULONG
 "SetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(4, "SetThreadContext"),
    }


class IDebugAdvanced2(COMInterface):
    IID = generate_IID(0x716D14C9, 0x119B, 0x4BA5, 0xAF, 0x1F, 0x08, 0x90, 0xE6, 0x72, 0x41, 0x6A, name="IDebugAdvanced2", strid="716D14C9-119B-4BA5-AF1F-0890E672416A")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetThreadContext -> Context:PVOID, ContextSize:ULONG
 "GetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(3, "GetThreadContext"),
 #SetThreadContext -> Context:PVOID, ContextSize:ULONG
 "SetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(4, "SetThreadContext"),
 #Request -> Request:ULONG, InBuffer:PVOID, InBufferSize:ULONG, OutBuffer:PVOID, OutBufferSize:ULONG, OutSize:PULONG
 "Request": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PVOID, ULONG, PULONG)(5, "Request"),
 #GetSourceFileInformation -> Which:ULONG, SourceFile:PSTR, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetSourceFileInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG64, ULONG, PVOID, ULONG, PULONG)(6, "GetSourceFileInformation"),
 #FindSourceFileAndToken -> StartElement:ULONG, ModAddr:ULONG64, File:PCSTR, Flags:ULONG, FileToken:PVOID, FileTokenSize:ULONG, FoundElement:PULONG, Buffer:PSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFileAndToken": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCSTR, ULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(7, "FindSourceFileAndToken"),
 #GetSymbolInformation -> Which:ULONG, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG, StringBuffer:PSTR, StringBufferSize:ULONG, StringSize:PULONG
 "GetSymbolInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(8, "GetSymbolInformation"),
 #GetSystemObjectInformation -> Which:ULONG, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetSystemObjectInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PVOID, ULONG, PULONG)(9, "GetSystemObjectInformation"),
    }


class IDebugAdvanced3(COMInterface):
    IID = generate_IID(0xCBA4ABB4, 0x84C4, 0x444D, 0x87, 0xCA, 0xA0, 0x4E, 0x13, 0x28, 0x67, 0x39, name="IDebugAdvanced3", strid="CBA4ABB4-84C4-444D-87CA-A04E13286739")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetThreadContext -> Context:PVOID, ContextSize:ULONG
 "GetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(3, "GetThreadContext"),
 #SetThreadContext -> Context:PVOID, ContextSize:ULONG
 "SetThreadContext": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(4, "SetThreadContext"),
 #Request -> Request:ULONG, InBuffer:PVOID, InBufferSize:ULONG, OutBuffer:PVOID, OutBufferSize:ULONG, OutSize:PULONG
 "Request": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PVOID, ULONG, PULONG)(5, "Request"),
 #GetSourceFileInformation -> Which:ULONG, SourceFile:PSTR, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetSourceFileInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG64, ULONG, PVOID, ULONG, PULONG)(6, "GetSourceFileInformation"),
 #FindSourceFileAndToken -> StartElement:ULONG, ModAddr:ULONG64, File:PCSTR, Flags:ULONG, FileToken:PVOID, FileTokenSize:ULONG, FoundElement:PULONG, Buffer:PSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFileAndToken": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCSTR, ULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(7, "FindSourceFileAndToken"),
 #GetSymbolInformation -> Which:ULONG, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG, StringBuffer:PSTR, StringBufferSize:ULONG, StringSize:PULONG
 "GetSymbolInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(8, "GetSymbolInformation"),
 #GetSystemObjectInformation -> Which:ULONG, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetSystemObjectInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PVOID, ULONG, PULONG)(9, "GetSystemObjectInformation"),
 #GetSourceFileInformationWide -> Which:ULONG, SourceFile:PWSTR, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetSourceFileInformationWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG64, ULONG, PVOID, ULONG, PULONG)(10, "GetSourceFileInformationWide"),
 #FindSourceFileAndTokenWide -> StartElement:ULONG, ModAddr:ULONG64, File:PCWSTR, Flags:ULONG, FileToken:PVOID, FileTokenSize:ULONG, FoundElement:PULONG, Buffer:PWSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFileAndTokenWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCWSTR, ULONG, PVOID, ULONG, PULONG, PWSTR, ULONG, PULONG)(11, "FindSourceFileAndTokenWide"),
 #GetSymbolInformationWide -> Which:ULONG, Arg64:ULONG64, Arg32:ULONG, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG, StringBuffer:PWSTR, StringBufferSize:ULONG, StringSize:PULONG
 "GetSymbolInformationWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PVOID, ULONG, PULONG, PWSTR, ULONG, PULONG)(12, "GetSymbolInformationWide"),
    }


class IDebugBreakpoint(COMInterface):
    IID = generate_IID(0x5BD9D474, 0x5975, 0x423A, 0xB8, 0x8B, 0x65, 0xA8, 0xE7, 0x11, 0x0E, 0x65, name="IDebugBreakpoint", strid="5BD9D474-5975-423A-B88B-65A8E7110E65")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetId -> Id:PULONG
 "GetId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetId"),
 #GetType -> BreakType:PULONG, ProcType:PULONG
 "GetType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(4, "GetType"),
 #GetAdder -> Adder:*PDEBUG_CLIENT
 "GetAdder": ctypes.WINFUNCTYPE(HRESULT, PVOID)(5, "GetAdder"),
 #GetFlags -> Flags:PULONG
 "GetFlags": ctypes.WINFUNCTYPE(HRESULT, PULONG)(6, "GetFlags"),
 #AddFlags -> Flags:ULONG
 "AddFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(7, "AddFlags"),
 #RemoveFlags -> Flags:ULONG
 "RemoveFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "RemoveFlags"),
 #SetFlags -> Flags:ULONG
 "SetFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(9, "SetFlags"),
 #GetOffset -> Offset:PULONG64
 "GetOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(10, "GetOffset"),
 #SetOffset -> Offset:ULONG64
 "SetOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(11, "SetOffset"),
 #GetDataParameters -> Size:PULONG, AccessType:PULONG
 "GetDataParameters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(12, "GetDataParameters"),
 #SetDataParameters -> Size:ULONG, AccessType:ULONG
 "SetDataParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(13, "SetDataParameters"),
 #GetPassCount -> Count:PULONG
 "GetPassCount": ctypes.WINFUNCTYPE(HRESULT, PULONG)(14, "GetPassCount"),
 #SetPassCount -> Count:ULONG
 "SetPassCount": ctypes.WINFUNCTYPE(HRESULT, ULONG)(15, "SetPassCount"),
 #GetCurrentPassCount -> Count:PULONG
 "GetCurrentPassCount": ctypes.WINFUNCTYPE(HRESULT, PULONG)(16, "GetCurrentPassCount"),
 #GetMatchThreadId -> Id:PULONG
 "GetMatchThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetMatchThreadId"),
 #SetMatchThreadId -> Thread:ULONG
 "SetMatchThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetMatchThreadId"),
 #GetCommand -> Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetCommand": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(19, "GetCommand"),
 #SetCommand -> Command:PCSTR
 "SetCommand": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(20, "SetCommand"),
 #GetOffsetExpression -> Buffer:PSTR, BufferSize:ULONG, ExpressionSize:PULONG
 "GetOffsetExpression": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(21, "GetOffsetExpression"),
 #SetOffsetExpression -> Expression:PCSTR
 "SetOffsetExpression": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "SetOffsetExpression"),
 #GetParameters -> Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetParameters": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_BREAKPOINT_PARAMETERS)(23, "GetParameters"),
    }


class IDebugBreakpoint2(COMInterface):
    IID = generate_IID(0x1B278D20, 0x79F2, 0x426E, 0xA3, 0xF9, 0xC1, 0xDD, 0xF3, 0x75, 0xD4, 0x8E, name="IDebugBreakpoint2", strid="1B278D20-79F2-426E-A3F9-C1DDF375D48E")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetId -> Id:PULONG
 "GetId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetId"),
 #GetType -> BreakType:PULONG, ProcType:PULONG
 "GetType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(4, "GetType"),
 #GetAdder -> Adder:*PDEBUG_CLIENT
 "GetAdder": ctypes.WINFUNCTYPE(HRESULT, PVOID)(5, "GetAdder"),
 #GetFlags -> Flags:PULONG
 "GetFlags": ctypes.WINFUNCTYPE(HRESULT, PULONG)(6, "GetFlags"),
 #AddFlags -> Flags:ULONG
 "AddFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(7, "AddFlags"),
 #RemoveFlags -> Flags:ULONG
 "RemoveFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "RemoveFlags"),
 #SetFlags -> Flags:ULONG
 "SetFlags": ctypes.WINFUNCTYPE(HRESULT, ULONG)(9, "SetFlags"),
 #GetOffset -> Offset:PULONG64
 "GetOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(10, "GetOffset"),
 #SetOffset -> Offset:ULONG64
 "SetOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(11, "SetOffset"),
 #GetDataParameters -> Size:PULONG, AccessType:PULONG
 "GetDataParameters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(12, "GetDataParameters"),
 #SetDataParameters -> Size:ULONG, AccessType:ULONG
 "SetDataParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(13, "SetDataParameters"),
 #GetPassCount -> Count:PULONG
 "GetPassCount": ctypes.WINFUNCTYPE(HRESULT, PULONG)(14, "GetPassCount"),
 #SetPassCount -> Count:ULONG
 "SetPassCount": ctypes.WINFUNCTYPE(HRESULT, ULONG)(15, "SetPassCount"),
 #GetCurrentPassCount -> Count:PULONG
 "GetCurrentPassCount": ctypes.WINFUNCTYPE(HRESULT, PULONG)(16, "GetCurrentPassCount"),
 #GetMatchThreadId -> Id:PULONG
 "GetMatchThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetMatchThreadId"),
 #SetMatchThreadId -> Thread:ULONG
 "SetMatchThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetMatchThreadId"),
 #GetCommand -> Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetCommand": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(19, "GetCommand"),
 #SetCommand -> Command:PCSTR
 "SetCommand": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(20, "SetCommand"),
 #GetOffsetExpression -> Buffer:PSTR, BufferSize:ULONG, ExpressionSize:PULONG
 "GetOffsetExpression": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(21, "GetOffsetExpression"),
 #SetOffsetExpression -> Expression:PCSTR
 "SetOffsetExpression": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "SetOffsetExpression"),
 #GetParameters -> Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetParameters": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_BREAKPOINT_PARAMETERS)(23, "GetParameters"),
 #GetCommandWide -> Buffer:PWSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetCommandWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(24, "GetCommandWide"),
 #SetCommandWide -> Command:PCWSTR
 "SetCommandWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(25, "SetCommandWide"),
 #GetOffsetExpressionWide -> Buffer:PWSTR, BufferSize:ULONG, ExpressionSize:PULONG
 "GetOffsetExpressionWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(26, "GetOffsetExpressionWide"),
 #SetOffsetExpressionWide -> Expression:PCWSTR
 "SetOffsetExpressionWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(27, "SetOffsetExpressionWide"),
    }


class IDebugClient(COMInterface):
    IID = generate_IID(0x27FE5639, 0x8407, 0x4F47, 0x83, 0x64, 0xEE, 0x11, 0x8F, 0xB0, 0x8A, 0xC8, name="IDebugClient", strid="27FE5639-8407-4F47-8364-EE118FB08AC8")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #AttachKernel -> Flags:ULONG, ConnectOptions:PCSTR
 "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "AttachKernel"),
 #GetKernelConnectionOptions -> Buffer:PSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(4, "GetKernelConnectionOptions"),
 #SetKernelConnectionOptions -> Options:PCSTR
 "SetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "SetKernelConnectionOptions"),
 #StartProcessServer -> Flags:ULONG, Options:PCSTR, Reserved:PVOID
 "StartProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PVOID)(6, "StartProcessServer"),
 #ConnectProcessServer -> RemoteOptions:PCSTR, Server:PULONG64
 "ConnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(7, "ConnectProcessServer"),
 #DisconnectProcessServer -> Server:ULONG64
 "DisconnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(8, "DisconnectProcessServer"),
 #GetRunningProcessSystemIds -> Server:ULONG64, Ids:PULONG, Count:ULONG, ActualCount:PULONG
 "GetRunningProcessSystemIds": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, ULONG, PULONG)(9, "GetRunningProcessSystemIds"),
 #GetRunningProcessSystemIdByExecutableName -> Server:ULONG64, ExeName:PCSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, ULONG, PULONG)(10, "GetRunningProcessSystemIdByExecutableName"),
 #GetRunningProcessDescription -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(11, "GetRunningProcessDescription"),
 #AttachProcess -> Server:ULONG64, ProcessId:ULONG, AttachFlags:ULONG
 "AttachProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG)(12, "AttachProcess"),
 #CreateProcess -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG)(13, "CreateProcess"),
 #CreateProcessAndAttach -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, ULONG, ULONG)(14, "CreateProcessAndAttach"),
 #GetProcessOptions -> Options:PULONG
 "GetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(15, "GetProcessOptions"),
 #AddProcessOptions -> Options:ULONG
 "AddProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(16, "AddProcessOptions"),
 #RemoveProcessOptions -> Options:ULONG
 "RemoveProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(17, "RemoveProcessOptions"),
 #SetProcessOptions -> Options:ULONG
 "SetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetProcessOptions"),
 #OpenDumpFile -> DumpFile:PCSTR
 "OpenDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(19, "OpenDumpFile"),
 #WriteDumpFile -> DumpFile:PCSTR, Qualifier:ULONG
 "WriteDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(20, "WriteDumpFile"),
 #ConnectSession -> Flags:ULONG, HistoryLimit:ULONG
 "ConnectSession": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "ConnectSession"),
 #StartServer -> Options:PCSTR
 "StartServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "StartServer"),
 #OutputServers -> OutputControl:ULONG, Machine:PCSTR, Flags:ULONG
 "OutputServers": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(23, "OutputServers"),
 #TerminateProcesses -> 
 "TerminateProcesses": ctypes.WINFUNCTYPE(HRESULT)(24, "TerminateProcesses"),
 #DetachProcesses -> 
 "DetachProcesses": ctypes.WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
 #EndSession -> Flags:ULONG
 "EndSession": ctypes.WINFUNCTYPE(HRESULT, ULONG)(26, "EndSession"),
 #GetExitCode -> Code:PULONG
 "GetExitCode": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetExitCode"),
 #DispatchCallbacks -> Timeout:ULONG
 "DispatchCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG)(28, "DispatchCallbacks"),
 #ExitDispatch -> Client:PDEBUG_CLIENT
 "ExitDispatch": ctypes.WINFUNCTYPE(HRESULT, PVOID)(29, "ExitDispatch"),
 #CreateClient -> Client:*PDEBUG_CLIENT
 "CreateClient": ctypes.WINFUNCTYPE(HRESULT, PVOID)(30, "CreateClient"),
 #GetInputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(31, "GetInputCallbacks"),
 #SetInputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(32, "SetInputCallbacks"),
 #GetOutputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(33, "GetOutputCallbacks"),
 #SetOutputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(34, "SetOutputCallbacks"),
 #GetOutputMask -> Mask:PULONG
 "GetOutputMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetOutputMask"),
 #SetOutputMask -> Mask:ULONG
 "SetOutputMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(36, "SetOutputMask"),
 #GetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:PULONG
 "GetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, PULONG)(37, "GetOtherOutputMask"),
 #SetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:ULONG
 "SetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(38, "SetOtherOutputMask"),
 #GetOutputWidth -> Columns:PULONG
 "GetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetOutputWidth"),
 #SetOutputWidth -> Columns:ULONG
 "SetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, ULONG)(40, "SetOutputWidth"),
 #GetOutputLinePrefix -> Buffer:PSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(41, "GetOutputLinePrefix"),
 #SetOutputLinePrefix -> Prefix:PCSTR
 "SetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "SetOutputLinePrefix"),
 #GetIdentity -> Buffer:PSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentity": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetIdentity"),
 #OutputIdentity -> OutputControl:ULONG, Flags:ULONG, Format:PCSTR
 "OutputIdentity": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(44, "OutputIdentity"),
 #GetEventCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(45, "GetEventCallbacks"),
 #SetEventCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(46, "SetEventCallbacks"),
 #FlushCallbacks -> 
 "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
    }


class IDebugClient2(COMInterface):
    IID = generate_IID(0xEDBED635, 0x372E, 0x4DAB, 0xBB, 0xFE, 0xED, 0x0D, 0x2F, 0x63, 0xBE, 0x81, name="IDebugClient2", strid="EDBED635-372E-4DAB-BBFE-ED0D2F63BE81")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #AttachKernel -> Flags:ULONG, ConnectOptions:PCSTR
 "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "AttachKernel"),
 #GetKernelConnectionOptions -> Buffer:PSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(4, "GetKernelConnectionOptions"),
 #SetKernelConnectionOptions -> Options:PCSTR
 "SetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "SetKernelConnectionOptions"),
 #StartProcessServer -> Flags:ULONG, Options:PCSTR, Reserved:PVOID
 "StartProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PVOID)(6, "StartProcessServer"),
 #ConnectProcessServer -> RemoteOptions:PCSTR, Server:PULONG64
 "ConnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(7, "ConnectProcessServer"),
 #DisconnectProcessServer -> Server:ULONG64
 "DisconnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(8, "DisconnectProcessServer"),
 #GetRunningProcessSystemIds -> Server:ULONG64, Ids:PULONG, Count:ULONG, ActualCount:PULONG
 "GetRunningProcessSystemIds": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, ULONG, PULONG)(9, "GetRunningProcessSystemIds"),
 #GetRunningProcessSystemIdByExecutableName -> Server:ULONG64, ExeName:PCSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, ULONG, PULONG)(10, "GetRunningProcessSystemIdByExecutableName"),
 #GetRunningProcessDescription -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(11, "GetRunningProcessDescription"),
 #AttachProcess -> Server:ULONG64, ProcessId:ULONG, AttachFlags:ULONG
 "AttachProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG)(12, "AttachProcess"),
 #CreateProcess -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG)(13, "CreateProcess"),
 #CreateProcessAndAttach -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, ULONG, ULONG)(14, "CreateProcessAndAttach"),
 #GetProcessOptions -> Options:PULONG
 "GetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(15, "GetProcessOptions"),
 #AddProcessOptions -> Options:ULONG
 "AddProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(16, "AddProcessOptions"),
 #RemoveProcessOptions -> Options:ULONG
 "RemoveProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(17, "RemoveProcessOptions"),
 #SetProcessOptions -> Options:ULONG
 "SetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetProcessOptions"),
 #OpenDumpFile -> DumpFile:PCSTR
 "OpenDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(19, "OpenDumpFile"),
 #WriteDumpFile -> DumpFile:PCSTR, Qualifier:ULONG
 "WriteDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(20, "WriteDumpFile"),
 #ConnectSession -> Flags:ULONG, HistoryLimit:ULONG
 "ConnectSession": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "ConnectSession"),
 #StartServer -> Options:PCSTR
 "StartServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "StartServer"),
 #OutputServers -> OutputControl:ULONG, Machine:PCSTR, Flags:ULONG
 "OutputServers": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(23, "OutputServers"),
 #TerminateProcesses -> 
 "TerminateProcesses": ctypes.WINFUNCTYPE(HRESULT)(24, "TerminateProcesses"),
 #DetachProcesses -> 
 "DetachProcesses": ctypes.WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
 #EndSession -> Flags:ULONG
 "EndSession": ctypes.WINFUNCTYPE(HRESULT, ULONG)(26, "EndSession"),
 #GetExitCode -> Code:PULONG
 "GetExitCode": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetExitCode"),
 #DispatchCallbacks -> Timeout:ULONG
 "DispatchCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG)(28, "DispatchCallbacks"),
 #ExitDispatch -> Client:PDEBUG_CLIENT
 "ExitDispatch": ctypes.WINFUNCTYPE(HRESULT, PVOID)(29, "ExitDispatch"),
 #CreateClient -> Client:*PDEBUG_CLIENT
 "CreateClient": ctypes.WINFUNCTYPE(HRESULT, PVOID)(30, "CreateClient"),
 #GetInputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(31, "GetInputCallbacks"),
 #SetInputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(32, "SetInputCallbacks"),
 #GetOutputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(33, "GetOutputCallbacks"),
 #SetOutputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(34, "SetOutputCallbacks"),
 #GetOutputMask -> Mask:PULONG
 "GetOutputMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetOutputMask"),
 #SetOutputMask -> Mask:ULONG
 "SetOutputMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(36, "SetOutputMask"),
 #GetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:PULONG
 "GetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, PULONG)(37, "GetOtherOutputMask"),
 #SetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:ULONG
 "SetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(38, "SetOtherOutputMask"),
 #GetOutputWidth -> Columns:PULONG
 "GetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetOutputWidth"),
 #SetOutputWidth -> Columns:ULONG
 "SetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, ULONG)(40, "SetOutputWidth"),
 #GetOutputLinePrefix -> Buffer:PSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(41, "GetOutputLinePrefix"),
 #SetOutputLinePrefix -> Prefix:PCSTR
 "SetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "SetOutputLinePrefix"),
 #GetIdentity -> Buffer:PSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentity": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetIdentity"),
 #OutputIdentity -> OutputControl:ULONG, Flags:ULONG, Format:PCSTR
 "OutputIdentity": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(44, "OutputIdentity"),
 #GetEventCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(45, "GetEventCallbacks"),
 #SetEventCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(46, "SetEventCallbacks"),
 #FlushCallbacks -> 
 "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
 #WriteDumpFile2 -> DumpFile:PCSTR, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCSTR
 "WriteDumpFile2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, ULONG, PCSTR)(48, "WriteDumpFile2"),
 #AddDumpInformationFile -> InfoFile:PCSTR, Type:ULONG
 "AddDumpInformationFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(49, "AddDumpInformationFile"),
 #EndProcessServer -> Server:ULONG64
 "EndProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(50, "EndProcessServer"),
 #WaitForProcessServerEnd -> Timeout:ULONG
 "WaitForProcessServerEnd": ctypes.WINFUNCTYPE(HRESULT, ULONG)(51, "WaitForProcessServerEnd"),
 #IsKernelDebuggerEnabled -> 
 "IsKernelDebuggerEnabled": ctypes.WINFUNCTYPE(HRESULT)(52, "IsKernelDebuggerEnabled"),
 #TerminateCurrentProcess -> 
 "TerminateCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(53, "TerminateCurrentProcess"),
 #DetachCurrentProcess -> 
 "DetachCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(54, "DetachCurrentProcess"),
 #AbandonCurrentProcess -> 
 "AbandonCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(55, "AbandonCurrentProcess"),
    }


class IDebugClient3(COMInterface):
    IID = generate_IID(0xDD492D7F, 0x71B8, 0x4AD6, 0xA8, 0xDC, 0x1C, 0x88, 0x74, 0x79, 0xFF, 0x91, name="IDebugClient3", strid="DD492D7F-71B8-4AD6-A8DC-1C887479FF91")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #AttachKernel -> Flags:ULONG, ConnectOptions:PCSTR
 "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "AttachKernel"),
 #GetKernelConnectionOptions -> Buffer:PSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(4, "GetKernelConnectionOptions"),
 #SetKernelConnectionOptions -> Options:PCSTR
 "SetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "SetKernelConnectionOptions"),
 #StartProcessServer -> Flags:ULONG, Options:PCSTR, Reserved:PVOID
 "StartProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PVOID)(6, "StartProcessServer"),
 #ConnectProcessServer -> RemoteOptions:PCSTR, Server:PULONG64
 "ConnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(7, "ConnectProcessServer"),
 #DisconnectProcessServer -> Server:ULONG64
 "DisconnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(8, "DisconnectProcessServer"),
 #GetRunningProcessSystemIds -> Server:ULONG64, Ids:PULONG, Count:ULONG, ActualCount:PULONG
 "GetRunningProcessSystemIds": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, ULONG, PULONG)(9, "GetRunningProcessSystemIds"),
 #GetRunningProcessSystemIdByExecutableName -> Server:ULONG64, ExeName:PCSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, ULONG, PULONG)(10, "GetRunningProcessSystemIdByExecutableName"),
 #GetRunningProcessDescription -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(11, "GetRunningProcessDescription"),
 #AttachProcess -> Server:ULONG64, ProcessId:ULONG, AttachFlags:ULONG
 "AttachProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG)(12, "AttachProcess"),
 #CreateProcess -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG)(13, "CreateProcess"),
 #CreateProcessAndAttach -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, ULONG, ULONG)(14, "CreateProcessAndAttach"),
 #GetProcessOptions -> Options:PULONG
 "GetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(15, "GetProcessOptions"),
 #AddProcessOptions -> Options:ULONG
 "AddProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(16, "AddProcessOptions"),
 #RemoveProcessOptions -> Options:ULONG
 "RemoveProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(17, "RemoveProcessOptions"),
 #SetProcessOptions -> Options:ULONG
 "SetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetProcessOptions"),
 #OpenDumpFile -> DumpFile:PCSTR
 "OpenDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(19, "OpenDumpFile"),
 #WriteDumpFile -> DumpFile:PCSTR, Qualifier:ULONG
 "WriteDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(20, "WriteDumpFile"),
 #ConnectSession -> Flags:ULONG, HistoryLimit:ULONG
 "ConnectSession": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "ConnectSession"),
 #StartServer -> Options:PCSTR
 "StartServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "StartServer"),
 #OutputServers -> OutputControl:ULONG, Machine:PCSTR, Flags:ULONG
 "OutputServers": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(23, "OutputServers"),
 #TerminateProcesses -> 
 "TerminateProcesses": ctypes.WINFUNCTYPE(HRESULT)(24, "TerminateProcesses"),
 #DetachProcesses -> 
 "DetachProcesses": ctypes.WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
 #EndSession -> Flags:ULONG
 "EndSession": ctypes.WINFUNCTYPE(HRESULT, ULONG)(26, "EndSession"),
 #GetExitCode -> Code:PULONG
 "GetExitCode": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetExitCode"),
 #DispatchCallbacks -> Timeout:ULONG
 "DispatchCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG)(28, "DispatchCallbacks"),
 #ExitDispatch -> Client:PDEBUG_CLIENT
 "ExitDispatch": ctypes.WINFUNCTYPE(HRESULT, PVOID)(29, "ExitDispatch"),
 #CreateClient -> Client:*PDEBUG_CLIENT
 "CreateClient": ctypes.WINFUNCTYPE(HRESULT, PVOID)(30, "CreateClient"),
 #GetInputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(31, "GetInputCallbacks"),
 #SetInputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(32, "SetInputCallbacks"),
 #GetOutputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(33, "GetOutputCallbacks"),
 #SetOutputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(34, "SetOutputCallbacks"),
 #GetOutputMask -> Mask:PULONG
 "GetOutputMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetOutputMask"),
 #SetOutputMask -> Mask:ULONG
 "SetOutputMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(36, "SetOutputMask"),
 #GetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:PULONG
 "GetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, PULONG)(37, "GetOtherOutputMask"),
 #SetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:ULONG
 "SetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(38, "SetOtherOutputMask"),
 #GetOutputWidth -> Columns:PULONG
 "GetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetOutputWidth"),
 #SetOutputWidth -> Columns:ULONG
 "SetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, ULONG)(40, "SetOutputWidth"),
 #GetOutputLinePrefix -> Buffer:PSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(41, "GetOutputLinePrefix"),
 #SetOutputLinePrefix -> Prefix:PCSTR
 "SetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "SetOutputLinePrefix"),
 #GetIdentity -> Buffer:PSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentity": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetIdentity"),
 #OutputIdentity -> OutputControl:ULONG, Flags:ULONG, Format:PCSTR
 "OutputIdentity": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(44, "OutputIdentity"),
 #GetEventCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(45, "GetEventCallbacks"),
 #SetEventCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(46, "SetEventCallbacks"),
 #FlushCallbacks -> 
 "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
 #WriteDumpFile2 -> DumpFile:PCSTR, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCSTR
 "WriteDumpFile2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, ULONG, PCSTR)(48, "WriteDumpFile2"),
 #AddDumpInformationFile -> InfoFile:PCSTR, Type:ULONG
 "AddDumpInformationFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(49, "AddDumpInformationFile"),
 #EndProcessServer -> Server:ULONG64
 "EndProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(50, "EndProcessServer"),
 #WaitForProcessServerEnd -> Timeout:ULONG
 "WaitForProcessServerEnd": ctypes.WINFUNCTYPE(HRESULT, ULONG)(51, "WaitForProcessServerEnd"),
 #IsKernelDebuggerEnabled -> 
 "IsKernelDebuggerEnabled": ctypes.WINFUNCTYPE(HRESULT)(52, "IsKernelDebuggerEnabled"),
 #TerminateCurrentProcess -> 
 "TerminateCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(53, "TerminateCurrentProcess"),
 #DetachCurrentProcess -> 
 "DetachCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(54, "DetachCurrentProcess"),
 #AbandonCurrentProcess -> 
 "AbandonCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(55, "AbandonCurrentProcess"),
 #GetRunningProcessSystemIdByExecutableNameWide -> Server:ULONG64, ExeName:PCWSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, ULONG, PULONG)(56, "GetRunningProcessSystemIdByExecutableNameWide"),
 #GetRunningProcessDescriptionWide -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PWSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PWSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(57, "GetRunningProcessDescriptionWide"),
 #CreateProcessWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG
 "CreateProcessWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG)(58, "CreateProcessWide"),
 #CreateProcessAndAttachWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttachWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG, ULONG, ULONG)(59, "CreateProcessAndAttachWide"),
    }


class IDebugClient4(COMInterface):
    IID = generate_IID(0xCA83C3DE, 0x5089, 0x4CF8, 0x93, 0xC8, 0xD8, 0x92, 0x38, 0x7F, 0x2A, 0x5E, name="IDebugClient4", strid="CA83C3DE-5089-4CF8-93C8-D892387F2A5E")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #AttachKernel -> Flags:ULONG, ConnectOptions:PCSTR
 "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "AttachKernel"),
 #GetKernelConnectionOptions -> Buffer:PSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(4, "GetKernelConnectionOptions"),
 #SetKernelConnectionOptions -> Options:PCSTR
 "SetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "SetKernelConnectionOptions"),
 #StartProcessServer -> Flags:ULONG, Options:PCSTR, Reserved:PVOID
 "StartProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PVOID)(6, "StartProcessServer"),
 #ConnectProcessServer -> RemoteOptions:PCSTR, Server:PULONG64
 "ConnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(7, "ConnectProcessServer"),
 #DisconnectProcessServer -> Server:ULONG64
 "DisconnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(8, "DisconnectProcessServer"),
 #GetRunningProcessSystemIds -> Server:ULONG64, Ids:PULONG, Count:ULONG, ActualCount:PULONG
 "GetRunningProcessSystemIds": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, ULONG, PULONG)(9, "GetRunningProcessSystemIds"),
 #GetRunningProcessSystemIdByExecutableName -> Server:ULONG64, ExeName:PCSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, ULONG, PULONG)(10, "GetRunningProcessSystemIdByExecutableName"),
 #GetRunningProcessDescription -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(11, "GetRunningProcessDescription"),
 #AttachProcess -> Server:ULONG64, ProcessId:ULONG, AttachFlags:ULONG
 "AttachProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG)(12, "AttachProcess"),
 #CreateProcess -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG)(13, "CreateProcess"),
 #CreateProcessAndAttach -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, ULONG, ULONG)(14, "CreateProcessAndAttach"),
 #GetProcessOptions -> Options:PULONG
 "GetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(15, "GetProcessOptions"),
 #AddProcessOptions -> Options:ULONG
 "AddProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(16, "AddProcessOptions"),
 #RemoveProcessOptions -> Options:ULONG
 "RemoveProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(17, "RemoveProcessOptions"),
 #SetProcessOptions -> Options:ULONG
 "SetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetProcessOptions"),
 #OpenDumpFile -> DumpFile:PCSTR
 "OpenDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(19, "OpenDumpFile"),
 #WriteDumpFile -> DumpFile:PCSTR, Qualifier:ULONG
 "WriteDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(20, "WriteDumpFile"),
 #ConnectSession -> Flags:ULONG, HistoryLimit:ULONG
 "ConnectSession": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "ConnectSession"),
 #StartServer -> Options:PCSTR
 "StartServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "StartServer"),
 #OutputServers -> OutputControl:ULONG, Machine:PCSTR, Flags:ULONG
 "OutputServers": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(23, "OutputServers"),
 #TerminateProcesses -> 
 "TerminateProcesses": ctypes.WINFUNCTYPE(HRESULT)(24, "TerminateProcesses"),
 #DetachProcesses -> 
 "DetachProcesses": ctypes.WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
 #EndSession -> Flags:ULONG
 "EndSession": ctypes.WINFUNCTYPE(HRESULT, ULONG)(26, "EndSession"),
 #GetExitCode -> Code:PULONG
 "GetExitCode": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetExitCode"),
 #DispatchCallbacks -> Timeout:ULONG
 "DispatchCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG)(28, "DispatchCallbacks"),
 #ExitDispatch -> Client:PDEBUG_CLIENT
 "ExitDispatch": ctypes.WINFUNCTYPE(HRESULT, PVOID)(29, "ExitDispatch"),
 #CreateClient -> Client:*PDEBUG_CLIENT
 "CreateClient": ctypes.WINFUNCTYPE(HRESULT, PVOID)(30, "CreateClient"),
 #GetInputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(31, "GetInputCallbacks"),
 #SetInputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(32, "SetInputCallbacks"),
 #GetOutputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(33, "GetOutputCallbacks"),
 #SetOutputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(34, "SetOutputCallbacks"),
 #GetOutputMask -> Mask:PULONG
 "GetOutputMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetOutputMask"),
 #SetOutputMask -> Mask:ULONG
 "SetOutputMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(36, "SetOutputMask"),
 #GetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:PULONG
 "GetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, PULONG)(37, "GetOtherOutputMask"),
 #SetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:ULONG
 "SetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(38, "SetOtherOutputMask"),
 #GetOutputWidth -> Columns:PULONG
 "GetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetOutputWidth"),
 #SetOutputWidth -> Columns:ULONG
 "SetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, ULONG)(40, "SetOutputWidth"),
 #GetOutputLinePrefix -> Buffer:PSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(41, "GetOutputLinePrefix"),
 #SetOutputLinePrefix -> Prefix:PCSTR
 "SetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "SetOutputLinePrefix"),
 #GetIdentity -> Buffer:PSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentity": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetIdentity"),
 #OutputIdentity -> OutputControl:ULONG, Flags:ULONG, Format:PCSTR
 "OutputIdentity": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(44, "OutputIdentity"),
 #GetEventCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(45, "GetEventCallbacks"),
 #SetEventCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(46, "SetEventCallbacks"),
 #FlushCallbacks -> 
 "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
 #WriteDumpFile2 -> DumpFile:PCSTR, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCSTR
 "WriteDumpFile2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, ULONG, PCSTR)(48, "WriteDumpFile2"),
 #AddDumpInformationFile -> InfoFile:PCSTR, Type:ULONG
 "AddDumpInformationFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(49, "AddDumpInformationFile"),
 #EndProcessServer -> Server:ULONG64
 "EndProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(50, "EndProcessServer"),
 #WaitForProcessServerEnd -> Timeout:ULONG
 "WaitForProcessServerEnd": ctypes.WINFUNCTYPE(HRESULT, ULONG)(51, "WaitForProcessServerEnd"),
 #IsKernelDebuggerEnabled -> 
 "IsKernelDebuggerEnabled": ctypes.WINFUNCTYPE(HRESULT)(52, "IsKernelDebuggerEnabled"),
 #TerminateCurrentProcess -> 
 "TerminateCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(53, "TerminateCurrentProcess"),
 #DetachCurrentProcess -> 
 "DetachCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(54, "DetachCurrentProcess"),
 #AbandonCurrentProcess -> 
 "AbandonCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(55, "AbandonCurrentProcess"),
 #GetRunningProcessSystemIdByExecutableNameWide -> Server:ULONG64, ExeName:PCWSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, ULONG, PULONG)(56, "GetRunningProcessSystemIdByExecutableNameWide"),
 #GetRunningProcessDescriptionWide -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PWSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PWSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(57, "GetRunningProcessDescriptionWide"),
 #CreateProcessWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG
 "CreateProcessWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG)(58, "CreateProcessWide"),
 #CreateProcessAndAttachWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttachWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG, ULONG, ULONG)(59, "CreateProcessAndAttachWide"),
 #OpenDumpFileWide -> FileName:PCWSTR, FileHandle:ULONG64
 "OpenDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64)(60, "OpenDumpFileWide"),
 #WriteDumpFileWide -> FileName:PCWSTR, FileHandle:ULONG64, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCWSTR
 "WriteDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64, ULONG, ULONG, PCWSTR)(61, "WriteDumpFileWide"),
 #AddDumpInformationFileWide -> FileName:PCWSTR, FileHandle:ULONG64, Type:ULONG
 "AddDumpInformationFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64, ULONG)(62, "AddDumpInformationFileWide"),
 #GetNumberDumpFiles -> Number:PULONG
 "GetNumberDumpFiles": ctypes.WINFUNCTYPE(HRESULT, PULONG)(63, "GetNumberDumpFiles"),
 #GetDumpFile -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG, Handle:PULONG64, Type:PULONG
 "GetDumpFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PULONG64, PULONG)(64, "GetDumpFile"),
 #GetDumpFileWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG, Handle:PULONG64, Type:PULONG
 "GetDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PULONG64, PULONG)(65, "GetDumpFileWide"),
    }


class IDebugClient5(COMInterface):
    IID = generate_IID(0xE3ACB9D7, 0x7EC2, 0x4F0C, 0xA0, 0xDA, 0xE8, 0x1E, 0x0C, 0xBB, 0xE6, 0x28, name="IDebugClient5", strid="E3ACB9D7-7EC2-4F0C-A0DA-E81E0CBBE628")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #AttachKernel -> Flags:ULONG, ConnectOptions:PCSTR
 "AttachKernel": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "AttachKernel"),
 #GetKernelConnectionOptions -> Buffer:PSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(4, "GetKernelConnectionOptions"),
 #SetKernelConnectionOptions -> Options:PCSTR
 "SetKernelConnectionOptions": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "SetKernelConnectionOptions"),
 #StartProcessServer -> Flags:ULONG, Options:PCSTR, Reserved:PVOID
 "StartProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PVOID)(6, "StartProcessServer"),
 #ConnectProcessServer -> RemoteOptions:PCSTR, Server:PULONG64
 "ConnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(7, "ConnectProcessServer"),
 #DisconnectProcessServer -> Server:ULONG64
 "DisconnectProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(8, "DisconnectProcessServer"),
 #GetRunningProcessSystemIds -> Server:ULONG64, Ids:PULONG, Count:ULONG, ActualCount:PULONG
 "GetRunningProcessSystemIds": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, ULONG, PULONG)(9, "GetRunningProcessSystemIds"),
 #GetRunningProcessSystemIdByExecutableName -> Server:ULONG64, ExeName:PCSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, ULONG, PULONG)(10, "GetRunningProcessSystemIdByExecutableName"),
 #GetRunningProcessDescription -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(11, "GetRunningProcessDescription"),
 #AttachProcess -> Server:ULONG64, ProcessId:ULONG, AttachFlags:ULONG
 "AttachProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG)(12, "AttachProcess"),
 #CreateProcess -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG)(13, "CreateProcess"),
 #CreateProcessAndAttach -> Server:ULONG64, CommandLine:PSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, ULONG, ULONG)(14, "CreateProcessAndAttach"),
 #GetProcessOptions -> Options:PULONG
 "GetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(15, "GetProcessOptions"),
 #AddProcessOptions -> Options:ULONG
 "AddProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(16, "AddProcessOptions"),
 #RemoveProcessOptions -> Options:ULONG
 "RemoveProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(17, "RemoveProcessOptions"),
 #SetProcessOptions -> Options:ULONG
 "SetProcessOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(18, "SetProcessOptions"),
 #OpenDumpFile -> DumpFile:PCSTR
 "OpenDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(19, "OpenDumpFile"),
 #WriteDumpFile -> DumpFile:PCSTR, Qualifier:ULONG
 "WriteDumpFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(20, "WriteDumpFile"),
 #ConnectSession -> Flags:ULONG, HistoryLimit:ULONG
 "ConnectSession": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "ConnectSession"),
 #StartServer -> Options:PCSTR
 "StartServer": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(22, "StartServer"),
 #OutputServers -> OutputControl:ULONG, Machine:PCSTR, Flags:ULONG
 "OutputServers": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(23, "OutputServers"),
 #TerminateProcesses -> 
 "TerminateProcesses": ctypes.WINFUNCTYPE(HRESULT)(24, "TerminateProcesses"),
 #DetachProcesses -> 
 "DetachProcesses": ctypes.WINFUNCTYPE(HRESULT)(25, "DetachProcesses"),
 #EndSession -> Flags:ULONG
 "EndSession": ctypes.WINFUNCTYPE(HRESULT, ULONG)(26, "EndSession"),
 #GetExitCode -> Code:PULONG
 "GetExitCode": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetExitCode"),
 #DispatchCallbacks -> Timeout:ULONG
 "DispatchCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG)(28, "DispatchCallbacks"),
 #ExitDispatch -> Client:PDEBUG_CLIENT
 "ExitDispatch": ctypes.WINFUNCTYPE(HRESULT, PVOID)(29, "ExitDispatch"),
 #CreateClient -> Client:*PDEBUG_CLIENT
 "CreateClient": ctypes.WINFUNCTYPE(HRESULT, PVOID)(30, "CreateClient"),
 #GetInputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(31, "GetInputCallbacks"),
 #SetInputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(32, "SetInputCallbacks"),
 #GetOutputCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(33, "GetOutputCallbacks"),
 #SetOutputCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(34, "SetOutputCallbacks"),
 #GetOutputMask -> Mask:PULONG
 "GetOutputMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetOutputMask"),
 #SetOutputMask -> Mask:ULONG
 "SetOutputMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(36, "SetOutputMask"),
 #GetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:PULONG
 "GetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, PULONG)(37, "GetOtherOutputMask"),
 #SetOtherOutputMask -> Client:PDEBUG_CLIENT, Mask:ULONG
 "SetOtherOutputMask": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG)(38, "SetOtherOutputMask"),
 #GetOutputWidth -> Columns:PULONG
 "GetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetOutputWidth"),
 #SetOutputWidth -> Columns:ULONG
 "SetOutputWidth": ctypes.WINFUNCTYPE(HRESULT, ULONG)(40, "SetOutputWidth"),
 #GetOutputLinePrefix -> Buffer:PSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(41, "GetOutputLinePrefix"),
 #SetOutputLinePrefix -> Prefix:PCSTR
 "SetOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "SetOutputLinePrefix"),
 #GetIdentity -> Buffer:PSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentity": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetIdentity"),
 #OutputIdentity -> OutputControl:ULONG, Flags:ULONG, Format:PCSTR
 "OutputIdentity": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(44, "OutputIdentity"),
 #GetEventCallbacks -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(45, "GetEventCallbacks"),
 #SetEventCallbacks -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, PVOID)(46, "SetEventCallbacks"),
 #FlushCallbacks -> 
 "FlushCallbacks": ctypes.WINFUNCTYPE(HRESULT)(47, "FlushCallbacks"),
 #WriteDumpFile2 -> DumpFile:PCSTR, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCSTR
 "WriteDumpFile2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, ULONG, PCSTR)(48, "WriteDumpFile2"),
 #AddDumpInformationFile -> InfoFile:PCSTR, Type:ULONG
 "AddDumpInformationFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(49, "AddDumpInformationFile"),
 #EndProcessServer -> Server:ULONG64
 "EndProcessServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(50, "EndProcessServer"),
 #WaitForProcessServerEnd -> Timeout:ULONG
 "WaitForProcessServerEnd": ctypes.WINFUNCTYPE(HRESULT, ULONG)(51, "WaitForProcessServerEnd"),
 #IsKernelDebuggerEnabled -> 
 "IsKernelDebuggerEnabled": ctypes.WINFUNCTYPE(HRESULT)(52, "IsKernelDebuggerEnabled"),
 #TerminateCurrentProcess -> 
 "TerminateCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(53, "TerminateCurrentProcess"),
 #DetachCurrentProcess -> 
 "DetachCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(54, "DetachCurrentProcess"),
 #AbandonCurrentProcess -> 
 "AbandonCurrentProcess": ctypes.WINFUNCTYPE(HRESULT)(55, "AbandonCurrentProcess"),
 #GetRunningProcessSystemIdByExecutableNameWide -> Server:ULONG64, ExeName:PCWSTR, Flags:ULONG, Id:PULONG
 "GetRunningProcessSystemIdByExecutableNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, ULONG, PULONG)(56, "GetRunningProcessSystemIdByExecutableNameWide"),
 #GetRunningProcessDescriptionWide -> Server:ULONG64, SystemId:ULONG, Flags:ULONG, ExeName:PWSTR, ExeNameSize:ULONG, ActualExeNameSize:PULONG, Description:PWSTR, DescriptionSize:ULONG, ActualDescriptionSize:PULONG
 "GetRunningProcessDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(57, "GetRunningProcessDescriptionWide"),
 #CreateProcessWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG
 "CreateProcessWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG)(58, "CreateProcessWide"),
 #CreateProcessAndAttachWide -> Server:ULONG64, CommandLine:PWSTR, CreateFlags:ULONG, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttachWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG, ULONG, ULONG)(59, "CreateProcessAndAttachWide"),
 #OpenDumpFileWide -> FileName:PCWSTR, FileHandle:ULONG64
 "OpenDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64)(60, "OpenDumpFileWide"),
 #WriteDumpFileWide -> FileName:PCWSTR, FileHandle:ULONG64, Qualifier:ULONG, FormatFlags:ULONG, Comment:PCWSTR
 "WriteDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64, ULONG, ULONG, PCWSTR)(61, "WriteDumpFileWide"),
 #AddDumpInformationFileWide -> FileName:PCWSTR, FileHandle:ULONG64, Type:ULONG
 "AddDumpInformationFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64, ULONG)(62, "AddDumpInformationFileWide"),
 #GetNumberDumpFiles -> Number:PULONG
 "GetNumberDumpFiles": ctypes.WINFUNCTYPE(HRESULT, PULONG)(63, "GetNumberDumpFiles"),
 #GetDumpFile -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG, Handle:PULONG64, Type:PULONG
 "GetDumpFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PULONG64, PULONG)(64, "GetDumpFile"),
 #GetDumpFileWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG, Handle:PULONG64, Type:PULONG
 "GetDumpFileWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PULONG64, PULONG)(65, "GetDumpFileWide"),
 #AttachKernelWide -> Flags:ULONG, ConnectOptions:PCWSTR
 "AttachKernelWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(66, "AttachKernelWide"),
 #GetKernelConnectionOptionsWide -> Buffer:PWSTR, BufferSize:ULONG, OptionsSize:PULONG
 "GetKernelConnectionOptionsWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(67, "GetKernelConnectionOptionsWide"),
 #SetKernelConnectionOptionsWide -> Options:PCWSTR
 "SetKernelConnectionOptionsWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(68, "SetKernelConnectionOptionsWide"),
 #StartProcessServerWide -> Flags:ULONG, Options:PCWSTR, Reserved:PVOID
 "StartProcessServerWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, PVOID)(69, "StartProcessServerWide"),
 #ConnectProcessServerWide -> RemoteOptions:PCWSTR, Server:PULONG64
 "ConnectProcessServerWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(70, "ConnectProcessServerWide"),
 #StartServerWide -> Options:PCWSTR
 "StartServerWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(71, "StartServerWide"),
 #OutputServersWide -> OutputControl:ULONG, Machine:PCWSTR, Flags:ULONG
 "OutputServersWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, ULONG)(72, "OutputServersWide"),
 #GetOutputCallbacksWide -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetOutputCallbacksWide": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "GetOutputCallbacksWide"),
 #SetOutputCallbacksWide -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetOutputCallbacksWide": ctypes.WINFUNCTYPE(HRESULT, PVOID)(74, "SetOutputCallbacksWide"),
 #GetOutputLinePrefixWide -> Buffer:PWSTR, BufferSize:ULONG, PrefixSize:PULONG
 "GetOutputLinePrefixWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(75, "GetOutputLinePrefixWide"),
 #SetOutputLinePrefixWide -> Prefix:PCWSTR
 "SetOutputLinePrefixWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(76, "SetOutputLinePrefixWide"),
 #GetIdentityWide -> Buffer:PWSTR, BufferSize:ULONG, IdentitySize:PULONG
 "GetIdentityWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(77, "GetIdentityWide"),
 #OutputIdentityWide -> OutputControl:ULONG, Flags:ULONG, Format:PCWSTR
 "OutputIdentityWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCWSTR)(78, "OutputIdentityWide"),
 #GetEventCallbacksWide -> Callbacks:*PDEBUG_EVENT_CALLBACKS_WIDE
 "GetEventCallbacksWide": ctypes.WINFUNCTYPE(HRESULT, PVOID)(79, "GetEventCallbacksWide"),
 #SetEventCallbacksWide -> Callbacks:PDEBUG_EVENT_CALLBACKS_WIDE
 "SetEventCallbacksWide": ctypes.WINFUNCTYPE(HRESULT, PVOID)(80, "SetEventCallbacksWide"),
 #CreateProcess2 -> Server:ULONG64, CommandLine:PSTR, OptionsBuffer:PVOID, OptionsBufferSize:ULONG, InitialDirectory:PCSTR, Environment:PCSTR
 "CreateProcess2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, PVOID, ULONG, PCSTR, PCSTR)(81, "CreateProcess2"),
 #CreateProcess2Wide -> Server:ULONG64, CommandLine:PWSTR, OptionsBuffer:PVOID, OptionsBufferSize:ULONG, InitialDirectory:PCWSTR, Environment:PCWSTR
 "CreateProcess2Wide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, PVOID, ULONG, PCWSTR, PCWSTR)(82, "CreateProcess2Wide"),
 #CreateProcessAndAttach2 -> Server:ULONG64, CommandLine:PSTR, OptionsBuffer:PVOID, OptionsBufferSize:ULONG, InitialDirectory:PCSTR, Environment:PCSTR, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, PVOID, ULONG, PCSTR, PCSTR, ULONG, ULONG)(83, "CreateProcessAndAttach2"),
 #CreateProcessAndAttach2Wide -> Server:ULONG64, CommandLine:PWSTR, OptionsBuffer:PVOID, OptionsBufferSize:ULONG, InitialDirectory:PCWSTR, Environment:PCWSTR, ProcessId:ULONG, AttachFlags:ULONG
 "CreateProcessAndAttach2Wide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, PVOID, ULONG, PCWSTR, PCWSTR, ULONG, ULONG)(84, "CreateProcessAndAttach2Wide"),
 #PushOutputLinePrefix -> NewPrefix:PCSTR, Handle:PULONG64
 "PushOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(85, "PushOutputLinePrefix"),
 #PushOutputLinePrefixWide -> NewPrefix:PCWSTR, Handle:PULONG64
 "PushOutputLinePrefixWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(86, "PushOutputLinePrefixWide"),
 #PopOutputLinePrefix -> Handle:ULONG64
 "PopOutputLinePrefix": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(87, "PopOutputLinePrefix"),
 #GetNumberInputCallbacks -> Count:PULONG
 "GetNumberInputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PULONG)(88, "GetNumberInputCallbacks"),
 #GetNumberOutputCallbacks -> Count:PULONG
 "GetNumberOutputCallbacks": ctypes.WINFUNCTYPE(HRESULT, PULONG)(89, "GetNumberOutputCallbacks"),
 #GetNumberEventCallbacks -> EventFlags:ULONG, Count:PULONG
 "GetNumberEventCallbacks": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(90, "GetNumberEventCallbacks"),
 #GetQuitLockString -> Buffer:PSTR, BufferSize:ULONG, StringSize:PULONG
 "GetQuitLockString": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(91, "GetQuitLockString"),
 #SetQuitLockString -> String:PCSTR
 "SetQuitLockString": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(92, "SetQuitLockString"),
 #GetQuitLockStringWide -> Buffer:PWSTR, BufferSize:ULONG, StringSize:PULONG
 "GetQuitLockStringWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(93, "GetQuitLockStringWide"),
 #SetQuitLockStringWide -> String:PCWSTR
 "SetQuitLockStringWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(94, "SetQuitLockStringWide"),
    }


class IDebugControl(COMInterface):
    IID = generate_IID(0x5182E668, 0x105E, 0x416E, 0xAD, 0x92, 0x24, 0xEF, 0x80, 0x04, 0x24, 0xBA, name="IDebugControl", strid="5182E668-105E-416E-AD92-24EF800424BA")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterrupt -> 
 "GetInterrupt": ctypes.WINFUNCTYPE(HRESULT)(3, "GetInterrupt"),
 #SetInterrupt -> Flags:ULONG
 "SetInterrupt": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "SetInterrupt"),
 #GetInterruptTimeout -> Seconds:PULONG
 "GetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetInterruptTimeout"),
 #SetInterruptTimeout -> Seconds:ULONG
 "SetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetInterruptTimeout"),
 #GetLogFile -> Buffer:PSTR, BufferSize:ULONG, FileSize:PULONG, Append:PBOOL
 "GetLogFile": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG, PBOOL)(7, "GetLogFile"),
 #OpenLogFile -> File:PCSTR, Append:BOOL
 "OpenLogFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, BOOL)(8, "OpenLogFile"),
 #CloseLogFile -> 
 "CloseLogFile": ctypes.WINFUNCTYPE(HRESULT)(9, "CloseLogFile"),
 #GetLogMask -> Mask:PULONG
 "GetLogMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(10, "GetLogMask"),
 #SetLogMask -> Mask:ULONG
 "SetLogMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(11, "SetLogMask"),
 #Input -> Buffer:PSTR, BufferSize:ULONG, InputSize:PULONG
 "Input": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(12, "Input"),
 #ReturnInput -> Buffer:PCSTR
 "ReturnInput": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(13, "ReturnInput"),
 #Output -> Mask:ULONG, Format:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(14, "Output"),
 #OutputVaList -> Mask:ULONG, Format:PCSTR, Args:va_list
 "OutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(15, "OutputVaList"),
 #ControlledOutput -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR
 "ControlledOutput": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(16, "ControlledOutput"),
 #ControlledOutputVaList -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR, Args:va_list
 "ControlledOutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR, va_list)(17, "ControlledOutputVaList"),
 #OutputPrompt -> OutputControl:ULONG, Format:PCSTR
 "OutputPrompt": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(18, "OutputPrompt"),
 #OutputPromptVaList -> OutputControl:ULONG, Format:PCSTR, Args:va_list
 "OutputPromptVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(19, "OutputPromptVaList"),
 #GetPromptText -> Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetPromptText": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(20, "GetPromptText"),
 #OutputCurrentState -> OutputControl:ULONG, Flags:ULONG
 "OutputCurrentState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "OutputCurrentState"),
 #OutputVersionInformation -> OutputControl:ULONG
 "OutputVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG)(22, "OutputVersionInformation"),
 #GetNotifyEventHandle -> Handle:PULONG64
 "GetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetNotifyEventHandle"),
 #SetNotifyEventHandle -> Handle:ULONG64
 "SetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(24, "SetNotifyEventHandle"),
 #Assemble -> Offset:ULONG64, Instr:PCSTR, EndOffset:PULONG64
 "Assemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG64)(25, "Assemble"),
 #Disassemble -> Offset:ULONG64, Flags:ULONG, Buffer:PSTR, BufferSize:ULONG, DisassemblySize:PULONG, EndOffset:PULONG64
 "Disassemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG, PULONG64)(26, "Disassemble"),
 #GetDisassembleEffectiveOffset -> Offset:PULONG64
 "GetDisassembleEffectiveOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(27, "GetDisassembleEffectiveOffset"),
 #OutputDisassembly -> OutputControl:ULONG, Offset:ULONG64, Flags:ULONG, EndOffset:PULONG64
 "OutputDisassembly": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PULONG64)(28, "OutputDisassembly"),
 #OutputDisassemblyLines -> OutputControl:ULONG, PreviousLines:ULONG, TotalLines:ULONG, Offset:ULONG64, Flags:ULONG, OffsetLine:PULONG, StartOffset:PULONG64, EndOffset:PULONG64, LineOffsets:PULONG64
 "OutputDisassemblyLines": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, ULONG, PULONG, PULONG64, PULONG64, PULONG64)(29, "OutputDisassemblyLines"),
 #GetNearInstruction -> Offset:ULONG64, Delta:LONG, NearOffset:PULONG64
 "GetNearInstruction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PULONG64)(30, "GetNearInstruction"),
 #GetStackTrace -> FrameOffset:ULONG64, StackOffset:ULONG64, InstructionOffset:ULONG64, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FramesFilled:PULONG
 "GetStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, PDEBUG_STACK_FRAME, ULONG, PULONG)(31, "GetStackTrace"),
 #GetReturnOffset -> Offset:PULONG64
 "GetReturnOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(32, "GetReturnOffset"),
 #OutputStackTrace -> OutputControl:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, Flags:ULONG
 "OutputStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_STACK_FRAME, ULONG, ULONG)(33, "OutputStackTrace"),
 #GetDebuggeeType -> Class:PULONG, Qualifier:PULONG
 "GetDebuggeeType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(34, "GetDebuggeeType"),
 #GetActualProcessorType -> Type:PULONG
 "GetActualProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetActualProcessorType"),
 #GetExecutingProcessorType -> Type:PULONG
 "GetExecutingProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(36, "GetExecutingProcessorType"),
 #GetNumberPossibleExecutingProcessorTypes -> Number:PULONG
 "GetNumberPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetNumberPossibleExecutingProcessorTypes"),
 #GetPossibleExecutingProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(38, "GetPossibleExecutingProcessorTypes"),
 #GetNumberProcessors -> Number:PULONG
 "GetNumberProcessors": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetNumberProcessors"),
 #GetSystemVersion -> PlatformId:PULONG, Major:PULONG, Minor:PULONG, ServicePackString:PSTR, ServicePackStringSize:ULONG, ServicePackStringUsed:PULONG, ServicePackNumber:PULONG, BuildString:PSTR, BuildStringSize:ULONG, BuildStringUsed:PULONG
 "GetSystemVersion": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PSTR, ULONG, PULONG, PULONG, PSTR, ULONG, PULONG)(40, "GetSystemVersion"),
 #GetPageSize -> Size:PULONG
 "GetPageSize": ctypes.WINFUNCTYPE(HRESULT, PULONG)(41, "GetPageSize"),
 #IsPointer64Bit -> 
 "IsPointer64Bit": ctypes.WINFUNCTYPE(HRESULT)(42, "IsPointer64Bit"),
 #ReadBugCheckData -> Code:PULONG, Arg1:PULONG64, Arg2:PULONG64, Arg3:PULONG64, Arg4:PULONG64
 "ReadBugCheckData": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG64, PULONG64, PULONG64, PULONG64)(43, "ReadBugCheckData"),
 #GetNumberSupportedProcessorTypes -> Number:PULONG
 "GetNumberSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(44, "GetNumberSupportedProcessorTypes"),
 #GetSupportedProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(45, "GetSupportedProcessorTypes"),
 #GetProcessorTypeNames -> Type:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetProcessorTypeNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(46, "GetProcessorTypeNames"),
 #GetEffectiveProcessorType -> Type:PULONG
 "GetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(47, "GetEffectiveProcessorType"),
 #SetEffectiveProcessorType -> Type:ULONG
 "SetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, ULONG)(48, "SetEffectiveProcessorType"),
 #GetExecutionStatus -> Status:PULONG
 "GetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG)(49, "GetExecutionStatus"),
 #SetExecutionStatus -> Status:ULONG
 "SetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(50, "SetExecutionStatus"),
 #GetCodeLevel -> Level:PULONG
 "GetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, PULONG)(51, "GetCodeLevel"),
 #SetCodeLevel -> Level:ULONG
 "SetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, ULONG)(52, "SetCodeLevel"),
 #GetEngineOptions -> Options:PULONG
 "GetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(53, "GetEngineOptions"),
 #AddEngineOptions -> Options:ULONG
 "AddEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(54, "AddEngineOptions"),
 #RemoveEngineOptions -> Options:ULONG
 "RemoveEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(55, "RemoveEngineOptions"),
 #SetEngineOptions -> Options:ULONG
 "SetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(56, "SetEngineOptions"),
 #GetSystemErrorControl -> OutputLevel:PULONG, BreakLevel:PULONG
 "GetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(57, "GetSystemErrorControl"),
 #SetSystemErrorControl -> OutputLevel:ULONG, BreakLevel:ULONG
 "SetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(58, "SetSystemErrorControl"),
 #GetTextMacro -> Slot:ULONG, Buffer:PSTR, BufferSize:ULONG, MacroSize:PULONG
 "GetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(59, "GetTextMacro"),
 #SetTextMacro -> Slot:ULONG, Macro:PCSTR
 "SetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(60, "SetTextMacro"),
 #GetRadix -> Radix:PULONG
 "GetRadix": ctypes.WINFUNCTYPE(HRESULT, PULONG)(61, "GetRadix"),
 #SetRadix -> Radix:ULONG
 "SetRadix": ctypes.WINFUNCTYPE(HRESULT, ULONG)(62, "SetRadix"),
 #Evaluate -> Expression:PCSTR, DesiredType:ULONG, Value:PDEBUG_VALUE, RemainderIndex:PULONG
 "Evaluate": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PDEBUG_VALUE, PULONG)(63, "Evaluate"),
 #CoerceValue -> In:PDEBUG_VALUE, OutType:ULONG, Out:PDEBUG_VALUE
 "CoerceValue": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_VALUE, ULONG, PDEBUG_VALUE)(64, "CoerceValue"),
 #CoerceValues -> Count:ULONG, In:PDEBUG_VALUE, OutTypes:PULONG, Out:PDEBUG_VALUE
 "CoerceValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE, PULONG, PDEBUG_VALUE)(65, "CoerceValues"),
 #Execute -> OutputControl:ULONG, Command:PCSTR, Flags:ULONG
 "Execute": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(66, "Execute"),
 #ExecuteCommandFile -> OutputControl:ULONG, CommandFile:PCSTR, Flags:ULONG
 "ExecuteCommandFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(67, "ExecuteCommandFile"),
 #GetNumberBreakpoints -> Number:PULONG
 "GetNumberBreakpoints": ctypes.WINFUNCTYPE(HRESULT, PULONG)(68, "GetNumberBreakpoints"),
 #GetBreakpointByIndex -> Index:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(69, "GetBreakpointByIndex"),
 #GetBreakpointById -> Id:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointById": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(70, "GetBreakpointById"),
 #GetBreakpointParameters -> Count:ULONG, Ids:PULONG, Start:ULONG, Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetBreakpointParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_BREAKPOINT_PARAMETERS)(71, "GetBreakpointParameters"),
 #AddBreakpoint -> Type:ULONG, DesiredId:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "AddBreakpoint": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(72, "AddBreakpoint"),
 #RemoveBreakpoint -> Bp:PDEBUG_BREAKPOINT2
 "RemoveBreakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "RemoveBreakpoint"),
 #AddExtension -> Path:PCSTR, Flags:ULONG, Handle:PULONG64
 "AddExtension": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG64)(74, "AddExtension"),
 #RemoveExtension -> Handle:ULONG64
 "RemoveExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(75, "RemoveExtension"),
 #GetExtensionByPath -> Path:PCSTR, Handle:PULONG64
 "GetExtensionByPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(76, "GetExtensionByPath"),
 #CallExtension -> Handle:ULONG64, Function:PCSTR, Arguments:PCSTR
 "CallExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PCSTR)(77, "CallExtension"),
 #GetExtensionFunction -> Handle:ULONG64, FuncName:PCSTR, Function:*FARPROC
 "GetExtensionFunction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, POINTER(FARPROC))(78, "GetExtensionFunction"),
 #GetWindbgExtensionApis32 -> Api:PWINDBG_EXTENSION_APIS32
 "GetWindbgExtensionApis32": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS32)(79, "GetWindbgExtensionApis32"),
 #GetWindbgExtensionApis64 -> Api:PWINDBG_EXTENSION_APIS64
 "GetWindbgExtensionApis64": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS64)(80, "GetWindbgExtensionApis64"),
 #GetNumberEventFilters -> SpecificEvents:PULONG, SpecificExceptions:PULONG, ArbitraryExceptions:PULONG
 "GetNumberEventFilters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG)(81, "GetNumberEventFilters"),
 #GetEventFilterText -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetEventFilterText": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(82, "GetEventFilterText"),
 #GetEventFilterCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(83, "GetEventFilterCommand"),
 #SetEventFilterCommand -> Index:ULONG, Command:PCSTR
 "SetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(84, "SetEventFilterCommand"),
 #GetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "GetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(85, "GetSpecificFilterParameters"),
 #SetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "SetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(86, "SetSpecificFilterParameters"),
 #GetSpecificFilterArgument -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ArgumentSize:PULONG
 "GetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(87, "GetSpecificFilterArgument"),
 #SetSpecificFilterArgument -> Index:ULONG, Argument:PCSTR
 "SetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(88, "SetSpecificFilterArgument"),
 #GetExceptionFilterParameters -> Count:ULONG, Codes:PULONG, Start:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "GetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(89, "GetExceptionFilterParameters"),
 #SetExceptionFilterParameters -> Count:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "SetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(90, "SetExceptionFilterParameters"),
 #GetExceptionFilterSecondCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(91, "GetExceptionFilterSecondCommand"),
 #SetExceptionFilterSecondCommand -> Index:ULONG, Command:PCSTR
 "SetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(92, "SetExceptionFilterSecondCommand"),
 #WaitForEvent -> Flags:ULONG, Timeout:ULONG
 "WaitForEvent": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(93, "WaitForEvent"),
 #GetLastEventInformation -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG, Description:PSTR, DescriptionSize:ULONG, DescriptionUsed:PULONG
 "GetLastEventInformation": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(94, "GetLastEventInformation"),
    }


class IDebugControl2(COMInterface):
    IID = generate_IID(0xD4366723, 0x44DF, 0x4BED, 0x8C, 0x7E, 0x4C, 0x05, 0x42, 0x4F, 0x45, 0x88, name="IDebugControl2", strid="D4366723-44DF-4BED-8C7E-4C05424F4588")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterrupt -> 
 "GetInterrupt": ctypes.WINFUNCTYPE(HRESULT)(3, "GetInterrupt"),
 #SetInterrupt -> Flags:ULONG
 "SetInterrupt": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "SetInterrupt"),
 #GetInterruptTimeout -> Seconds:PULONG
 "GetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetInterruptTimeout"),
 #SetInterruptTimeout -> Seconds:ULONG
 "SetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetInterruptTimeout"),
 #GetLogFile -> Buffer:PSTR, BufferSize:ULONG, FileSize:PULONG, Append:PBOOL
 "GetLogFile": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG, PBOOL)(7, "GetLogFile"),
 #OpenLogFile -> File:PCSTR, Append:BOOL
 "OpenLogFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, BOOL)(8, "OpenLogFile"),
 #CloseLogFile -> 
 "CloseLogFile": ctypes.WINFUNCTYPE(HRESULT)(9, "CloseLogFile"),
 #GetLogMask -> Mask:PULONG
 "GetLogMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(10, "GetLogMask"),
 #SetLogMask -> Mask:ULONG
 "SetLogMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(11, "SetLogMask"),
 #Input -> Buffer:PSTR, BufferSize:ULONG, InputSize:PULONG
 "Input": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(12, "Input"),
 #ReturnInput -> Buffer:PCSTR
 "ReturnInput": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(13, "ReturnInput"),
 #Output -> Mask:ULONG, Format:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(14, "Output"),
 #OutputVaList -> Mask:ULONG, Format:PCSTR, Args:va_list
 "OutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(15, "OutputVaList"),
 #ControlledOutput -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR
 "ControlledOutput": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(16, "ControlledOutput"),
 #ControlledOutputVaList -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR, Args:va_list
 "ControlledOutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR, va_list)(17, "ControlledOutputVaList"),
 #OutputPrompt -> OutputControl:ULONG, Format:PCSTR
 "OutputPrompt": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(18, "OutputPrompt"),
 #OutputPromptVaList -> OutputControl:ULONG, Format:PCSTR, Args:va_list
 "OutputPromptVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(19, "OutputPromptVaList"),
 #GetPromptText -> Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetPromptText": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(20, "GetPromptText"),
 #OutputCurrentState -> OutputControl:ULONG, Flags:ULONG
 "OutputCurrentState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "OutputCurrentState"),
 #OutputVersionInformation -> OutputControl:ULONG
 "OutputVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG)(22, "OutputVersionInformation"),
 #GetNotifyEventHandle -> Handle:PULONG64
 "GetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetNotifyEventHandle"),
 #SetNotifyEventHandle -> Handle:ULONG64
 "SetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(24, "SetNotifyEventHandle"),
 #Assemble -> Offset:ULONG64, Instr:PCSTR, EndOffset:PULONG64
 "Assemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG64)(25, "Assemble"),
 #Disassemble -> Offset:ULONG64, Flags:ULONG, Buffer:PSTR, BufferSize:ULONG, DisassemblySize:PULONG, EndOffset:PULONG64
 "Disassemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG, PULONG64)(26, "Disassemble"),
 #GetDisassembleEffectiveOffset -> Offset:PULONG64
 "GetDisassembleEffectiveOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(27, "GetDisassembleEffectiveOffset"),
 #OutputDisassembly -> OutputControl:ULONG, Offset:ULONG64, Flags:ULONG, EndOffset:PULONG64
 "OutputDisassembly": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PULONG64)(28, "OutputDisassembly"),
 #OutputDisassemblyLines -> OutputControl:ULONG, PreviousLines:ULONG, TotalLines:ULONG, Offset:ULONG64, Flags:ULONG, OffsetLine:PULONG, StartOffset:PULONG64, EndOffset:PULONG64, LineOffsets:PULONG64
 "OutputDisassemblyLines": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, ULONG, PULONG, PULONG64, PULONG64, PULONG64)(29, "OutputDisassemblyLines"),
 #GetNearInstruction -> Offset:ULONG64, Delta:LONG, NearOffset:PULONG64
 "GetNearInstruction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PULONG64)(30, "GetNearInstruction"),
 #GetStackTrace -> FrameOffset:ULONG64, StackOffset:ULONG64, InstructionOffset:ULONG64, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FramesFilled:PULONG
 "GetStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, PDEBUG_STACK_FRAME, ULONG, PULONG)(31, "GetStackTrace"),
 #GetReturnOffset -> Offset:PULONG64
 "GetReturnOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(32, "GetReturnOffset"),
 #OutputStackTrace -> OutputControl:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, Flags:ULONG
 "OutputStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_STACK_FRAME, ULONG, ULONG)(33, "OutputStackTrace"),
 #GetDebuggeeType -> Class:PULONG, Qualifier:PULONG
 "GetDebuggeeType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(34, "GetDebuggeeType"),
 #GetActualProcessorType -> Type:PULONG
 "GetActualProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetActualProcessorType"),
 #GetExecutingProcessorType -> Type:PULONG
 "GetExecutingProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(36, "GetExecutingProcessorType"),
 #GetNumberPossibleExecutingProcessorTypes -> Number:PULONG
 "GetNumberPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetNumberPossibleExecutingProcessorTypes"),
 #GetPossibleExecutingProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(38, "GetPossibleExecutingProcessorTypes"),
 #GetNumberProcessors -> Number:PULONG
 "GetNumberProcessors": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetNumberProcessors"),
 #GetSystemVersion -> PlatformId:PULONG, Major:PULONG, Minor:PULONG, ServicePackString:PSTR, ServicePackStringSize:ULONG, ServicePackStringUsed:PULONG, ServicePackNumber:PULONG, BuildString:PSTR, BuildStringSize:ULONG, BuildStringUsed:PULONG
 "GetSystemVersion": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PSTR, ULONG, PULONG, PULONG, PSTR, ULONG, PULONG)(40, "GetSystemVersion"),
 #GetPageSize -> Size:PULONG
 "GetPageSize": ctypes.WINFUNCTYPE(HRESULT, PULONG)(41, "GetPageSize"),
 #IsPointer64Bit -> 
 "IsPointer64Bit": ctypes.WINFUNCTYPE(HRESULT)(42, "IsPointer64Bit"),
 #ReadBugCheckData -> Code:PULONG, Arg1:PULONG64, Arg2:PULONG64, Arg3:PULONG64, Arg4:PULONG64
 "ReadBugCheckData": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG64, PULONG64, PULONG64, PULONG64)(43, "ReadBugCheckData"),
 #GetNumberSupportedProcessorTypes -> Number:PULONG
 "GetNumberSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(44, "GetNumberSupportedProcessorTypes"),
 #GetSupportedProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(45, "GetSupportedProcessorTypes"),
 #GetProcessorTypeNames -> Type:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetProcessorTypeNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(46, "GetProcessorTypeNames"),
 #GetEffectiveProcessorType -> Type:PULONG
 "GetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(47, "GetEffectiveProcessorType"),
 #SetEffectiveProcessorType -> Type:ULONG
 "SetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, ULONG)(48, "SetEffectiveProcessorType"),
 #GetExecutionStatus -> Status:PULONG
 "GetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG)(49, "GetExecutionStatus"),
 #SetExecutionStatus -> Status:ULONG
 "SetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(50, "SetExecutionStatus"),
 #GetCodeLevel -> Level:PULONG
 "GetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, PULONG)(51, "GetCodeLevel"),
 #SetCodeLevel -> Level:ULONG
 "SetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, ULONG)(52, "SetCodeLevel"),
 #GetEngineOptions -> Options:PULONG
 "GetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(53, "GetEngineOptions"),
 #AddEngineOptions -> Options:ULONG
 "AddEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(54, "AddEngineOptions"),
 #RemoveEngineOptions -> Options:ULONG
 "RemoveEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(55, "RemoveEngineOptions"),
 #SetEngineOptions -> Options:ULONG
 "SetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(56, "SetEngineOptions"),
 #GetSystemErrorControl -> OutputLevel:PULONG, BreakLevel:PULONG
 "GetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(57, "GetSystemErrorControl"),
 #SetSystemErrorControl -> OutputLevel:ULONG, BreakLevel:ULONG
 "SetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(58, "SetSystemErrorControl"),
 #GetTextMacro -> Slot:ULONG, Buffer:PSTR, BufferSize:ULONG, MacroSize:PULONG
 "GetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(59, "GetTextMacro"),
 #SetTextMacro -> Slot:ULONG, Macro:PCSTR
 "SetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(60, "SetTextMacro"),
 #GetRadix -> Radix:PULONG
 "GetRadix": ctypes.WINFUNCTYPE(HRESULT, PULONG)(61, "GetRadix"),
 #SetRadix -> Radix:ULONG
 "SetRadix": ctypes.WINFUNCTYPE(HRESULT, ULONG)(62, "SetRadix"),
 #Evaluate -> Expression:PCSTR, DesiredType:ULONG, Value:PDEBUG_VALUE, RemainderIndex:PULONG
 "Evaluate": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PDEBUG_VALUE, PULONG)(63, "Evaluate"),
 #CoerceValue -> In:PDEBUG_VALUE, OutType:ULONG, Out:PDEBUG_VALUE
 "CoerceValue": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_VALUE, ULONG, PDEBUG_VALUE)(64, "CoerceValue"),
 #CoerceValues -> Count:ULONG, In:PDEBUG_VALUE, OutTypes:PULONG, Out:PDEBUG_VALUE
 "CoerceValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE, PULONG, PDEBUG_VALUE)(65, "CoerceValues"),
 #Execute -> OutputControl:ULONG, Command:PCSTR, Flags:ULONG
 "Execute": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(66, "Execute"),
 #ExecuteCommandFile -> OutputControl:ULONG, CommandFile:PCSTR, Flags:ULONG
 "ExecuteCommandFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(67, "ExecuteCommandFile"),
 #GetNumberBreakpoints -> Number:PULONG
 "GetNumberBreakpoints": ctypes.WINFUNCTYPE(HRESULT, PULONG)(68, "GetNumberBreakpoints"),
 #GetBreakpointByIndex -> Index:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(69, "GetBreakpointByIndex"),
 #GetBreakpointById -> Id:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointById": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(70, "GetBreakpointById"),
 #GetBreakpointParameters -> Count:ULONG, Ids:PULONG, Start:ULONG, Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetBreakpointParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_BREAKPOINT_PARAMETERS)(71, "GetBreakpointParameters"),
 #AddBreakpoint -> Type:ULONG, DesiredId:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "AddBreakpoint": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(72, "AddBreakpoint"),
 #RemoveBreakpoint -> Bp:PDEBUG_BREAKPOINT2
 "RemoveBreakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "RemoveBreakpoint"),
 #AddExtension -> Path:PCSTR, Flags:ULONG, Handle:PULONG64
 "AddExtension": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG64)(74, "AddExtension"),
 #RemoveExtension -> Handle:ULONG64
 "RemoveExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(75, "RemoveExtension"),
 #GetExtensionByPath -> Path:PCSTR, Handle:PULONG64
 "GetExtensionByPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(76, "GetExtensionByPath"),
 #CallExtension -> Handle:ULONG64, Function:PCSTR, Arguments:PCSTR
 "CallExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PCSTR)(77, "CallExtension"),
 #GetExtensionFunction -> Handle:ULONG64, FuncName:PCSTR, Function:*FARPROC
 "GetExtensionFunction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, POINTER(FARPROC))(78, "GetExtensionFunction"),
 #GetWindbgExtensionApis32 -> Api:PWINDBG_EXTENSION_APIS32
 "GetWindbgExtensionApis32": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS32)(79, "GetWindbgExtensionApis32"),
 #GetWindbgExtensionApis64 -> Api:PWINDBG_EXTENSION_APIS64
 "GetWindbgExtensionApis64": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS64)(80, "GetWindbgExtensionApis64"),
 #GetNumberEventFilters -> SpecificEvents:PULONG, SpecificExceptions:PULONG, ArbitraryExceptions:PULONG
 "GetNumberEventFilters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG)(81, "GetNumberEventFilters"),
 #GetEventFilterText -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetEventFilterText": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(82, "GetEventFilterText"),
 #GetEventFilterCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(83, "GetEventFilterCommand"),
 #SetEventFilterCommand -> Index:ULONG, Command:PCSTR
 "SetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(84, "SetEventFilterCommand"),
 #GetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "GetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(85, "GetSpecificFilterParameters"),
 #SetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "SetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(86, "SetSpecificFilterParameters"),
 #GetSpecificFilterArgument -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ArgumentSize:PULONG
 "GetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(87, "GetSpecificFilterArgument"),
 #SetSpecificFilterArgument -> Index:ULONG, Argument:PCSTR
 "SetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(88, "SetSpecificFilterArgument"),
 #GetExceptionFilterParameters -> Count:ULONG, Codes:PULONG, Start:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "GetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(89, "GetExceptionFilterParameters"),
 #SetExceptionFilterParameters -> Count:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "SetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(90, "SetExceptionFilterParameters"),
 #GetExceptionFilterSecondCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(91, "GetExceptionFilterSecondCommand"),
 #SetExceptionFilterSecondCommand -> Index:ULONG, Command:PCSTR
 "SetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(92, "SetExceptionFilterSecondCommand"),
 #WaitForEvent -> Flags:ULONG, Timeout:ULONG
 "WaitForEvent": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(93, "WaitForEvent"),
 #GetLastEventInformation -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG, Description:PSTR, DescriptionSize:ULONG, DescriptionUsed:PULONG
 "GetLastEventInformation": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(94, "GetLastEventInformation"),
 #GetCurrentTimeDate -> TimeDate:PULONG
 "GetCurrentTimeDate": ctypes.WINFUNCTYPE(HRESULT, PULONG)(95, "GetCurrentTimeDate"),
 #GetCurrentSystemUpTime -> UpTime:PULONG
 "GetCurrentSystemUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(96, "GetCurrentSystemUpTime"),
 #GetDumpFormatFlags -> FormatFlags:PULONG
 "GetDumpFormatFlags": ctypes.WINFUNCTYPE(HRESULT, PULONG)(97, "GetDumpFormatFlags"),
 #GetNumberTextReplacements -> NumRepl:PULONG
 "GetNumberTextReplacements": ctypes.WINFUNCTYPE(HRESULT, PULONG)(98, "GetNumberTextReplacements"),
 #GetTextReplacement -> SrcText:PCSTR, Index:ULONG, SrcBuffer:PSTR, SrcBufferSize:ULONG, SrcSize:PULONG, DstBuffer:PSTR, DstBufferSize:ULONG, DstSize:PULONG
 "GetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(99, "GetTextReplacement"),
 #SetTextReplacement -> SrcText:PCSTR, DstText:PCSTR
 "SetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PCSTR)(100, "SetTextReplacement"),
 #RemoveTextReplacements -> 
 "RemoveTextReplacements": ctypes.WINFUNCTYPE(HRESULT)(101, "RemoveTextReplacements"),
 #OutputTextReplacements -> OutputControl:ULONG, Flags:ULONG
 "OutputTextReplacements": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(102, "OutputTextReplacements"),
    }


class IDebugControl3(COMInterface):
    IID = generate_IID(0x7DF74A86, 0xB03F, 0x407F, 0x90, 0xAB, 0xA2, 0x0D, 0xAD, 0xCE, 0xAD, 0x08, name="IDebugControl3", strid="7DF74A86-B03F-407F-90AB-A20DADCEAD08")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterrupt -> 
 "GetInterrupt": ctypes.WINFUNCTYPE(HRESULT)(3, "GetInterrupt"),
 #SetInterrupt -> Flags:ULONG
 "SetInterrupt": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "SetInterrupt"),
 #GetInterruptTimeout -> Seconds:PULONG
 "GetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetInterruptTimeout"),
 #SetInterruptTimeout -> Seconds:ULONG
 "SetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetInterruptTimeout"),
 #GetLogFile -> Buffer:PSTR, BufferSize:ULONG, FileSize:PULONG, Append:PBOOL
 "GetLogFile": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG, PBOOL)(7, "GetLogFile"),
 #OpenLogFile -> File:PCSTR, Append:BOOL
 "OpenLogFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, BOOL)(8, "OpenLogFile"),
 #CloseLogFile -> 
 "CloseLogFile": ctypes.WINFUNCTYPE(HRESULT)(9, "CloseLogFile"),
 #GetLogMask -> Mask:PULONG
 "GetLogMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(10, "GetLogMask"),
 #SetLogMask -> Mask:ULONG
 "SetLogMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(11, "SetLogMask"),
 #Input -> Buffer:PSTR, BufferSize:ULONG, InputSize:PULONG
 "Input": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(12, "Input"),
 #ReturnInput -> Buffer:PCSTR
 "ReturnInput": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(13, "ReturnInput"),
 #Output -> Mask:ULONG, Format:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(14, "Output"),
 #OutputVaList -> Mask:ULONG, Format:PCSTR, Args:va_list
 "OutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(15, "OutputVaList"),
 #ControlledOutput -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR
 "ControlledOutput": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(16, "ControlledOutput"),
 #ControlledOutputVaList -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR, Args:va_list
 "ControlledOutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR, va_list)(17, "ControlledOutputVaList"),
 #OutputPrompt -> OutputControl:ULONG, Format:PCSTR
 "OutputPrompt": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(18, "OutputPrompt"),
 #OutputPromptVaList -> OutputControl:ULONG, Format:PCSTR, Args:va_list
 "OutputPromptVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(19, "OutputPromptVaList"),
 #GetPromptText -> Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetPromptText": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(20, "GetPromptText"),
 #OutputCurrentState -> OutputControl:ULONG, Flags:ULONG
 "OutputCurrentState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "OutputCurrentState"),
 #OutputVersionInformation -> OutputControl:ULONG
 "OutputVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG)(22, "OutputVersionInformation"),
 #GetNotifyEventHandle -> Handle:PULONG64
 "GetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetNotifyEventHandle"),
 #SetNotifyEventHandle -> Handle:ULONG64
 "SetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(24, "SetNotifyEventHandle"),
 #Assemble -> Offset:ULONG64, Instr:PCSTR, EndOffset:PULONG64
 "Assemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG64)(25, "Assemble"),
 #Disassemble -> Offset:ULONG64, Flags:ULONG, Buffer:PSTR, BufferSize:ULONG, DisassemblySize:PULONG, EndOffset:PULONG64
 "Disassemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG, PULONG64)(26, "Disassemble"),
 #GetDisassembleEffectiveOffset -> Offset:PULONG64
 "GetDisassembleEffectiveOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(27, "GetDisassembleEffectiveOffset"),
 #OutputDisassembly -> OutputControl:ULONG, Offset:ULONG64, Flags:ULONG, EndOffset:PULONG64
 "OutputDisassembly": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PULONG64)(28, "OutputDisassembly"),
 #OutputDisassemblyLines -> OutputControl:ULONG, PreviousLines:ULONG, TotalLines:ULONG, Offset:ULONG64, Flags:ULONG, OffsetLine:PULONG, StartOffset:PULONG64, EndOffset:PULONG64, LineOffsets:PULONG64
 "OutputDisassemblyLines": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, ULONG, PULONG, PULONG64, PULONG64, PULONG64)(29, "OutputDisassemblyLines"),
 #GetNearInstruction -> Offset:ULONG64, Delta:LONG, NearOffset:PULONG64
 "GetNearInstruction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PULONG64)(30, "GetNearInstruction"),
 #GetStackTrace -> FrameOffset:ULONG64, StackOffset:ULONG64, InstructionOffset:ULONG64, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FramesFilled:PULONG
 "GetStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, PDEBUG_STACK_FRAME, ULONG, PULONG)(31, "GetStackTrace"),
 #GetReturnOffset -> Offset:PULONG64
 "GetReturnOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(32, "GetReturnOffset"),
 #OutputStackTrace -> OutputControl:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, Flags:ULONG
 "OutputStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_STACK_FRAME, ULONG, ULONG)(33, "OutputStackTrace"),
 #GetDebuggeeType -> Class:PULONG, Qualifier:PULONG
 "GetDebuggeeType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(34, "GetDebuggeeType"),
 #GetActualProcessorType -> Type:PULONG
 "GetActualProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetActualProcessorType"),
 #GetExecutingProcessorType -> Type:PULONG
 "GetExecutingProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(36, "GetExecutingProcessorType"),
 #GetNumberPossibleExecutingProcessorTypes -> Number:PULONG
 "GetNumberPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetNumberPossibleExecutingProcessorTypes"),
 #GetPossibleExecutingProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(38, "GetPossibleExecutingProcessorTypes"),
 #GetNumberProcessors -> Number:PULONG
 "GetNumberProcessors": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetNumberProcessors"),
 #GetSystemVersion -> PlatformId:PULONG, Major:PULONG, Minor:PULONG, ServicePackString:PSTR, ServicePackStringSize:ULONG, ServicePackStringUsed:PULONG, ServicePackNumber:PULONG, BuildString:PSTR, BuildStringSize:ULONG, BuildStringUsed:PULONG
 "GetSystemVersion": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PSTR, ULONG, PULONG, PULONG, PSTR, ULONG, PULONG)(40, "GetSystemVersion"),
 #GetPageSize -> Size:PULONG
 "GetPageSize": ctypes.WINFUNCTYPE(HRESULT, PULONG)(41, "GetPageSize"),
 #IsPointer64Bit -> 
 "IsPointer64Bit": ctypes.WINFUNCTYPE(HRESULT)(42, "IsPointer64Bit"),
 #ReadBugCheckData -> Code:PULONG, Arg1:PULONG64, Arg2:PULONG64, Arg3:PULONG64, Arg4:PULONG64
 "ReadBugCheckData": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG64, PULONG64, PULONG64, PULONG64)(43, "ReadBugCheckData"),
 #GetNumberSupportedProcessorTypes -> Number:PULONG
 "GetNumberSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(44, "GetNumberSupportedProcessorTypes"),
 #GetSupportedProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(45, "GetSupportedProcessorTypes"),
 #GetProcessorTypeNames -> Type:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetProcessorTypeNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(46, "GetProcessorTypeNames"),
 #GetEffectiveProcessorType -> Type:PULONG
 "GetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(47, "GetEffectiveProcessorType"),
 #SetEffectiveProcessorType -> Type:ULONG
 "SetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, ULONG)(48, "SetEffectiveProcessorType"),
 #GetExecutionStatus -> Status:PULONG
 "GetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG)(49, "GetExecutionStatus"),
 #SetExecutionStatus -> Status:ULONG
 "SetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(50, "SetExecutionStatus"),
 #GetCodeLevel -> Level:PULONG
 "GetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, PULONG)(51, "GetCodeLevel"),
 #SetCodeLevel -> Level:ULONG
 "SetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, ULONG)(52, "SetCodeLevel"),
 #GetEngineOptions -> Options:PULONG
 "GetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(53, "GetEngineOptions"),
 #AddEngineOptions -> Options:ULONG
 "AddEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(54, "AddEngineOptions"),
 #RemoveEngineOptions -> Options:ULONG
 "RemoveEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(55, "RemoveEngineOptions"),
 #SetEngineOptions -> Options:ULONG
 "SetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(56, "SetEngineOptions"),
 #GetSystemErrorControl -> OutputLevel:PULONG, BreakLevel:PULONG
 "GetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(57, "GetSystemErrorControl"),
 #SetSystemErrorControl -> OutputLevel:ULONG, BreakLevel:ULONG
 "SetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(58, "SetSystemErrorControl"),
 #GetTextMacro -> Slot:ULONG, Buffer:PSTR, BufferSize:ULONG, MacroSize:PULONG
 "GetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(59, "GetTextMacro"),
 #SetTextMacro -> Slot:ULONG, Macro:PCSTR
 "SetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(60, "SetTextMacro"),
 #GetRadix -> Radix:PULONG
 "GetRadix": ctypes.WINFUNCTYPE(HRESULT, PULONG)(61, "GetRadix"),
 #SetRadix -> Radix:ULONG
 "SetRadix": ctypes.WINFUNCTYPE(HRESULT, ULONG)(62, "SetRadix"),
 #Evaluate -> Expression:PCSTR, DesiredType:ULONG, Value:PDEBUG_VALUE, RemainderIndex:PULONG
 "Evaluate": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PDEBUG_VALUE, PULONG)(63, "Evaluate"),
 #CoerceValue -> In:PDEBUG_VALUE, OutType:ULONG, Out:PDEBUG_VALUE
 "CoerceValue": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_VALUE, ULONG, PDEBUG_VALUE)(64, "CoerceValue"),
 #CoerceValues -> Count:ULONG, In:PDEBUG_VALUE, OutTypes:PULONG, Out:PDEBUG_VALUE
 "CoerceValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE, PULONG, PDEBUG_VALUE)(65, "CoerceValues"),
 #Execute -> OutputControl:ULONG, Command:PCSTR, Flags:ULONG
 "Execute": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(66, "Execute"),
 #ExecuteCommandFile -> OutputControl:ULONG, CommandFile:PCSTR, Flags:ULONG
 "ExecuteCommandFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(67, "ExecuteCommandFile"),
 #GetNumberBreakpoints -> Number:PULONG
 "GetNumberBreakpoints": ctypes.WINFUNCTYPE(HRESULT, PULONG)(68, "GetNumberBreakpoints"),
 #GetBreakpointByIndex -> Index:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(69, "GetBreakpointByIndex"),
 #GetBreakpointById -> Id:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointById": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(70, "GetBreakpointById"),
 #GetBreakpointParameters -> Count:ULONG, Ids:PULONG, Start:ULONG, Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetBreakpointParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_BREAKPOINT_PARAMETERS)(71, "GetBreakpointParameters"),
 #AddBreakpoint -> Type:ULONG, DesiredId:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "AddBreakpoint": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(72, "AddBreakpoint"),
 #RemoveBreakpoint -> Bp:PDEBUG_BREAKPOINT2
 "RemoveBreakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "RemoveBreakpoint"),
 #AddExtension -> Path:PCSTR, Flags:ULONG, Handle:PULONG64
 "AddExtension": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG64)(74, "AddExtension"),
 #RemoveExtension -> Handle:ULONG64
 "RemoveExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(75, "RemoveExtension"),
 #GetExtensionByPath -> Path:PCSTR, Handle:PULONG64
 "GetExtensionByPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(76, "GetExtensionByPath"),
 #CallExtension -> Handle:ULONG64, Function:PCSTR, Arguments:PCSTR
 "CallExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PCSTR)(77, "CallExtension"),
 #GetExtensionFunction -> Handle:ULONG64, FuncName:PCSTR, Function:*FARPROC
 "GetExtensionFunction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, POINTER(FARPROC))(78, "GetExtensionFunction"),
 #GetWindbgExtensionApis32 -> Api:PWINDBG_EXTENSION_APIS32
 "GetWindbgExtensionApis32": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS32)(79, "GetWindbgExtensionApis32"),
 #GetWindbgExtensionApis64 -> Api:PWINDBG_EXTENSION_APIS64
 "GetWindbgExtensionApis64": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS64)(80, "GetWindbgExtensionApis64"),
 #GetNumberEventFilters -> SpecificEvents:PULONG, SpecificExceptions:PULONG, ArbitraryExceptions:PULONG
 "GetNumberEventFilters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG)(81, "GetNumberEventFilters"),
 #GetEventFilterText -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetEventFilterText": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(82, "GetEventFilterText"),
 #GetEventFilterCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(83, "GetEventFilterCommand"),
 #SetEventFilterCommand -> Index:ULONG, Command:PCSTR
 "SetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(84, "SetEventFilterCommand"),
 #GetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "GetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(85, "GetSpecificFilterParameters"),
 #SetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "SetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(86, "SetSpecificFilterParameters"),
 #GetSpecificFilterArgument -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ArgumentSize:PULONG
 "GetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(87, "GetSpecificFilterArgument"),
 #SetSpecificFilterArgument -> Index:ULONG, Argument:PCSTR
 "SetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(88, "SetSpecificFilterArgument"),
 #GetExceptionFilterParameters -> Count:ULONG, Codes:PULONG, Start:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "GetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(89, "GetExceptionFilterParameters"),
 #SetExceptionFilterParameters -> Count:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "SetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(90, "SetExceptionFilterParameters"),
 #GetExceptionFilterSecondCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(91, "GetExceptionFilterSecondCommand"),
 #SetExceptionFilterSecondCommand -> Index:ULONG, Command:PCSTR
 "SetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(92, "SetExceptionFilterSecondCommand"),
 #WaitForEvent -> Flags:ULONG, Timeout:ULONG
 "WaitForEvent": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(93, "WaitForEvent"),
 #GetLastEventInformation -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG, Description:PSTR, DescriptionSize:ULONG, DescriptionUsed:PULONG
 "GetLastEventInformation": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(94, "GetLastEventInformation"),
 #GetCurrentTimeDate -> TimeDate:PULONG
 "GetCurrentTimeDate": ctypes.WINFUNCTYPE(HRESULT, PULONG)(95, "GetCurrentTimeDate"),
 #GetCurrentSystemUpTime -> UpTime:PULONG
 "GetCurrentSystemUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(96, "GetCurrentSystemUpTime"),
 #GetDumpFormatFlags -> FormatFlags:PULONG
 "GetDumpFormatFlags": ctypes.WINFUNCTYPE(HRESULT, PULONG)(97, "GetDumpFormatFlags"),
 #GetNumberTextReplacements -> NumRepl:PULONG
 "GetNumberTextReplacements": ctypes.WINFUNCTYPE(HRESULT, PULONG)(98, "GetNumberTextReplacements"),
 #GetTextReplacement -> SrcText:PCSTR, Index:ULONG, SrcBuffer:PSTR, SrcBufferSize:ULONG, SrcSize:PULONG, DstBuffer:PSTR, DstBufferSize:ULONG, DstSize:PULONG
 "GetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(99, "GetTextReplacement"),
 #SetTextReplacement -> SrcText:PCSTR, DstText:PCSTR
 "SetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PCSTR)(100, "SetTextReplacement"),
 #RemoveTextReplacements -> 
 "RemoveTextReplacements": ctypes.WINFUNCTYPE(HRESULT)(101, "RemoveTextReplacements"),
 #OutputTextReplacements -> OutputControl:ULONG, Flags:ULONG
 "OutputTextReplacements": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(102, "OutputTextReplacements"),
 #GetAssemblyOptions -> Options:PULONG
 "GetAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(103, "GetAssemblyOptions"),
 #AddAssemblyOptions -> Options:ULONG
 "AddAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(104, "AddAssemblyOptions"),
 #RemoveAssemblyOptions -> Options:ULONG
 "RemoveAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(105, "RemoveAssemblyOptions"),
 #SetAssemblyOptions -> Options:ULONG
 "SetAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(106, "SetAssemblyOptions"),
 #GetExpressionSyntax -> Flags:PULONG
 "GetExpressionSyntax": ctypes.WINFUNCTYPE(HRESULT, PULONG)(107, "GetExpressionSyntax"),
 #SetExpressionSyntax -> Flags:ULONG
 "SetExpressionSyntax": ctypes.WINFUNCTYPE(HRESULT, ULONG)(108, "SetExpressionSyntax"),
 #SetExpressionSyntaxByName -> AbbrevName:PCSTR
 "SetExpressionSyntaxByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(109, "SetExpressionSyntaxByName"),
 #GetNumberExpressionSyntaxes -> Number:PULONG
 "GetNumberExpressionSyntaxes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(110, "GetNumberExpressionSyntaxes"),
 #GetExpressionSyntaxNames -> Index:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetExpressionSyntaxNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(111, "GetExpressionSyntaxNames"),
 #GetNumberEvents -> Events:PULONG
 "GetNumberEvents": ctypes.WINFUNCTYPE(HRESULT, PULONG)(112, "GetNumberEvents"),
 #GetEventIndexDescription -> Index:ULONG, Which:ULONG, Buffer:PSTR, BufferSize:ULONG, DescSize:PULONG
 "GetEventIndexDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PSTR, ULONG, PULONG)(113, "GetEventIndexDescription"),
 #GetCurrentEventIndex -> Index:PULONG
 "GetCurrentEventIndex": ctypes.WINFUNCTYPE(HRESULT, PULONG)(114, "GetCurrentEventIndex"),
 #SetNextEventIndex -> Relation:ULONG, Value:ULONG, NextIndex:PULONG
 "SetNextEventIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(115, "SetNextEventIndex"),
    }


class IDebugControl4(COMInterface):
    IID = generate_IID(0x94E60CE9, 0x9B41, 0x4B19, 0x9F, 0xC0, 0x6D, 0x9E, 0xB3, 0x52, 0x72, 0xB3, name="IDebugControl4", strid="94E60CE9-9B41-4B19-9FC0-6D9EB35272B3")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterrupt -> 
 "GetInterrupt": ctypes.WINFUNCTYPE(HRESULT)(3, "GetInterrupt"),
 #SetInterrupt -> Flags:ULONG
 "SetInterrupt": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "SetInterrupt"),
 #GetInterruptTimeout -> Seconds:PULONG
 "GetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetInterruptTimeout"),
 #SetInterruptTimeout -> Seconds:ULONG
 "SetInterruptTimeout": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetInterruptTimeout"),
 #GetLogFile -> Buffer:PSTR, BufferSize:ULONG, FileSize:PULONG, Append:PBOOL
 "GetLogFile": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG, PBOOL)(7, "GetLogFile"),
 #OpenLogFile -> File:PCSTR, Append:BOOL
 "OpenLogFile": ctypes.WINFUNCTYPE(HRESULT, PCSTR, BOOL)(8, "OpenLogFile"),
 #CloseLogFile -> 
 "CloseLogFile": ctypes.WINFUNCTYPE(HRESULT)(9, "CloseLogFile"),
 #GetLogMask -> Mask:PULONG
 "GetLogMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(10, "GetLogMask"),
 #SetLogMask -> Mask:ULONG
 "SetLogMask": ctypes.WINFUNCTYPE(HRESULT, ULONG)(11, "SetLogMask"),
 #Input -> Buffer:PSTR, BufferSize:ULONG, InputSize:PULONG
 "Input": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(12, "Input"),
 #ReturnInput -> Buffer:PCSTR
 "ReturnInput": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(13, "ReturnInput"),
 #Output -> Mask:ULONG, Format:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(14, "Output"),
 #OutputVaList -> Mask:ULONG, Format:PCSTR, Args:va_list
 "OutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(15, "OutputVaList"),
 #ControlledOutput -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR
 "ControlledOutput": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR)(16, "ControlledOutput"),
 #ControlledOutputVaList -> OutputControl:ULONG, Mask:ULONG, Format:PCSTR, Args:va_list
 "ControlledOutputVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCSTR, va_list)(17, "ControlledOutputVaList"),
 #OutputPrompt -> OutputControl:ULONG, Format:PCSTR
 "OutputPrompt": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(18, "OutputPrompt"),
 #OutputPromptVaList -> OutputControl:ULONG, Format:PCSTR, Args:va_list
 "OutputPromptVaList": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, va_list)(19, "OutputPromptVaList"),
 #GetPromptText -> Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetPromptText": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(20, "GetPromptText"),
 #OutputCurrentState -> OutputControl:ULONG, Flags:ULONG
 "OutputCurrentState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(21, "OutputCurrentState"),
 #OutputVersionInformation -> OutputControl:ULONG
 "OutputVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG)(22, "OutputVersionInformation"),
 #GetNotifyEventHandle -> Handle:PULONG64
 "GetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetNotifyEventHandle"),
 #SetNotifyEventHandle -> Handle:ULONG64
 "SetNotifyEventHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(24, "SetNotifyEventHandle"),
 #Assemble -> Offset:ULONG64, Instr:PCSTR, EndOffset:PULONG64
 "Assemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG64)(25, "Assemble"),
 #Disassemble -> Offset:ULONG64, Flags:ULONG, Buffer:PSTR, BufferSize:ULONG, DisassemblySize:PULONG, EndOffset:PULONG64
 "Disassemble": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG, PULONG64)(26, "Disassemble"),
 #GetDisassembleEffectiveOffset -> Offset:PULONG64
 "GetDisassembleEffectiveOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(27, "GetDisassembleEffectiveOffset"),
 #OutputDisassembly -> OutputControl:ULONG, Offset:ULONG64, Flags:ULONG, EndOffset:PULONG64
 "OutputDisassembly": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG, PULONG64)(28, "OutputDisassembly"),
 #OutputDisassemblyLines -> OutputControl:ULONG, PreviousLines:ULONG, TotalLines:ULONG, Offset:ULONG64, Flags:ULONG, OffsetLine:PULONG, StartOffset:PULONG64, EndOffset:PULONG64, LineOffsets:PULONG64
 "OutputDisassemblyLines": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, ULONG, PULONG, PULONG64, PULONG64, PULONG64)(29, "OutputDisassemblyLines"),
 #GetNearInstruction -> Offset:ULONG64, Delta:LONG, NearOffset:PULONG64
 "GetNearInstruction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PULONG64)(30, "GetNearInstruction"),
 #GetStackTrace -> FrameOffset:ULONG64, StackOffset:ULONG64, InstructionOffset:ULONG64, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FramesFilled:PULONG
 "GetStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, PDEBUG_STACK_FRAME, ULONG, PULONG)(31, "GetStackTrace"),
 #GetReturnOffset -> Offset:PULONG64
 "GetReturnOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(32, "GetReturnOffset"),
 #OutputStackTrace -> OutputControl:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, Flags:ULONG
 "OutputStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_STACK_FRAME, ULONG, ULONG)(33, "OutputStackTrace"),
 #GetDebuggeeType -> Class:PULONG, Qualifier:PULONG
 "GetDebuggeeType": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(34, "GetDebuggeeType"),
 #GetActualProcessorType -> Type:PULONG
 "GetActualProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(35, "GetActualProcessorType"),
 #GetExecutingProcessorType -> Type:PULONG
 "GetExecutingProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(36, "GetExecutingProcessorType"),
 #GetNumberPossibleExecutingProcessorTypes -> Number:PULONG
 "GetNumberPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetNumberPossibleExecutingProcessorTypes"),
 #GetPossibleExecutingProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetPossibleExecutingProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(38, "GetPossibleExecutingProcessorTypes"),
 #GetNumberProcessors -> Number:PULONG
 "GetNumberProcessors": ctypes.WINFUNCTYPE(HRESULT, PULONG)(39, "GetNumberProcessors"),
 #GetSystemVersion -> PlatformId:PULONG, Major:PULONG, Minor:PULONG, ServicePackString:PSTR, ServicePackStringSize:ULONG, ServicePackStringUsed:PULONG, ServicePackNumber:PULONG, BuildString:PSTR, BuildStringSize:ULONG, BuildStringUsed:PULONG
 "GetSystemVersion": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PSTR, ULONG, PULONG, PULONG, PSTR, ULONG, PULONG)(40, "GetSystemVersion"),
 #GetPageSize -> Size:PULONG
 "GetPageSize": ctypes.WINFUNCTYPE(HRESULT, PULONG)(41, "GetPageSize"),
 #IsPointer64Bit -> 
 "IsPointer64Bit": ctypes.WINFUNCTYPE(HRESULT)(42, "IsPointer64Bit"),
 #ReadBugCheckData -> Code:PULONG, Arg1:PULONG64, Arg2:PULONG64, Arg3:PULONG64, Arg4:PULONG64
 "ReadBugCheckData": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG64, PULONG64, PULONG64, PULONG64)(43, "ReadBugCheckData"),
 #GetNumberSupportedProcessorTypes -> Number:PULONG
 "GetNumberSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(44, "GetNumberSupportedProcessorTypes"),
 #GetSupportedProcessorTypes -> Start:ULONG, Count:ULONG, Types:PULONG
 "GetSupportedProcessorTypes": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(45, "GetSupportedProcessorTypes"),
 #GetProcessorTypeNames -> Type:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetProcessorTypeNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(46, "GetProcessorTypeNames"),
 #GetEffectiveProcessorType -> Type:PULONG
 "GetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, PULONG)(47, "GetEffectiveProcessorType"),
 #SetEffectiveProcessorType -> Type:ULONG
 "SetEffectiveProcessorType": ctypes.WINFUNCTYPE(HRESULT, ULONG)(48, "SetEffectiveProcessorType"),
 #GetExecutionStatus -> Status:PULONG
 "GetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG)(49, "GetExecutionStatus"),
 #SetExecutionStatus -> Status:ULONG
 "SetExecutionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(50, "SetExecutionStatus"),
 #GetCodeLevel -> Level:PULONG
 "GetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, PULONG)(51, "GetCodeLevel"),
 #SetCodeLevel -> Level:ULONG
 "SetCodeLevel": ctypes.WINFUNCTYPE(HRESULT, ULONG)(52, "SetCodeLevel"),
 #GetEngineOptions -> Options:PULONG
 "GetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(53, "GetEngineOptions"),
 #AddEngineOptions -> Options:ULONG
 "AddEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(54, "AddEngineOptions"),
 #RemoveEngineOptions -> Options:ULONG
 "RemoveEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(55, "RemoveEngineOptions"),
 #SetEngineOptions -> Options:ULONG
 "SetEngineOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(56, "SetEngineOptions"),
 #GetSystemErrorControl -> OutputLevel:PULONG, BreakLevel:PULONG
 "GetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(57, "GetSystemErrorControl"),
 #SetSystemErrorControl -> OutputLevel:ULONG, BreakLevel:ULONG
 "SetSystemErrorControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(58, "SetSystemErrorControl"),
 #GetTextMacro -> Slot:ULONG, Buffer:PSTR, BufferSize:ULONG, MacroSize:PULONG
 "GetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(59, "GetTextMacro"),
 #SetTextMacro -> Slot:ULONG, Macro:PCSTR
 "SetTextMacro": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(60, "SetTextMacro"),
 #GetRadix -> Radix:PULONG
 "GetRadix": ctypes.WINFUNCTYPE(HRESULT, PULONG)(61, "GetRadix"),
 #SetRadix -> Radix:ULONG
 "SetRadix": ctypes.WINFUNCTYPE(HRESULT, ULONG)(62, "SetRadix"),
 #Evaluate -> Expression:PCSTR, DesiredType:ULONG, Value:PDEBUG_VALUE, RemainderIndex:PULONG
 "Evaluate": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PDEBUG_VALUE, PULONG)(63, "Evaluate"),
 #CoerceValue -> In:PDEBUG_VALUE, OutType:ULONG, Out:PDEBUG_VALUE
 "CoerceValue": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_VALUE, ULONG, PDEBUG_VALUE)(64, "CoerceValue"),
 #CoerceValues -> Count:ULONG, In:PDEBUG_VALUE, OutTypes:PULONG, Out:PDEBUG_VALUE
 "CoerceValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE, PULONG, PDEBUG_VALUE)(65, "CoerceValues"),
 #Execute -> OutputControl:ULONG, Command:PCSTR, Flags:ULONG
 "Execute": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(66, "Execute"),
 #ExecuteCommandFile -> OutputControl:ULONG, CommandFile:PCSTR, Flags:ULONG
 "ExecuteCommandFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG)(67, "ExecuteCommandFile"),
 #GetNumberBreakpoints -> Number:PULONG
 "GetNumberBreakpoints": ctypes.WINFUNCTYPE(HRESULT, PULONG)(68, "GetNumberBreakpoints"),
 #GetBreakpointByIndex -> Index:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(69, "GetBreakpointByIndex"),
 #GetBreakpointById -> Id:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointById": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(70, "GetBreakpointById"),
 #GetBreakpointParameters -> Count:ULONG, Ids:PULONG, Start:ULONG, Params:PDEBUG_BREAKPOINT_PARAMETERS
 "GetBreakpointParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_BREAKPOINT_PARAMETERS)(71, "GetBreakpointParameters"),
 #AddBreakpoint -> Type:ULONG, DesiredId:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "AddBreakpoint": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(72, "AddBreakpoint"),
 #RemoveBreakpoint -> Bp:PDEBUG_BREAKPOINT2
 "RemoveBreakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(73, "RemoveBreakpoint"),
 #AddExtension -> Path:PCSTR, Flags:ULONG, Handle:PULONG64
 "AddExtension": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG64)(74, "AddExtension"),
 #RemoveExtension -> Handle:ULONG64
 "RemoveExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(75, "RemoveExtension"),
 #GetExtensionByPath -> Path:PCSTR, Handle:PULONG64
 "GetExtensionByPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(76, "GetExtensionByPath"),
 #CallExtension -> Handle:ULONG64, Function:PCSTR, Arguments:PCSTR
 "CallExtension": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PCSTR)(77, "CallExtension"),
 #GetExtensionFunction -> Handle:ULONG64, FuncName:PCSTR, Function:*FARPROC
 "GetExtensionFunction": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, POINTER(FARPROC))(78, "GetExtensionFunction"),
 #GetWindbgExtensionApis32 -> Api:PWINDBG_EXTENSION_APIS32
 "GetWindbgExtensionApis32": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS32)(79, "GetWindbgExtensionApis32"),
 #GetWindbgExtensionApis64 -> Api:PWINDBG_EXTENSION_APIS64
 "GetWindbgExtensionApis64": ctypes.WINFUNCTYPE(HRESULT, PWINDBG_EXTENSION_APIS64)(80, "GetWindbgExtensionApis64"),
 #GetNumberEventFilters -> SpecificEvents:PULONG, SpecificExceptions:PULONG, ArbitraryExceptions:PULONG
 "GetNumberEventFilters": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG)(81, "GetNumberEventFilters"),
 #GetEventFilterText -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, TextSize:PULONG
 "GetEventFilterText": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(82, "GetEventFilterText"),
 #GetEventFilterCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(83, "GetEventFilterCommand"),
 #SetEventFilterCommand -> Index:ULONG, Command:PCSTR
 "SetEventFilterCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(84, "SetEventFilterCommand"),
 #GetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "GetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(85, "GetSpecificFilterParameters"),
 #SetSpecificFilterParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SPECIFIC_FILTER_PARAMETERS
 "SetSpecificFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SPECIFIC_FILTER_PARAMETERS)(86, "SetSpecificFilterParameters"),
 #GetSpecificFilterArgument -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ArgumentSize:PULONG
 "GetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(87, "GetSpecificFilterArgument"),
 #SetSpecificFilterArgument -> Index:ULONG, Argument:PCSTR
 "SetSpecificFilterArgument": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(88, "SetSpecificFilterArgument"),
 #GetExceptionFilterParameters -> Count:ULONG, Codes:PULONG, Start:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "GetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(89, "GetExceptionFilterParameters"),
 #SetExceptionFilterParameters -> Count:ULONG, Params:PDEBUG_EXCEPTION_FILTER_PARAMETERS
 "SetExceptionFilterParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_EXCEPTION_FILTER_PARAMETERS)(90, "SetExceptionFilterParameters"),
 #GetExceptionFilterSecondCommand -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(91, "GetExceptionFilterSecondCommand"),
 #SetExceptionFilterSecondCommand -> Index:ULONG, Command:PCSTR
 "SetExceptionFilterSecondCommand": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(92, "SetExceptionFilterSecondCommand"),
 #WaitForEvent -> Flags:ULONG, Timeout:ULONG
 "WaitForEvent": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(93, "WaitForEvent"),
 #GetLastEventInformation -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG, Description:PSTR, DescriptionSize:ULONG, DescriptionUsed:PULONG
 "GetLastEventInformation": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PSTR, ULONG, PULONG)(94, "GetLastEventInformation"),
 #GetCurrentTimeDate -> TimeDate:PULONG
 "GetCurrentTimeDate": ctypes.WINFUNCTYPE(HRESULT, PULONG)(95, "GetCurrentTimeDate"),
 #GetCurrentSystemUpTime -> UpTime:PULONG
 "GetCurrentSystemUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(96, "GetCurrentSystemUpTime"),
 #GetDumpFormatFlags -> FormatFlags:PULONG
 "GetDumpFormatFlags": ctypes.WINFUNCTYPE(HRESULT, PULONG)(97, "GetDumpFormatFlags"),
 #GetNumberTextReplacements -> NumRepl:PULONG
 "GetNumberTextReplacements": ctypes.WINFUNCTYPE(HRESULT, PULONG)(98, "GetNumberTextReplacements"),
 #GetTextReplacement -> SrcText:PCSTR, Index:ULONG, SrcBuffer:PSTR, SrcBufferSize:ULONG, SrcSize:PULONG, DstBuffer:PSTR, DstBufferSize:ULONG, DstSize:PULONG
 "GetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(99, "GetTextReplacement"),
 #SetTextReplacement -> SrcText:PCSTR, DstText:PCSTR
 "SetTextReplacement": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PCSTR)(100, "SetTextReplacement"),
 #RemoveTextReplacements -> 
 "RemoveTextReplacements": ctypes.WINFUNCTYPE(HRESULT)(101, "RemoveTextReplacements"),
 #OutputTextReplacements -> OutputControl:ULONG, Flags:ULONG
 "OutputTextReplacements": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(102, "OutputTextReplacements"),
 #GetAssemblyOptions -> Options:PULONG
 "GetAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(103, "GetAssemblyOptions"),
 #AddAssemblyOptions -> Options:ULONG
 "AddAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(104, "AddAssemblyOptions"),
 #RemoveAssemblyOptions -> Options:ULONG
 "RemoveAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(105, "RemoveAssemblyOptions"),
 #SetAssemblyOptions -> Options:ULONG
 "SetAssemblyOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(106, "SetAssemblyOptions"),
 #GetExpressionSyntax -> Flags:PULONG
 "GetExpressionSyntax": ctypes.WINFUNCTYPE(HRESULT, PULONG)(107, "GetExpressionSyntax"),
 #SetExpressionSyntax -> Flags:ULONG
 "SetExpressionSyntax": ctypes.WINFUNCTYPE(HRESULT, ULONG)(108, "SetExpressionSyntax"),
 #SetExpressionSyntaxByName -> AbbrevName:PCSTR
 "SetExpressionSyntaxByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(109, "SetExpressionSyntaxByName"),
 #GetNumberExpressionSyntaxes -> Number:PULONG
 "GetNumberExpressionSyntaxes": ctypes.WINFUNCTYPE(HRESULT, PULONG)(110, "GetNumberExpressionSyntaxes"),
 #GetExpressionSyntaxNames -> Index:ULONG, FullNameBuffer:PSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetExpressionSyntaxNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(111, "GetExpressionSyntaxNames"),
 #GetNumberEvents -> Events:PULONG
 "GetNumberEvents": ctypes.WINFUNCTYPE(HRESULT, PULONG)(112, "GetNumberEvents"),
 #GetEventIndexDescription -> Index:ULONG, Which:ULONG, Buffer:PSTR, BufferSize:ULONG, DescSize:PULONG
 "GetEventIndexDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PSTR, ULONG, PULONG)(113, "GetEventIndexDescription"),
 #GetCurrentEventIndex -> Index:PULONG
 "GetCurrentEventIndex": ctypes.WINFUNCTYPE(HRESULT, PULONG)(114, "GetCurrentEventIndex"),
 #SetNextEventIndex -> Relation:ULONG, Value:ULONG, NextIndex:PULONG
 "SetNextEventIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(115, "SetNextEventIndex"),
 #GetLogFileWide -> Buffer:PWSTR, BufferSize:ULONG, FileSize:PULONG, Append:PBOOL
 "GetLogFileWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG, PBOOL)(116, "GetLogFileWide"),
 #OpenLogFileWide -> File:PCWSTR, Append:BOOL
 "OpenLogFileWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, BOOL)(117, "OpenLogFileWide"),
 #InputWide -> Buffer:PWSTR, BufferSize:ULONG, InputSize:PULONG
 "InputWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(118, "InputWide"),
 #ReturnInputWide -> Buffer:PCWSTR
 "ReturnInputWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(119, "ReturnInputWide"),
 #OutputWide -> Mask:ULONG, Format:PCWSTR
 "OutputWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(120, "OutputWide"),
 #OutputVaListWide -> Mask:ULONG, Format:PCWSTR, Args:va_list
 "OutputVaListWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, va_list)(121, "OutputVaListWide"),
 #ControlledOutputWide -> OutputControl:ULONG, Mask:ULONG, Format:PCWSTR
 "ControlledOutputWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCWSTR)(122, "ControlledOutputWide"),
 #ControlledOutputVaListWide -> OutputControl:ULONG, Mask:ULONG, Format:PCWSTR, Args:va_list
 "ControlledOutputVaListWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PCWSTR, va_list)(123, "ControlledOutputVaListWide"),
 #OutputPromptWide -> OutputControl:ULONG, Format:PCWSTR
 "OutputPromptWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(124, "OutputPromptWide"),
 #OutputPromptVaListWide -> OutputControl:ULONG, Format:PCWSTR, Args:va_list
 "OutputPromptVaListWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, va_list)(125, "OutputPromptVaListWide"),
 #GetPromptTextWide -> Buffer:PWSTR, BufferSize:ULONG, TextSize:PULONG
 "GetPromptTextWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(126, "GetPromptTextWide"),
 #AssembleWide -> Offset:ULONG64, Instr:PCWSTR, EndOffset:PULONG64
 "AssembleWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, PULONG64)(127, "AssembleWide"),
 #DisassembleWide -> Offset:ULONG64, Flags:ULONG, Buffer:PWSTR, BufferSize:ULONG, DisassemblySize:PULONG, EndOffset:PULONG64
 "DisassembleWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PWSTR, ULONG, PULONG, PULONG64)(128, "DisassembleWide"),
 #GetProcessorTypeNamesWide -> Type:ULONG, FullNameBuffer:PWSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PWSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetProcessorTypeNamesWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(129, "GetProcessorTypeNamesWide"),
 #GetTextMacroWide -> Slot:ULONG, Buffer:PWSTR, BufferSize:ULONG, MacroSize:PULONG
 "GetTextMacroWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(130, "GetTextMacroWide"),
 #SetTextMacroWide -> Slot:ULONG, Macro:PCWSTR
 "SetTextMacroWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(131, "SetTextMacroWide"),
 #EvaluateWide -> Expression:PCWSTR, DesiredType:ULONG, Value:PDEBUG_VALUE, RemainderIndex:PULONG
 "EvaluateWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, PDEBUG_VALUE, PULONG)(132, "EvaluateWide"),
 #ExecuteWide -> OutputControl:ULONG, Command:PCWSTR, Flags:ULONG
 "ExecuteWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, ULONG)(133, "ExecuteWide"),
 #ExecuteCommandFileWide -> OutputControl:ULONG, CommandFile:PCWSTR, Flags:ULONG
 "ExecuteCommandFileWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, ULONG)(134, "ExecuteCommandFileWide"),
 #GetBreakpointByIndex2 -> Index:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointByIndex2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(135, "GetBreakpointByIndex2"),
 #GetBreakpointById2 -> Id:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "GetBreakpointById2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID)(136, "GetBreakpointById2"),
 #AddBreakpoint2 -> Type:ULONG, DesiredId:ULONG, Bp:*PDEBUG_BREAKPOINT2
 "AddBreakpoint2": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID)(137, "AddBreakpoint2"),
 #RemoveBreakpoint2 -> Bp:PDEBUG_BREAKPOINT2
 "RemoveBreakpoint2": ctypes.WINFUNCTYPE(HRESULT, PVOID)(138, "RemoveBreakpoint2"),
 #AddExtensionWide -> Path:PCWSTR, Flags:ULONG, Handle:PULONG64
 "AddExtensionWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, PULONG64)(139, "AddExtensionWide"),
 #GetExtensionByPathWide -> Path:PCWSTR, Handle:PULONG64
 "GetExtensionByPathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(140, "GetExtensionByPathWide"),
 #CallExtensionWide -> Handle:ULONG64, Function:PCWSTR, Arguments:PCWSTR
 "CallExtensionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, PCWSTR)(141, "CallExtensionWide"),
 #GetExtensionFunctionWide -> Handle:ULONG64, FuncName:PCWSTR, Function:*FARPROC
 "GetExtensionFunctionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, POINTER(FARPROC))(142, "GetExtensionFunctionWide"),
 #GetEventFilterTextWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, TextSize:PULONG
 "GetEventFilterTextWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(143, "GetEventFilterTextWide"),
 #GetEventFilterCommandWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetEventFilterCommandWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(144, "GetEventFilterCommandWide"),
 #SetEventFilterCommandWide -> Index:ULONG, Command:PCWSTR
 "SetEventFilterCommandWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(145, "SetEventFilterCommandWide"),
 #GetSpecificFilterArgumentWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, ArgumentSize:PULONG
 "GetSpecificFilterArgumentWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(146, "GetSpecificFilterArgumentWide"),
 #SetSpecificFilterArgumentWide -> Index:ULONG, Argument:PCWSTR
 "SetSpecificFilterArgumentWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(147, "SetSpecificFilterArgumentWide"),
 #GetExceptionFilterSecondCommandWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, CommandSize:PULONG
 "GetExceptionFilterSecondCommandWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(148, "GetExceptionFilterSecondCommandWide"),
 #SetExceptionFilterSecondCommandWide -> Index:ULONG, Command:PCWSTR
 "SetExceptionFilterSecondCommandWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(149, "SetExceptionFilterSecondCommandWide"),
 #GetLastEventInformationWide -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG, Description:PWSTR, DescriptionSize:ULONG, DescriptionUsed:PULONG
 "GetLastEventInformationWide": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PWSTR, ULONG, PULONG)(150, "GetLastEventInformationWide"),
 #GetTextReplacementWide -> SrcText:PCWSTR, Index:ULONG, SrcBuffer:PWSTR, SrcBufferSize:ULONG, SrcSize:PULONG, DstBuffer:PWSTR, DstBufferSize:ULONG, DstSize:PULONG
 "GetTextReplacementWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(151, "GetTextReplacementWide"),
 #SetTextReplacementWide -> SrcText:PCWSTR, DstText:PCWSTR
 "SetTextReplacementWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PCWSTR)(152, "SetTextReplacementWide"),
 #SetExpressionSyntaxByNameWide -> AbbrevName:PCWSTR
 "SetExpressionSyntaxByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(153, "SetExpressionSyntaxByNameWide"),
 #GetExpressionSyntaxNamesWide -> Index:ULONG, FullNameBuffer:PWSTR, FullNameBufferSize:ULONG, FullNameSize:PULONG, AbbrevNameBuffer:PWSTR, AbbrevNameBufferSize:ULONG, AbbrevNameSize:PULONG
 "GetExpressionSyntaxNamesWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(154, "GetExpressionSyntaxNamesWide"),
 #GetEventIndexDescriptionWide -> Index:ULONG, Which:ULONG, Buffer:PWSTR, BufferSize:ULONG, DescSize:PULONG
 "GetEventIndexDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PWSTR, ULONG, PULONG)(155, "GetEventIndexDescriptionWide"),
 #GetLogFile2 -> Buffer:PSTR, BufferSize:ULONG, FileSize:PULONG, Flags:PULONG
 "GetLogFile2": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG, PULONG)(156, "GetLogFile2"),
 #OpenLogFile2 -> File:PCSTR, Flags:ULONG
 "OpenLogFile2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG)(157, "OpenLogFile2"),
 #GetLogFile2Wide -> Buffer:PWSTR, BufferSize:ULONG, FileSize:PULONG, Flags:PULONG
 "GetLogFile2Wide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG, PULONG)(158, "GetLogFile2Wide"),
 #OpenLogFile2Wide -> File:PCWSTR, Flags:ULONG
 "OpenLogFile2Wide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG)(159, "OpenLogFile2Wide"),
 #GetSystemVersionValues -> PlatformId:PULONG, Win32Major:PULONG, Win32Minor:PULONG, KdMajor:PULONG, KdMinor:PULONG
 "GetSystemVersionValues": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PULONG, PULONG)(160, "GetSystemVersionValues"),
 #GetSystemVersionString -> Which:ULONG, Buffer:PSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSystemVersionString": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(161, "GetSystemVersionString"),
 #GetSystemVersionStringWide -> Which:ULONG, Buffer:PWSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSystemVersionStringWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(162, "GetSystemVersionStringWide"),
 #GetContextStackTrace -> StartContext:PVOID, StartContextSize:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FrameContexts:PVOID, FrameContextsSize:ULONG, FrameContextsEntrySize:ULONG, FramesFilled:PULONG
 "GetContextStackTrace": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG, PDEBUG_STACK_FRAME, ULONG, PVOID, ULONG, ULONG, PULONG)(163, "GetContextStackTrace"),
 #OutputContextStackTrace -> OutputControl:ULONG, Frames:PDEBUG_STACK_FRAME, FramesSize:ULONG, FrameContexts:PVOID, FrameContextsSize:ULONG, FrameContextsEntrySize:ULONG, Flags:ULONG
 "OutputContextStackTrace": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_STACK_FRAME, ULONG, PVOID, ULONG, ULONG, ULONG)(164, "OutputContextStackTrace"),
 #GetStoredEventInformation -> Type:PULONG, ProcessId:PULONG, ThreadId:PULONG, Context:PVOID, ContextSize:ULONG, ContextUsed:PULONG, ExtraInformation:PVOID, ExtraInformationSize:ULONG, ExtraInformationUsed:PULONG
 "GetStoredEventInformation": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PVOID, ULONG, PULONG, PVOID, ULONG, PULONG)(165, "GetStoredEventInformation"),
 #GetManagedStatus -> Flags:PULONG, WhichString:ULONG, String:PSTR, StringSize:ULONG, StringNeeded:PULONG
 "GetManagedStatus": ctypes.WINFUNCTYPE(HRESULT, PULONG, ULONG, PSTR, ULONG, PULONG)(166, "GetManagedStatus"),
 #GetManagedStatusWide -> Flags:PULONG, WhichString:ULONG, String:PWSTR, StringSize:ULONG, StringNeeded:PULONG
 "GetManagedStatusWide": ctypes.WINFUNCTYPE(HRESULT, PULONG, ULONG, PWSTR, ULONG, PULONG)(167, "GetManagedStatusWide"),
 #ResetManagedStatus -> Flags:ULONG
 "ResetManagedStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(168, "ResetManagedStatus"),
    }


class IDebugDataSpaces(COMInterface):
    IID = generate_IID(0x88F7DFAB, 0x3EA7, 0x4C3A, 0xAE, 0xFB, 0xC4, 0xE8, 0x10, 0x61, 0x73, 0xAA, name="IDebugDataSpaces", strid="88F7DFAB-3EA7-4C3A-AEFB-C4E8106173AA")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #ReadVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(3, "ReadVirtual"),
 #WriteVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(4, "WriteVirtual"),
 #SearchVirtual -> Offset:ULONG64, Length:ULONG64, Pattern:PVOID, PatternSize:ULONG, PatternGranularity:ULONG, MatchOffset:PULONG64
 "SearchVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, PVOID, ULONG, ULONG, PULONG64)(5, "SearchVirtual"),
 #ReadVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(6, "ReadVirtualUncached"),
 #WriteVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(7, "WriteVirtualUncached"),
 #ReadPointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "ReadPointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(8, "ReadPointersVirtual"),
 #WritePointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "WritePointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(9, "WritePointersVirtual"),
 #ReadPhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(10, "ReadPhysical"),
 #WritePhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WritePhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(11, "WritePhysical"),
 #ReadControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(12, "ReadControl"),
 #WriteControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(13, "WriteControl"),
 #ReadIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(14, "ReadIo"),
 #WriteIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(15, "WriteIo"),
 #ReadMsr -> Msr:ULONG, Value:PULONG64
 "ReadMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(16, "ReadMsr"),
 #WriteMsr -> Msr:ULONG, Value:ULONG64
 "WriteMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(17, "WriteMsr"),
 #ReadBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(18, "ReadBusData"),
 #WriteBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(19, "WriteBusData"),
 #CheckLowMemory -> 
 "CheckLowMemory": ctypes.WINFUNCTYPE(HRESULT)(20, "CheckLowMemory"),
 #ReadDebuggerData -> Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadDebuggerData": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PULONG)(21, "ReadDebuggerData"),
 #ReadProcessorSystemData -> Processor:ULONG, Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadProcessorSystemData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID, ULONG, PULONG)(22, "ReadProcessorSystemData"),
    }


class IDebugDataSpaces2(COMInterface):
    IID = generate_IID(0x7A5E852F, 0x96E9, 0x468F, 0xAC, 0x1B, 0x0B, 0x3A, 0xDD, 0xC4, 0xA0, 0x49, name="IDebugDataSpaces2", strid="7A5E852F-96E9-468F-AC1B-0B3ADDC4A049")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #ReadVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(3, "ReadVirtual"),
 #WriteVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(4, "WriteVirtual"),
 #SearchVirtual -> Offset:ULONG64, Length:ULONG64, Pattern:PVOID, PatternSize:ULONG, PatternGranularity:ULONG, MatchOffset:PULONG64
 "SearchVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, PVOID, ULONG, ULONG, PULONG64)(5, "SearchVirtual"),
 #ReadVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(6, "ReadVirtualUncached"),
 #WriteVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(7, "WriteVirtualUncached"),
 #ReadPointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "ReadPointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(8, "ReadPointersVirtual"),
 #WritePointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "WritePointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(9, "WritePointersVirtual"),
 #ReadPhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(10, "ReadPhysical"),
 #WritePhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WritePhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(11, "WritePhysical"),
 #ReadControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(12, "ReadControl"),
 #WriteControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(13, "WriteControl"),
 #ReadIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(14, "ReadIo"),
 #WriteIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(15, "WriteIo"),
 #ReadMsr -> Msr:ULONG, Value:PULONG64
 "ReadMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(16, "ReadMsr"),
 #WriteMsr -> Msr:ULONG, Value:ULONG64
 "WriteMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(17, "WriteMsr"),
 #ReadBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(18, "ReadBusData"),
 #WriteBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(19, "WriteBusData"),
 #CheckLowMemory -> 
 "CheckLowMemory": ctypes.WINFUNCTYPE(HRESULT)(20, "CheckLowMemory"),
 #ReadDebuggerData -> Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadDebuggerData": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PULONG)(21, "ReadDebuggerData"),
 #ReadProcessorSystemData -> Processor:ULONG, Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadProcessorSystemData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID, ULONG, PULONG)(22, "ReadProcessorSystemData"),
 #VirtualToPhysical -> Virtual:ULONG64, Physical:PULONG64
 "VirtualToPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64)(23, "VirtualToPhysical"),
 #GetVirtualTranslationPhysicalOffsets -> Virtual:ULONG64, Offsets:PULONG64, OffsetsSize:ULONG, Levels:PULONG
 "GetVirtualTranslationPhysicalOffsets": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64, ULONG, PULONG)(24, "GetVirtualTranslationPhysicalOffsets"),
 #ReadHandleData -> Handle:ULONG64, DataType:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadHandleData": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadHandleData"),
 #FillVirtual -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "FillVirtual"),
 #FillPhysical -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(27, "FillPhysical"),
 #QueryVirtual -> Offset:ULONG64, Info:PMEMORY_BASIC_INFORMATION64
 "QueryVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PMEMORY_BASIC_INFORMATION64)(28, "QueryVirtual"),
    }


class IDebugDataSpaces3(COMInterface):
    IID = generate_IID(0x23F79D6C, 0x8AAF, 0x4F7C, 0xA6, 0x07, 0x99, 0x95, 0xF5, 0x40, 0x7E, 0x63, name="IDebugDataSpaces3", strid="23F79D6C-8AAF-4F7C-A607-9995F5407E63")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #ReadVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(3, "ReadVirtual"),
 #WriteVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(4, "WriteVirtual"),
 #SearchVirtual -> Offset:ULONG64, Length:ULONG64, Pattern:PVOID, PatternSize:ULONG, PatternGranularity:ULONG, MatchOffset:PULONG64
 "SearchVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, PVOID, ULONG, ULONG, PULONG64)(5, "SearchVirtual"),
 #ReadVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(6, "ReadVirtualUncached"),
 #WriteVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(7, "WriteVirtualUncached"),
 #ReadPointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "ReadPointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(8, "ReadPointersVirtual"),
 #WritePointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "WritePointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(9, "WritePointersVirtual"),
 #ReadPhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(10, "ReadPhysical"),
 #WritePhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WritePhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(11, "WritePhysical"),
 #ReadControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(12, "ReadControl"),
 #WriteControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(13, "WriteControl"),
 #ReadIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(14, "ReadIo"),
 #WriteIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(15, "WriteIo"),
 #ReadMsr -> Msr:ULONG, Value:PULONG64
 "ReadMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(16, "ReadMsr"),
 #WriteMsr -> Msr:ULONG, Value:ULONG64
 "WriteMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(17, "WriteMsr"),
 #ReadBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(18, "ReadBusData"),
 #WriteBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(19, "WriteBusData"),
 #CheckLowMemory -> 
 "CheckLowMemory": ctypes.WINFUNCTYPE(HRESULT)(20, "CheckLowMemory"),
 #ReadDebuggerData -> Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadDebuggerData": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PULONG)(21, "ReadDebuggerData"),
 #ReadProcessorSystemData -> Processor:ULONG, Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadProcessorSystemData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID, ULONG, PULONG)(22, "ReadProcessorSystemData"),
 #VirtualToPhysical -> Virtual:ULONG64, Physical:PULONG64
 "VirtualToPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64)(23, "VirtualToPhysical"),
 #GetVirtualTranslationPhysicalOffsets -> Virtual:ULONG64, Offsets:PULONG64, OffsetsSize:ULONG, Levels:PULONG
 "GetVirtualTranslationPhysicalOffsets": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64, ULONG, PULONG)(24, "GetVirtualTranslationPhysicalOffsets"),
 #ReadHandleData -> Handle:ULONG64, DataType:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadHandleData": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadHandleData"),
 #FillVirtual -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "FillVirtual"),
 #FillPhysical -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(27, "FillPhysical"),
 #QueryVirtual -> Offset:ULONG64, Info:PMEMORY_BASIC_INFORMATION64
 "QueryVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PMEMORY_BASIC_INFORMATION64)(28, "QueryVirtual"),
 #ReadImageNtHeaders -> ImageBase:ULONG64, Headers:PIMAGE_NT_HEADERS64
 "ReadImageNtHeaders": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PIMAGE_NT_HEADERS64)(29, "ReadImageNtHeaders"),
 #ReadTagged -> Tag:LPGUID, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, TotalSize:PULONG
 "ReadTagged": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG, PVOID, ULONG, PULONG)(30, "ReadTagged"),
 #StartEnumTagged -> Handle:PULONG64
 "StartEnumTagged": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(31, "StartEnumTagged"),
 #GetNextTagged -> Handle:ULONG64, Tag:LPGUID, Size:PULONG
 "GetNextTagged": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, PULONG)(32, "GetNextTagged"),
 #EndEnumTagged -> Handle:ULONG64
 "EndEnumTagged": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(33, "EndEnumTagged"),
    }


class IDebugDataSpaces4(COMInterface):
    IID = generate_IID(0xD98ADA1F, 0x29E9, 0x4EF5, 0xA6, 0xC0, 0xE5, 0x33, 0x49, 0x88, 0x32, 0x12, name="IDebugDataSpaces4", strid="D98ADA1F-29E9-4EF5-A6C0-E53349883212")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #ReadVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(3, "ReadVirtual"),
 #WriteVirtual -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(4, "WriteVirtual"),
 #SearchVirtual -> Offset:ULONG64, Length:ULONG64, Pattern:PVOID, PatternSize:ULONG, PatternGranularity:ULONG, MatchOffset:PULONG64
 "SearchVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, PVOID, ULONG, ULONG, PULONG64)(5, "SearchVirtual"),
 #ReadVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(6, "ReadVirtualUncached"),
 #WriteVirtualUncached -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteVirtualUncached": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(7, "WriteVirtualUncached"),
 #ReadPointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "ReadPointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(8, "ReadPointersVirtual"),
 #WritePointersVirtual -> Count:ULONG, Offset:ULONG64, Ptrs:PULONG64
 "WritePointersVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PULONG64)(9, "WritePointersVirtual"),
 #ReadPhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(10, "ReadPhysical"),
 #WritePhysical -> Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WritePhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, ULONG, PULONG)(11, "WritePhysical"),
 #ReadControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(12, "ReadControl"),
 #WriteControl -> Processor:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteControl": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PVOID, ULONG, PULONG)(13, "WriteControl"),
 #ReadIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(14, "ReadIo"),
 #WriteIo -> InterfaceType:ULONG, BusNumber:ULONG, AddressSpace:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteIo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(15, "WriteIo"),
 #ReadMsr -> Msr:ULONG, Value:PULONG64
 "ReadMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(16, "ReadMsr"),
 #WriteMsr -> Msr:ULONG, Value:ULONG64
 "WriteMsr": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(17, "WriteMsr"),
 #ReadBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(18, "ReadBusData"),
 #WriteBusData -> BusDataType:ULONG, BusNumber:ULONG, SlotNumber:ULONG, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteBusData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG, PVOID, ULONG, PULONG)(19, "WriteBusData"),
 #CheckLowMemory -> 
 "CheckLowMemory": ctypes.WINFUNCTYPE(HRESULT)(20, "CheckLowMemory"),
 #ReadDebuggerData -> Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadDebuggerData": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, ULONG, PULONG)(21, "ReadDebuggerData"),
 #ReadProcessorSystemData -> Processor:ULONG, Index:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadProcessorSystemData": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PVOID, ULONG, PULONG)(22, "ReadProcessorSystemData"),
 #VirtualToPhysical -> Virtual:ULONG64, Physical:PULONG64
 "VirtualToPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64)(23, "VirtualToPhysical"),
 #GetVirtualTranslationPhysicalOffsets -> Virtual:ULONG64, Offsets:PULONG64, OffsetsSize:ULONG, Levels:PULONG
 "GetVirtualTranslationPhysicalOffsets": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64, ULONG, PULONG)(24, "GetVirtualTranslationPhysicalOffsets"),
 #ReadHandleData -> Handle:ULONG64, DataType:ULONG, Buffer:PVOID, BufferSize:ULONG, DataSize:PULONG
 "ReadHandleData": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadHandleData"),
 #FillVirtual -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "FillVirtual"),
 #FillPhysical -> Start:ULONG64, Size:ULONG, Pattern:PVOID, PatternSize:ULONG, Filled:PULONG
 "FillPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(27, "FillPhysical"),
 #QueryVirtual -> Offset:ULONG64, Info:PMEMORY_BASIC_INFORMATION64
 "QueryVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PMEMORY_BASIC_INFORMATION64)(28, "QueryVirtual"),
 #ReadImageNtHeaders -> ImageBase:ULONG64, Headers:PIMAGE_NT_HEADERS64
 "ReadImageNtHeaders": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PIMAGE_NT_HEADERS64)(29, "ReadImageNtHeaders"),
 #ReadTagged -> Tag:LPGUID, Offset:ULONG, Buffer:PVOID, BufferSize:ULONG, TotalSize:PULONG
 "ReadTagged": ctypes.WINFUNCTYPE(HRESULT, PVOID, ULONG, PVOID, ULONG, PULONG)(30, "ReadTagged"),
 #StartEnumTagged -> Handle:PULONG64
 "StartEnumTagged": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(31, "StartEnumTagged"),
 #GetNextTagged -> Handle:ULONG64, Tag:LPGUID, Size:PULONG
 "GetNextTagged": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PVOID, PULONG)(32, "GetNextTagged"),
 #EndEnumTagged -> Handle:ULONG64
 "EndEnumTagged": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(33, "EndEnumTagged"),
 #GetOffsetInformation -> Space:ULONG, Which:ULONG, Offset:ULONG64, Buffer:PVOID, BufferSize:ULONG, InfoSize:PULONG
 "GetOffsetInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64, PVOID, ULONG, PULONG)(34, "GetOffsetInformation"),
 #GetNextDifferentlyValidOffsetVirtual -> Offset:ULONG64, NextOffset:PULONG64
 "GetNextDifferentlyValidOffsetVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG64)(35, "GetNextDifferentlyValidOffsetVirtual"),
 #GetValidRegionVirtual -> Base:ULONG64, Size:ULONG, ValidBase:PULONG64, ValidSize:PULONG
 "GetValidRegionVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG64, PULONG)(36, "GetValidRegionVirtual"),
 #SearchVirtual2 -> Offset:ULONG64, Length:ULONG64, Flags:ULONG, Pattern:PVOID, PatternSize:ULONG, PatternGranularity:ULONG, MatchOffset:PULONG64
 "SearchVirtual2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, ULONG, PULONG64)(37, "SearchVirtual2"),
 #ReadMultiByteStringVirtual -> Offset:ULONG64, MaxBytes:ULONG, Buffer:PSTR, BufferSize:ULONG, StringBytes:PULONG
 "ReadMultiByteStringVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG)(38, "ReadMultiByteStringVirtual"),
 #ReadMultiByteStringVirtualWide -> Offset:ULONG64, MaxBytes:ULONG, CodePage:ULONG, Buffer:PWSTR, BufferSize:ULONG, StringBytes:PULONG
 "ReadMultiByteStringVirtualWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PWSTR, ULONG, PULONG)(39, "ReadMultiByteStringVirtualWide"),
 #ReadUnicodeStringVirtual -> Offset:ULONG64, MaxBytes:ULONG, CodePage:ULONG, Buffer:PSTR, BufferSize:ULONG, StringBytes:PULONG
 "ReadUnicodeStringVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG)(40, "ReadUnicodeStringVirtual"),
 #ReadUnicodeStringVirtualWide -> Offset:ULONG64, MaxBytes:ULONG, Buffer:PWSTR, BufferSize:ULONG, StringBytes:PULONG
 "ReadUnicodeStringVirtualWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PWSTR, ULONG, PULONG)(41, "ReadUnicodeStringVirtualWide"),
 #ReadPhysical2 -> Offset:ULONG64, Flags:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadPhysical2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(42, "ReadPhysical2"),
 #WritePhysical2 -> Offset:ULONG64, Flags:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WritePhysical2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(43, "WritePhysical2"),
    }


class IDebugEventCallbacks(COMInterface):
    IID = generate_IID(0x337BE28B, 0x5036, 0x4D72, 0xB6, 0xBF, 0xC4, 0x5F, 0xBB, 0x9F, 0x2E, 0xAA, name="IDebugEventCallbacks", strid="337BE28B-5036-4D72-B6BF-C45FBB9F2EAA")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterestMask -> Mask:PULONG
 "GetInterestMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetInterestMask"),
 #Breakpoint -> Bp:PDEBUG_BREAKPOINT2
 "Breakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(4, "Breakpoint"),
 #Exception -> Exception:PEXCEPTION_RECORD64, FirstChance:ULONG
 "Exception": ctypes.WINFUNCTYPE(HRESULT, PEXCEPTION_RECORD64, ULONG)(5, "Exception"),
 #CreateThread -> Handle:ULONG64, DataOffset:ULONG64, StartOffset:ULONG64
 "CreateThread": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64)(6, "CreateThread"),
 #ExitThread -> ExitCode:ULONG
 "ExitThread": ctypes.WINFUNCTYPE(HRESULT, ULONG)(7, "ExitThread"),
 #CreateProcess -> ImageFileHandle:ULONG64, Handle:ULONG64, BaseOffset:ULONG64, ModuleSize:ULONG, ModuleName:PCSTR, ImageName:PCSTR, CheckSum:ULONG, TimeDateStamp:ULONG, InitialThreadHandle:ULONG64, ThreadDataOffset:ULONG64, StartOffset:ULONG64
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, ULONG, PCSTR, PCSTR, ULONG, ULONG, ULONG64, ULONG64, ULONG64)(8, "CreateProcess"),
 #ExitProcess -> ExitCode:ULONG
 "ExitProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG)(9, "ExitProcess"),
 #LoadModule -> ImageFileHandle:ULONG64, BaseOffset:ULONG64, ModuleSize:ULONG, ModuleName:PCSTR, ImageName:PCSTR, CheckSum:ULONG, TimeDateStamp:ULONG
 "LoadModule": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PCSTR, PCSTR, ULONG, ULONG)(10, "LoadModule"),
 #UnloadModule -> ImageBaseName:PCSTR, BaseOffset:ULONG64
 "UnloadModule": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG64)(11, "UnloadModule"),
 #SystemError -> Error:ULONG, Level:ULONG
 "SystemError": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(12, "SystemError"),
 #SessionStatus -> Status:ULONG
 "SessionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(13, "SessionStatus"),
 #ChangeDebuggeeState -> Flags:ULONG, Argument:ULONG64
 "ChangeDebuggeeState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(14, "ChangeDebuggeeState"),
 #ChangeEngineState -> Flags:ULONG, Argument:ULONG64
 "ChangeEngineState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(15, "ChangeEngineState"),
 #ChangeSymbolState -> Flags:ULONG, Argument:ULONG64
 "ChangeSymbolState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(16, "ChangeSymbolState"),
    }


class IDebugEventCallbacksWide(COMInterface):
    IID = generate_IID(0x0690E046, 0x9C23, 0x45AC, 0xA0, 0x4F, 0x98, 0x7A, 0xC2, 0x9A, 0xD0, 0xD3, name="IDebugEventCallbacksWide", strid="0690E046-9C23-45AC-A04F-987AC29AD0D3")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetInterestMask -> Mask:PULONG
 "GetInterestMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetInterestMask"),
 #Breakpoint -> Bp:PDEBUG_BREAKPOINT2
 "Breakpoint": ctypes.WINFUNCTYPE(HRESULT, PVOID)(4, "Breakpoint"),
 #Exception -> Exception:PEXCEPTION_RECORD64, FirstChance:ULONG
 "Exception": ctypes.WINFUNCTYPE(HRESULT, PEXCEPTION_RECORD64, ULONG)(5, "Exception"),
 #CreateThread -> Handle:ULONG64, DataOffset:ULONG64, StartOffset:ULONG64
 "CreateThread": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64)(6, "CreateThread"),
 #ExitThread -> ExitCode:ULONG
 "ExitThread": ctypes.WINFUNCTYPE(HRESULT, ULONG)(7, "ExitThread"),
 #CreateProcess -> ImageFileHandle:ULONG64, Handle:ULONG64, BaseOffset:ULONG64, ModuleSize:ULONG, ModuleName:PCWSTR, ImageName:PCWSTR, CheckSum:ULONG, TimeDateStamp:ULONG, InitialThreadHandle:ULONG64, ThreadDataOffset:ULONG64, StartOffset:ULONG64
 "CreateProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG64, ULONG, PCWSTR, PCWSTR, ULONG, ULONG, ULONG64, ULONG64, ULONG64)(8, "CreateProcess"),
 #ExitProcess -> ExitCode:ULONG
 "ExitProcess": ctypes.WINFUNCTYPE(HRESULT, ULONG)(9, "ExitProcess"),
 #LoadModule -> ImageFileHandle:ULONG64, BaseOffset:ULONG64, ModuleSize:ULONG, ModuleName:PCWSTR, ImageName:PCWSTR, CheckSum:ULONG, TimeDateStamp:ULONG
 "LoadModule": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PCWSTR, PCWSTR, ULONG, ULONG)(10, "LoadModule"),
 #UnloadModule -> ImageBaseName:PCWSTR, BaseOffset:ULONG64
 "UnloadModule": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG64)(11, "UnloadModule"),
 #SystemError -> Error:ULONG, Level:ULONG
 "SystemError": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(12, "SystemError"),
 #SessionStatus -> Status:ULONG
 "SessionStatus": ctypes.WINFUNCTYPE(HRESULT, ULONG)(13, "SessionStatus"),
 #ChangeDebuggeeState -> Flags:ULONG, Argument:ULONG64
 "ChangeDebuggeeState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(14, "ChangeDebuggeeState"),
 #ChangeEngineState -> Flags:ULONG, Argument:ULONG64
 "ChangeEngineState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(15, "ChangeEngineState"),
 #ChangeSymbolState -> Flags:ULONG, Argument:ULONG64
 "ChangeSymbolState": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(16, "ChangeSymbolState"),
    }


class IDebugInputCallbacks(COMInterface):
    IID = generate_IID(0x9F50E42C, 0xF136, 0x499E, 0x9A, 0x97, 0x73, 0x03, 0x6C, 0x94, 0xED, 0x2D, name="IDebugInputCallbacks", strid="9F50E42C-F136-499E-9A97-73036C94ED2D")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #StartInput -> BufferSize:ULONG
 "StartInput": ctypes.WINFUNCTYPE(HRESULT, ULONG)(3, "StartInput"),
 #EndInput -> 
 "EndInput": ctypes.WINFUNCTYPE(HRESULT)(4, "EndInput"),
    }


class IDebugOutputCallbacks(COMInterface):
    IID = generate_IID(0x4BF58045, 0xD654, 0x4C40, 0xB0, 0xAF, 0x68, 0x30, 0x90, 0xF3, 0x56, 0xDC, name="IDebugOutputCallbacks", strid="4BF58045-D654-4C40-B0AF-683090F356DC")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #Output -> Mask:ULONG, Text:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "Output"),
    }


class IDebugOutputCallbacks2(COMInterface):
    IID = generate_IID(0x67721FE9, 0x56D2, 0x4A44, 0xA3, 0x25, 0x2B, 0x65, 0x51, 0x3C, 0xE6, 0xEB, name="IDebugOutputCallbacks2", strid="67721FE9-56D2-4A44-A325-2B65513CE6EB")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #Output -> Mask:ULONG, Text:PCSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(3, "Output"),
 #GetInterestMask -> Mask:PULONG
 "GetInterestMask": ctypes.WINFUNCTYPE(HRESULT, PULONG)(4, "GetInterestMask"),
 #Output2 -> Which:ULONG, Flags:ULONG, Arg:ULONG64, Text:PCWSTR
 "Output2": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64, PCWSTR)(5, "Output2"),
    }


class IDebugOutputCallbacksWide(COMInterface):
    IID = generate_IID(0x4C7FD663, 0xC394, 0x4E26, 0x8E, 0xF1, 0x34, 0xAD, 0x5E, 0xD3, 0x76, 0x4C, name="IDebugOutputCallbacksWide", strid="4C7FD663-C394-4E26-8EF1-34AD5ED3764C")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #Output -> Mask:ULONG, Text:PCWSTR
 "Output": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(3, "Output"),
    }


class IDebugRegisters(COMInterface):
    IID = generate_IID(0xCE289126, 0x9E84, 0x45A7, 0x93, 0x7E, 0x67, 0xBB, 0x18, 0x69, 0x14, 0x93, name="IDebugRegisters", strid="CE289126-9E84-45A7-937E-67BB18691493")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetNumberRegisters -> Number:PULONG
 "GetNumberRegisters": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetNumberRegisters"),
 #GetDescription -> Register:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Desc:PDEBUG_REGISTER_DESCRIPTION
 "GetDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PDEBUG_REGISTER_DESCRIPTION)(4, "GetDescription"),
 #GetIndexByName -> Name:PCSTR, Index:PULONG
 "GetIndexByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG)(5, "GetIndexByName"),
 #GetValue -> Register:ULONG, Value:PDEBUG_VALUE
 "GetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(6, "GetValue"),
 #SetValue -> Register:ULONG, Value:PDEBUG_VALUE
 "SetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(7, "SetValue"),
 #GetValues -> Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "GetValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_VALUE)(8, "GetValues"),
 #SetValues -> Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "SetValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_VALUE)(9, "SetValues"),
 #OutputRegisters -> OutputControl:ULONG, Flags:ULONG
 "OutputRegisters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(10, "OutputRegisters"),
 #GetInstructionOffset -> Offset:PULONG64
 "GetInstructionOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(11, "GetInstructionOffset"),
 #GetStackOffset -> Offset:PULONG64
 "GetStackOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(12, "GetStackOffset"),
 #GetFrameOffset -> Offset:PULONG64
 "GetFrameOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetFrameOffset"),
    }


class IDebugRegisters2(COMInterface):
    IID = generate_IID(0x1656AFA9, 0x19C6, 0x4E3A, 0x97, 0xE7, 0x5D, 0xC9, 0x16, 0x0C, 0xF9, 0xC4, name="IDebugRegisters2", strid="1656AFA9-19C6-4E3A-97E7-5DC9160CF9C4")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetNumberRegisters -> Number:PULONG
 "GetNumberRegisters": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetNumberRegisters"),
 #GetDescription -> Register:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Desc:PDEBUG_REGISTER_DESCRIPTION
 "GetDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PDEBUG_REGISTER_DESCRIPTION)(4, "GetDescription"),
 #GetIndexByName -> Name:PCSTR, Index:PULONG
 "GetIndexByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG)(5, "GetIndexByName"),
 #GetValue -> Register:ULONG, Value:PDEBUG_VALUE
 "GetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(6, "GetValue"),
 #SetValue -> Register:ULONG, Value:PDEBUG_VALUE
 "SetValue": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_VALUE)(7, "SetValue"),
 #GetValues -> Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "GetValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_VALUE)(8, "GetValues"),
 #SetValues -> Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "SetValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG, ULONG, PDEBUG_VALUE)(9, "SetValues"),
 #OutputRegisters -> OutputControl:ULONG, Flags:ULONG
 "OutputRegisters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG)(10, "OutputRegisters"),
 #GetInstructionOffset -> Offset:PULONG64
 "GetInstructionOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(11, "GetInstructionOffset"),
 #GetStackOffset -> Offset:PULONG64
 "GetStackOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(12, "GetStackOffset"),
 #GetFrameOffset -> Offset:PULONG64
 "GetFrameOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetFrameOffset"),
 #GetDescriptionWide -> Register:ULONG, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG, Desc:PDEBUG_REGISTER_DESCRIPTION
 "GetDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PDEBUG_REGISTER_DESCRIPTION)(14, "GetDescriptionWide"),
 #GetIndexByNameWide -> Name:PCWSTR, Index:PULONG
 "GetIndexByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG)(15, "GetIndexByNameWide"),
 #GetNumberPseudoRegisters -> Number:PULONG
 "GetNumberPseudoRegisters": ctypes.WINFUNCTYPE(HRESULT, PULONG)(16, "GetNumberPseudoRegisters"),
 #GetPseudoDescription -> Register:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, TypeModule:PULONG64, TypeId:PULONG
 "GetPseudoDescription": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG, PULONG64, PULONG)(17, "GetPseudoDescription"),
 #GetPseudoDescriptionWide -> Register:ULONG, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG, TypeModule:PULONG64, TypeId:PULONG
 "GetPseudoDescriptionWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG, PULONG64, PULONG)(18, "GetPseudoDescriptionWide"),
 #GetPseudoIndexByName -> Name:PCSTR, Index:PULONG
 "GetPseudoIndexByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG)(19, "GetPseudoIndexByName"),
 #GetPseudoIndexByNameWide -> Name:PCWSTR, Index:PULONG
 "GetPseudoIndexByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG)(20, "GetPseudoIndexByNameWide"),
 #GetPseudoValues -> Source:ULONG, Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "GetPseudoValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, ULONG, PDEBUG_VALUE)(21, "GetPseudoValues"),
 #SetPseudoValues -> Source:ULONG, Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "SetPseudoValues": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, ULONG, PDEBUG_VALUE)(22, "SetPseudoValues"),
 #GetValues2 -> Source:ULONG, Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "GetValues2": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, ULONG, PDEBUG_VALUE)(23, "GetValues2"),
 #SetValues2 -> Source:ULONG, Count:ULONG, Indices:PULONG, Start:ULONG, Values:PDEBUG_VALUE
 "SetValues2": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, ULONG, PDEBUG_VALUE)(24, "SetValues2"),
 #OutputRegisters2 -> OutputControl:ULONG, Source:ULONG, Flags:ULONG
 "OutputRegisters2": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG)(25, "OutputRegisters2"),
 #GetInstructionOffset2 -> Source:ULONG, Offset:PULONG64
 "GetInstructionOffset2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(26, "GetInstructionOffset2"),
 #GetStackOffset2 -> Source:ULONG, Offset:PULONG64
 "GetStackOffset2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(27, "GetStackOffset2"),
 #GetFrameOffset2 -> Source:ULONG, Offset:PULONG64
 "GetFrameOffset2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(28, "GetFrameOffset2"),
    }


class IDebugSymbolGroup(COMInterface):
    IID = generate_IID(0xF2528316, 0x0F1A, 0x4431, 0xAE, 0xED, 0x11, 0xD0, 0x96, 0xE1, 0xE2, 0xAB, name="IDebugSymbolGroup", strid="F2528316-0F1A-4431-AEED-11D096E1E2AB")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetNumberSymbols -> Number:PULONG
 "GetNumberSymbols": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetNumberSymbols"),
 #AddSymbol -> Name:PCSTR, Index:PULONG
 "AddSymbol": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG)(4, "AddSymbol"),
 #RemoveSymbolByName -> Name:PCSTR
 "RemoveSymbolByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "RemoveSymbolByName"),
 #RemoveSymbolByIndex -> Index:ULONG
 "RemoveSymbolByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "RemoveSymbolByIndex"),
 #GetSymbolName -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolName": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(7, "GetSymbolName"),
 #GetSymbolParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SYMBOL_PARAMETERS
 "GetSymbolParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SYMBOL_PARAMETERS)(8, "GetSymbolParameters"),
 #ExpandSymbol -> Index:ULONG, Expand:BOOL
 "ExpandSymbol": ctypes.WINFUNCTYPE(HRESULT, ULONG, BOOL)(9, "ExpandSymbol"),
 #OutputSymbols -> OutputControl:ULONG, Flags:ULONG, Start:ULONG, Count:ULONG
 "OutputSymbols": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG)(10, "OutputSymbols"),
 #WriteSymbol -> Index:ULONG, Value:PCSTR
 "WriteSymbol": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(11, "WriteSymbol"),
 #OutputAsType -> Index:ULONG, Type:PCSTR
 "OutputAsType": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(12, "OutputAsType"),
    }


class IDebugSymbolGroup2(COMInterface):
    IID = generate_IID(0x6A7CCC5F, 0xFB5E, 0x4DCC, 0xB4, 0x1C, 0x6C, 0x20, 0x30, 0x7B, 0xCC, 0xC7, name="IDebugSymbolGroup2", strid="6A7CCC5F-FB5E-4DCC-B41C-6C20307BCCC7")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetNumberSymbols -> Number:PULONG
 "GetNumberSymbols": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetNumberSymbols"),
 #AddSymbol -> Name:PCSTR, Index:PULONG
 "AddSymbol": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG)(4, "AddSymbol"),
 #RemoveSymbolByName -> Name:PCSTR
 "RemoveSymbolByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(5, "RemoveSymbolByName"),
 #RemoveSymbolByIndex -> Index:ULONG
 "RemoveSymbolByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "RemoveSymbolByIndex"),
 #GetSymbolName -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolName": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(7, "GetSymbolName"),
 #GetSymbolParameters -> Start:ULONG, Count:ULONG, Params:PDEBUG_SYMBOL_PARAMETERS
 "GetSymbolParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PDEBUG_SYMBOL_PARAMETERS)(8, "GetSymbolParameters"),
 #ExpandSymbol -> Index:ULONG, Expand:BOOL
 "ExpandSymbol": ctypes.WINFUNCTYPE(HRESULT, ULONG, BOOL)(9, "ExpandSymbol"),
 #OutputSymbols -> OutputControl:ULONG, Flags:ULONG, Start:ULONG, Count:ULONG
 "OutputSymbols": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG, ULONG)(10, "OutputSymbols"),
 #WriteSymbol -> Index:ULONG, Value:PCSTR
 "WriteSymbol": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(11, "WriteSymbol"),
 #OutputAsType -> Index:ULONG, Type:PCSTR
 "OutputAsType": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR)(12, "OutputAsType"),
 #AddSymbolWide -> Name:PCWSTR, Index:PULONG
 "AddSymbolWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG)(13, "AddSymbolWide"),
 #RemoveSymbolByNameWide -> Name:PCWSTR
 "RemoveSymbolByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(14, "RemoveSymbolByNameWide"),
 #GetSymbolNameWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(15, "GetSymbolNameWide"),
 #WriteSymbolWide -> Index:ULONG, Value:PCWSTR
 "WriteSymbolWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(16, "WriteSymbolWide"),
 #OutputAsTypeWide -> Index:ULONG, Type:PCWSTR
 "OutputAsTypeWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR)(17, "OutputAsTypeWide"),
 #GetSymbolTypeName -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolTypeName": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(18, "GetSymbolTypeName"),
 #GetSymbolTypeNameWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolTypeNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(19, "GetSymbolTypeNameWide"),
 #GetSymbolSize -> Index:ULONG, Size:PULONG
 "GetSymbolSize": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(20, "GetSymbolSize"),
 #GetSymbolOffset -> Index:ULONG, Offset:PULONG64
 "GetSymbolOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(21, "GetSymbolOffset"),
 #GetSymbolRegister -> Index:ULONG, Register:PULONG
 "GetSymbolRegister": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(22, "GetSymbolRegister"),
 #GetSymbolValueText -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolValueText": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(23, "GetSymbolValueText"),
 #GetSymbolValueTextWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG
 "GetSymbolValueTextWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(24, "GetSymbolValueTextWide"),
 #GetSymbolEntryInformation -> Index:ULONG, Entry:PDEBUG_SYMBOL_ENTRY
 "GetSymbolEntryInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, PDEBUG_SYMBOL_ENTRY)(25, "GetSymbolEntryInformation"),
    }


class IDebugSymbols(COMInterface):
    IID = generate_IID(0x8C31E98C, 0x983A, 0x48A5, 0x90, 0x16, 0x6F, 0xE5, 0xD6, 0x67, 0xA9, 0x50, name="IDebugSymbols", strid="8C31E98C-983A-48A5-9016-6FE5D667A950")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetSymbolOptions -> Options:PULONG
 "GetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetSymbolOptions"),
 #AddSymbolOptions -> Options:ULONG
 "AddSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "AddSymbolOptions"),
 #RemoveSymbolOptions -> Options:ULONG
 "RemoveSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(5, "RemoveSymbolOptions"),
 #SetSymbolOptions -> Options:ULONG
 "SetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetSymbolOptions"),
 #GetNameByOffset -> Offset:ULONG64, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(7, "GetNameByOffset"),
 #GetOffsetByName -> Symbol:PCSTR, Offset:PULONG64
 "GetOffsetByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(8, "GetOffsetByName"),
 #GetNearNameByOffset -> Offset:ULONG64, Delta:LONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNearNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PSTR, ULONG, PULONG, PULONG64)(9, "GetNearNameByOffset"),
 #GetLineByOffset -> Offset:ULONG64, Line:PULONG, FileBuffer:PSTR, FileBufferSize:ULONG, FileSize:PULONG, Displacement:PULONG64
 "GetLineByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PSTR, ULONG, PULONG, PULONG64)(10, "GetLineByOffset"),
 #GetOffsetByLine -> Line:ULONG, File:PCSTR, Offset:PULONG64
 "GetOffsetByLine": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PULONG64)(11, "GetOffsetByLine"),
 #GetNumberModules -> Loaded:PULONG, Unloaded:PULONG
 "GetNumberModules": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(12, "GetNumberModules"),
 #GetModuleByIndex -> Index:ULONG, Base:PULONG64
 "GetModuleByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(13, "GetModuleByIndex"),
 #GetModuleByModuleName -> Name:PCSTR, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG, PULONG64)(14, "GetModuleByModuleName"),
 #GetModuleByOffset -> Offset:ULONG64, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG, PULONG64)(15, "GetModuleByOffset"),
 #GetModuleNames -> Index:ULONG, Base:ULONG64, ImageNameBuffer:PSTR, ImageNameBufferSize:ULONG, ImageNameSize:PULONG, ModuleNameBuffer:PSTR, ModuleNameBufferSize:ULONG, ModuleNameSize:PULONG, LoadedImageNameBuffer:PSTR, LoadedImageNameBufferSize:ULONG, LoadedImageNameSize:PULONG
 "GetModuleNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(16, "GetModuleNames"),
 #GetModuleParameters -> Count:ULONG, Bases:PULONG64, Start:ULONG, Params:PDEBUG_MODULE_PARAMETERS
 "GetModuleParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64, ULONG, PDEBUG_MODULE_PARAMETERS)(17, "GetModuleParameters"),
 #GetSymbolModule -> Symbol:PCSTR, Base:PULONG64
 "GetSymbolModule": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(18, "GetSymbolModule"),
 #GetTypeName -> Module:ULONG64, TypeId:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetTypeName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG)(19, "GetTypeName"),
 #GetTypeId -> Module:ULONG64, Name:PCSTR, TypeId:PULONG
 "GetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG)(20, "GetTypeId"),
 #GetTypeSize -> Module:ULONG64, TypeId:ULONG, Size:PULONG
 "GetTypeSize": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG)(21, "GetTypeSize"),
 #GetFieldOffset -> Module:ULONG64, TypeId:ULONG, Field:PCSTR, Offset:PULONG
 "GetFieldOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, PULONG)(22, "GetFieldOffset"),
 #GetSymbolTypeId -> Symbol:PCSTR, TypeId:PULONG, Module:PULONG64
 "GetSymbolTypeId": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG, PULONG64)(23, "GetSymbolTypeId"),
 #GetOffsetTypeId -> Offset:ULONG64, TypeId:PULONG, Module:PULONG64
 "GetOffsetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PULONG64)(24, "GetOffsetTypeId"),
 #ReadTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadTypedDataVirtual"),
 #WriteTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "WriteTypedDataVirtual"),
 #OutputTypedDataVirtual -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(27, "OutputTypedDataVirtual"),
 #ReadTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(28, "ReadTypedDataPhysical"),
 #WriteTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(29, "WriteTypedDataPhysical"),
 #OutputTypedDataPhysical -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(30, "OutputTypedDataPhysical"),
 #GetScope -> InstructionOffset:PULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "GetScope": ctypes.WINFUNCTYPE(HRESULT, PULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(31, "GetScope"),
 #SetScope -> InstructionOffset:ULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "SetScope": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(32, "SetScope"),
 #ResetScope -> 
 "ResetScope": ctypes.WINFUNCTYPE(HRESULT)(33, "ResetScope"),
 #GetScopeSymbolGroup -> Flags:ULONG, Update:PDEBUG_SYMBOL_GROUP2, Symbols:*PDEBUG_SYMBOL_GROUP2
 "GetScopeSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, PVOID)(34, "GetScopeSymbolGroup"),
 #CreateSymbolGroup -> Group:*PDEBUG_SYMBOL_GROUP2
 "CreateSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, PVOID)(35, "CreateSymbolGroup"),
 #StartSymbolMatch -> Pattern:PCSTR, Handle:PULONG64
 "StartSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(36, "StartSymbolMatch"),
 #GetNextSymbolMatch -> Handle:ULONG64, Buffer:PSTR, BufferSize:ULONG, MatchSize:PULONG, Offset:PULONG64
 "GetNextSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(37, "GetNextSymbolMatch"),
 #EndSymbolMatch -> Handle:ULONG64
 "EndSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(38, "EndSymbolMatch"),
 #Reload -> Module:PCSTR
 "Reload": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(39, "Reload"),
 #GetSymbolPath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(40, "GetSymbolPath"),
 #SetSymbolPath -> Path:PCSTR
 "SetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(41, "SetSymbolPath"),
 #AppendSymbolPath -> Addition:PCSTR
 "AppendSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "AppendSymbolPath"),
 #GetImagePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetImagePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetImagePath"),
 #SetImagePath -> Path:PCSTR
 "SetImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(44, "SetImagePath"),
 #AppendImagePath -> Addition:PCSTR
 "AppendImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(45, "AppendImagePath"),
 #GetSourcePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(46, "GetSourcePath"),
 #GetSourcePathElement -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ElementSize:PULONG
 "GetSourcePathElement": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(47, "GetSourcePathElement"),
 #SetSourcePath -> Path:PCSTR
 "SetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(48, "SetSourcePath"),
 #AppendSourcePath -> Addition:PCSTR
 "AppendSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(49, "AppendSourcePath"),
 #FindSourceFile -> StartElement:ULONG, File:PCSTR, Flags:ULONG, FoundElement:PULONG, Buffer:PSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(50, "FindSourceFile"),
 #GetSourceFileLineOffsets -> File:PCSTR, Buffer:PULONG64, BufferLines:ULONG, FileLines:PULONG
 "GetSourceFileLineOffsets": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64, ULONG, PULONG)(51, "GetSourceFileLineOffsets"),
    }


class IDebugSymbols2(COMInterface):
    IID = generate_IID(0x3A707211, 0xAFDD, 0x4495, 0xAD, 0x4F, 0x56, 0xFE, 0xCD, 0xF8, 0x16, 0x3F, name="IDebugSymbols2", strid="3A707211-AFDD-4495-AD4F-56FECDF8163F")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetSymbolOptions -> Options:PULONG
 "GetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetSymbolOptions"),
 #AddSymbolOptions -> Options:ULONG
 "AddSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "AddSymbolOptions"),
 #RemoveSymbolOptions -> Options:ULONG
 "RemoveSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(5, "RemoveSymbolOptions"),
 #SetSymbolOptions -> Options:ULONG
 "SetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetSymbolOptions"),
 #GetNameByOffset -> Offset:ULONG64, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(7, "GetNameByOffset"),
 #GetOffsetByName -> Symbol:PCSTR, Offset:PULONG64
 "GetOffsetByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(8, "GetOffsetByName"),
 #GetNearNameByOffset -> Offset:ULONG64, Delta:LONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNearNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PSTR, ULONG, PULONG, PULONG64)(9, "GetNearNameByOffset"),
 #GetLineByOffset -> Offset:ULONG64, Line:PULONG, FileBuffer:PSTR, FileBufferSize:ULONG, FileSize:PULONG, Displacement:PULONG64
 "GetLineByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PSTR, ULONG, PULONG, PULONG64)(10, "GetLineByOffset"),
 #GetOffsetByLine -> Line:ULONG, File:PCSTR, Offset:PULONG64
 "GetOffsetByLine": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PULONG64)(11, "GetOffsetByLine"),
 #GetNumberModules -> Loaded:PULONG, Unloaded:PULONG
 "GetNumberModules": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(12, "GetNumberModules"),
 #GetModuleByIndex -> Index:ULONG, Base:PULONG64
 "GetModuleByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(13, "GetModuleByIndex"),
 #GetModuleByModuleName -> Name:PCSTR, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG, PULONG64)(14, "GetModuleByModuleName"),
 #GetModuleByOffset -> Offset:ULONG64, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG, PULONG64)(15, "GetModuleByOffset"),
 #GetModuleNames -> Index:ULONG, Base:ULONG64, ImageNameBuffer:PSTR, ImageNameBufferSize:ULONG, ImageNameSize:PULONG, ModuleNameBuffer:PSTR, ModuleNameBufferSize:ULONG, ModuleNameSize:PULONG, LoadedImageNameBuffer:PSTR, LoadedImageNameBufferSize:ULONG, LoadedImageNameSize:PULONG
 "GetModuleNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(16, "GetModuleNames"),
 #GetModuleParameters -> Count:ULONG, Bases:PULONG64, Start:ULONG, Params:PDEBUG_MODULE_PARAMETERS
 "GetModuleParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64, ULONG, PDEBUG_MODULE_PARAMETERS)(17, "GetModuleParameters"),
 #GetSymbolModule -> Symbol:PCSTR, Base:PULONG64
 "GetSymbolModule": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(18, "GetSymbolModule"),
 #GetTypeName -> Module:ULONG64, TypeId:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetTypeName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG)(19, "GetTypeName"),
 #GetTypeId -> Module:ULONG64, Name:PCSTR, TypeId:PULONG
 "GetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG)(20, "GetTypeId"),
 #GetTypeSize -> Module:ULONG64, TypeId:ULONG, Size:PULONG
 "GetTypeSize": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG)(21, "GetTypeSize"),
 #GetFieldOffset -> Module:ULONG64, TypeId:ULONG, Field:PCSTR, Offset:PULONG
 "GetFieldOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, PULONG)(22, "GetFieldOffset"),
 #GetSymbolTypeId -> Symbol:PCSTR, TypeId:PULONG, Module:PULONG64
 "GetSymbolTypeId": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG, PULONG64)(23, "GetSymbolTypeId"),
 #GetOffsetTypeId -> Offset:ULONG64, TypeId:PULONG, Module:PULONG64
 "GetOffsetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PULONG64)(24, "GetOffsetTypeId"),
 #ReadTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadTypedDataVirtual"),
 #WriteTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "WriteTypedDataVirtual"),
 #OutputTypedDataVirtual -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(27, "OutputTypedDataVirtual"),
 #ReadTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(28, "ReadTypedDataPhysical"),
 #WriteTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(29, "WriteTypedDataPhysical"),
 #OutputTypedDataPhysical -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(30, "OutputTypedDataPhysical"),
 #GetScope -> InstructionOffset:PULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "GetScope": ctypes.WINFUNCTYPE(HRESULT, PULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(31, "GetScope"),
 #SetScope -> InstructionOffset:ULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "SetScope": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(32, "SetScope"),
 #ResetScope -> 
 "ResetScope": ctypes.WINFUNCTYPE(HRESULT)(33, "ResetScope"),
 #GetScopeSymbolGroup -> Flags:ULONG, Update:PDEBUG_SYMBOL_GROUP2, Symbols:*PDEBUG_SYMBOL_GROUP2
 "GetScopeSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, PVOID)(34, "GetScopeSymbolGroup"),
 #CreateSymbolGroup -> Group:*PDEBUG_SYMBOL_GROUP2
 "CreateSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, PVOID)(35, "CreateSymbolGroup"),
 #StartSymbolMatch -> Pattern:PCSTR, Handle:PULONG64
 "StartSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(36, "StartSymbolMatch"),
 #GetNextSymbolMatch -> Handle:ULONG64, Buffer:PSTR, BufferSize:ULONG, MatchSize:PULONG, Offset:PULONG64
 "GetNextSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(37, "GetNextSymbolMatch"),
 #EndSymbolMatch -> Handle:ULONG64
 "EndSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(38, "EndSymbolMatch"),
 #Reload -> Module:PCSTR
 "Reload": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(39, "Reload"),
 #GetSymbolPath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(40, "GetSymbolPath"),
 #SetSymbolPath -> Path:PCSTR
 "SetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(41, "SetSymbolPath"),
 #AppendSymbolPath -> Addition:PCSTR
 "AppendSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "AppendSymbolPath"),
 #GetImagePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetImagePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetImagePath"),
 #SetImagePath -> Path:PCSTR
 "SetImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(44, "SetImagePath"),
 #AppendImagePath -> Addition:PCSTR
 "AppendImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(45, "AppendImagePath"),
 #GetSourcePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(46, "GetSourcePath"),
 #GetSourcePathElement -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ElementSize:PULONG
 "GetSourcePathElement": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(47, "GetSourcePathElement"),
 #SetSourcePath -> Path:PCSTR
 "SetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(48, "SetSourcePath"),
 #AppendSourcePath -> Addition:PCSTR
 "AppendSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(49, "AppendSourcePath"),
 #FindSourceFile -> StartElement:ULONG, File:PCSTR, Flags:ULONG, FoundElement:PULONG, Buffer:PSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(50, "FindSourceFile"),
 #GetSourceFileLineOffsets -> File:PCSTR, Buffer:PULONG64, BufferLines:ULONG, FileLines:PULONG
 "GetSourceFileLineOffsets": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64, ULONG, PULONG)(51, "GetSourceFileLineOffsets"),
 #GetModuleVersionInformation -> Index:ULONG, Base:ULONG64, Item:PCSTR, Buffer:PVOID, BufferSize:ULONG, VerInfoSize:PULONG
 "GetModuleVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCSTR, PVOID, ULONG, PULONG)(52, "GetModuleVersionInformation"),
 #GetModuleNameString -> Which:ULONG, Index:ULONG, Base:ULONG64, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetModuleNameString": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64, PSTR, ULONG, PULONG)(53, "GetModuleNameString"),
 #GetConstantName -> Module:ULONG64, TypeId:ULONG, Value:ULONG64, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetConstantName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG64, PSTR, ULONG, PULONG)(54, "GetConstantName"),
 #GetFieldName -> Module:ULONG64, TypeId:ULONG, FieldIndex:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetFieldName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG)(55, "GetFieldName"),
 #GetTypeOptions -> Options:PULONG
 "GetTypeOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(56, "GetTypeOptions"),
 #AddTypeOptions -> Options:ULONG
 "AddTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(57, "AddTypeOptions"),
 #RemoveTypeOptions -> Options:ULONG
 "RemoveTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(58, "RemoveTypeOptions"),
 #SetTypeOptions -> Options:ULONG
 "SetTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(59, "SetTypeOptions"),
    }


class IDebugSymbols3(COMInterface):
    IID = generate_IID(0xF02FBECC, 0x50AC, 0x4F36, 0x9A, 0xD9, 0xC9, 0x75, 0xE8, 0xF3, 0x2F, 0xF8, name="IDebugSymbols3", strid="F02FBECC-50AC-4F36-9AD9-C975E8F32FF8")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetSymbolOptions -> Options:PULONG
 "GetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetSymbolOptions"),
 #AddSymbolOptions -> Options:ULONG
 "AddSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(4, "AddSymbolOptions"),
 #RemoveSymbolOptions -> Options:ULONG
 "RemoveSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(5, "RemoveSymbolOptions"),
 #SetSymbolOptions -> Options:ULONG
 "SetSymbolOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetSymbolOptions"),
 #GetNameByOffset -> Offset:ULONG64, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(7, "GetNameByOffset"),
 #GetOffsetByName -> Symbol:PCSTR, Offset:PULONG64
 "GetOffsetByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(8, "GetOffsetByName"),
 #GetNearNameByOffset -> Offset:ULONG64, Delta:LONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNearNameByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PSTR, ULONG, PULONG, PULONG64)(9, "GetNearNameByOffset"),
 #GetLineByOffset -> Offset:ULONG64, Line:PULONG, FileBuffer:PSTR, FileBufferSize:ULONG, FileSize:PULONG, Displacement:PULONG64
 "GetLineByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PSTR, ULONG, PULONG, PULONG64)(10, "GetLineByOffset"),
 #GetOffsetByLine -> Line:ULONG, File:PCSTR, Offset:PULONG64
 "GetOffsetByLine": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, PULONG64)(11, "GetOffsetByLine"),
 #GetNumberModules -> Loaded:PULONG, Unloaded:PULONG
 "GetNumberModules": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(12, "GetNumberModules"),
 #GetModuleByIndex -> Index:ULONG, Base:PULONG64
 "GetModuleByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64)(13, "GetModuleByIndex"),
 #GetModuleByModuleName -> Name:PCSTR, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PULONG, PULONG64)(14, "GetModuleByModuleName"),
 #GetModuleByOffset -> Offset:ULONG64, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG, PULONG64)(15, "GetModuleByOffset"),
 #GetModuleNames -> Index:ULONG, Base:ULONG64, ImageNameBuffer:PSTR, ImageNameBufferSize:ULONG, ImageNameSize:PULONG, ModuleNameBuffer:PSTR, ModuleNameBufferSize:ULONG, ModuleNameSize:PULONG, LoadedImageNameBuffer:PSTR, LoadedImageNameBufferSize:ULONG, LoadedImageNameSize:PULONG
 "GetModuleNames": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(16, "GetModuleNames"),
 #GetModuleParameters -> Count:ULONG, Bases:PULONG64, Start:ULONG, Params:PDEBUG_MODULE_PARAMETERS
 "GetModuleParameters": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG64, ULONG, PDEBUG_MODULE_PARAMETERS)(17, "GetModuleParameters"),
 #GetSymbolModule -> Symbol:PCSTR, Base:PULONG64
 "GetSymbolModule": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(18, "GetSymbolModule"),
 #GetTypeName -> Module:ULONG64, TypeId:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetTypeName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PSTR, ULONG, PULONG)(19, "GetTypeName"),
 #GetTypeId -> Module:ULONG64, Name:PCSTR, TypeId:PULONG
 "GetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCSTR, PULONG)(20, "GetTypeId"),
 #GetTypeSize -> Module:ULONG64, TypeId:ULONG, Size:PULONG
 "GetTypeSize": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PULONG)(21, "GetTypeSize"),
 #GetFieldOffset -> Module:ULONG64, TypeId:ULONG, Field:PCSTR, Offset:PULONG
 "GetFieldOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, PULONG)(22, "GetFieldOffset"),
 #GetSymbolTypeId -> Symbol:PCSTR, TypeId:PULONG, Module:PULONG64
 "GetSymbolTypeId": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG, PULONG64)(23, "GetSymbolTypeId"),
 #GetOffsetTypeId -> Offset:ULONG64, TypeId:PULONG, Module:PULONG64
 "GetOffsetTypeId": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PULONG64)(24, "GetOffsetTypeId"),
 #ReadTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(25, "ReadTypedDataVirtual"),
 #WriteTypedDataVirtual -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(26, "WriteTypedDataVirtual"),
 #OutputTypedDataVirtual -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataVirtual": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(27, "OutputTypedDataVirtual"),
 #ReadTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesRead:PULONG
 "ReadTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(28, "ReadTypedDataPhysical"),
 #WriteTypedDataPhysical -> Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Buffer:PVOID, BufferSize:ULONG, BytesWritten:PULONG
 "WriteTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG64, ULONG, PVOID, ULONG, PULONG)(29, "WriteTypedDataPhysical"),
 #OutputTypedDataPhysical -> OutputControl:ULONG, Offset:ULONG64, Module:ULONG64, TypeId:ULONG, Flags:ULONG
 "OutputTypedDataPhysical": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, ULONG64, ULONG, ULONG)(30, "OutputTypedDataPhysical"),
 #GetScope -> InstructionOffset:PULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "GetScope": ctypes.WINFUNCTYPE(HRESULT, PULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(31, "GetScope"),
 #SetScope -> InstructionOffset:ULONG64, ScopeFrame:PDEBUG_STACK_FRAME, ScopeContext:PVOID, ScopeContextSize:ULONG
 "SetScope": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PDEBUG_STACK_FRAME, PVOID, ULONG)(32, "SetScope"),
 #ResetScope -> 
 "ResetScope": ctypes.WINFUNCTYPE(HRESULT)(33, "ResetScope"),
 #GetScopeSymbolGroup -> Flags:ULONG, Update:PDEBUG_SYMBOL_GROUP2, Symbols:*PDEBUG_SYMBOL_GROUP2
 "GetScopeSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, PVOID)(34, "GetScopeSymbolGroup"),
 #CreateSymbolGroup -> Group:*PDEBUG_SYMBOL_GROUP2
 "CreateSymbolGroup": ctypes.WINFUNCTYPE(HRESULT, PVOID)(35, "CreateSymbolGroup"),
 #StartSymbolMatch -> Pattern:PCSTR, Handle:PULONG64
 "StartSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64)(36, "StartSymbolMatch"),
 #GetNextSymbolMatch -> Handle:ULONG64, Buffer:PSTR, BufferSize:ULONG, MatchSize:PULONG, Offset:PULONG64
 "GetNextSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PSTR, ULONG, PULONG, PULONG64)(37, "GetNextSymbolMatch"),
 #EndSymbolMatch -> Handle:ULONG64
 "EndSymbolMatch": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(38, "EndSymbolMatch"),
 #Reload -> Module:PCSTR
 "Reload": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(39, "Reload"),
 #GetSymbolPath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(40, "GetSymbolPath"),
 #SetSymbolPath -> Path:PCSTR
 "SetSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(41, "SetSymbolPath"),
 #AppendSymbolPath -> Addition:PCSTR
 "AppendSymbolPath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(42, "AppendSymbolPath"),
 #GetImagePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetImagePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(43, "GetImagePath"),
 #SetImagePath -> Path:PCSTR
 "SetImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(44, "SetImagePath"),
 #AppendImagePath -> Addition:PCSTR
 "AppendImagePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(45, "AppendImagePath"),
 #GetSourcePath -> Buffer:PSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(46, "GetSourcePath"),
 #GetSourcePathElement -> Index:ULONG, Buffer:PSTR, BufferSize:ULONG, ElementSize:PULONG
 "GetSourcePathElement": ctypes.WINFUNCTYPE(HRESULT, ULONG, PSTR, ULONG, PULONG)(47, "GetSourcePathElement"),
 #SetSourcePath -> Path:PCSTR
 "SetSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(48, "SetSourcePath"),
 #AppendSourcePath -> Addition:PCSTR
 "AppendSourcePath": ctypes.WINFUNCTYPE(HRESULT, PCSTR)(49, "AppendSourcePath"),
 #FindSourceFile -> StartElement:ULONG, File:PCSTR, Flags:ULONG, FoundElement:PULONG, Buffer:PSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFile": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG, PULONG, PSTR, ULONG, PULONG)(50, "FindSourceFile"),
 #GetSourceFileLineOffsets -> File:PCSTR, Buffer:PULONG64, BufferLines:ULONG, FileLines:PULONG
 "GetSourceFileLineOffsets": ctypes.WINFUNCTYPE(HRESULT, PCSTR, PULONG64, ULONG, PULONG)(51, "GetSourceFileLineOffsets"),
 #GetModuleVersionInformation -> Index:ULONG, Base:ULONG64, Item:PCSTR, Buffer:PVOID, BufferSize:ULONG, VerInfoSize:PULONG
 "GetModuleVersionInformation": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCSTR, PVOID, ULONG, PULONG)(52, "GetModuleVersionInformation"),
 #GetModuleNameString -> Which:ULONG, Index:ULONG, Base:ULONG64, Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetModuleNameString": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64, PSTR, ULONG, PULONG)(53, "GetModuleNameString"),
 #GetConstantName -> Module:ULONG64, TypeId:ULONG, Value:ULONG64, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetConstantName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG64, PSTR, ULONG, PULONG)(54, "GetConstantName"),
 #GetFieldName -> Module:ULONG64, TypeId:ULONG, FieldIndex:ULONG, NameBuffer:PSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetFieldName": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PSTR, ULONG, PULONG)(55, "GetFieldName"),
 #GetTypeOptions -> Options:PULONG
 "GetTypeOptions": ctypes.WINFUNCTYPE(HRESULT, PULONG)(56, "GetTypeOptions"),
 #AddTypeOptions -> Options:ULONG
 "AddTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(57, "AddTypeOptions"),
 #RemoveTypeOptions -> Options:ULONG
 "RemoveTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(58, "RemoveTypeOptions"),
 #SetTypeOptions -> Options:ULONG
 "SetTypeOptions": ctypes.WINFUNCTYPE(HRESULT, ULONG)(59, "SetTypeOptions"),
 #GetNameByOffsetWide -> Offset:ULONG64, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNameByOffsetWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG, PULONG, PULONG64)(60, "GetNameByOffsetWide"),
 #GetOffsetByNameWide -> Symbol:PCWSTR, Offset:PULONG64
 "GetOffsetByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(61, "GetOffsetByNameWide"),
 #GetNearNameByOffsetWide -> Offset:ULONG64, Delta:LONG, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG, Displacement:PULONG64
 "GetNearNameByOffsetWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, LONG, PWSTR, ULONG, PULONG, PULONG64)(62, "GetNearNameByOffsetWide"),
 #GetLineByOffsetWide -> Offset:ULONG64, Line:PULONG, FileBuffer:PWSTR, FileBufferSize:ULONG, FileSize:PULONG, Displacement:PULONG64
 "GetLineByOffsetWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG, PWSTR, ULONG, PULONG, PULONG64)(63, "GetLineByOffsetWide"),
 #GetOffsetByLineWide -> Line:ULONG, File:PCWSTR, Offset:PULONG64
 "GetOffsetByLineWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, PULONG64)(64, "GetOffsetByLineWide"),
 #GetModuleByModuleNameWide -> Name:PCWSTR, StartIndex:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, PULONG, PULONG64)(65, "GetModuleByModuleNameWide"),
 #GetSymbolModuleWide -> Symbol:PCWSTR, Base:PULONG64
 "GetSymbolModuleWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(66, "GetSymbolModuleWide"),
 #GetTypeNameWide -> Module:ULONG64, TypeId:ULONG, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetTypeNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PWSTR, ULONG, PULONG)(67, "GetTypeNameWide"),
 #GetTypeIdWide -> Module:ULONG64, Name:PCWSTR, TypeId:PULONG
 "GetTypeIdWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PCWSTR, PULONG)(68, "GetTypeIdWide"),
 #GetFieldOffsetWide -> Module:ULONG64, TypeId:ULONG, Field:PCWSTR, Offset:PULONG
 "GetFieldOffsetWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCWSTR, PULONG)(69, "GetFieldOffsetWide"),
 #GetSymbolTypeIdWide -> Symbol:PCWSTR, TypeId:PULONG, Module:PULONG64
 "GetSymbolTypeIdWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG, PULONG64)(70, "GetSymbolTypeIdWide"),
 #GetScopeSymbolGroup2 -> Flags:ULONG, Update:PDEBUG_SYMBOL_GROUP2, Symbols:*PDEBUG_SYMBOL_GROUP2
 "GetScopeSymbolGroup2": ctypes.WINFUNCTYPE(HRESULT, ULONG, PVOID, PVOID)(71, "GetScopeSymbolGroup2"),
 #CreateSymbolGroup2 -> Group:*PDEBUG_SYMBOL_GROUP2
 "CreateSymbolGroup2": ctypes.WINFUNCTYPE(HRESULT, PVOID)(72, "CreateSymbolGroup2"),
 #StartSymbolMatchWide -> Pattern:PCWSTR, Handle:PULONG64
 "StartSymbolMatchWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64)(73, "StartSymbolMatchWide"),
 #GetNextSymbolMatchWide -> Handle:ULONG64, Buffer:PWSTR, BufferSize:ULONG, MatchSize:PULONG, Offset:PULONG64
 "GetNextSymbolMatchWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PWSTR, ULONG, PULONG, PULONG64)(74, "GetNextSymbolMatchWide"),
 #ReloadWide -> Module:PCWSTR
 "ReloadWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(75, "ReloadWide"),
 #GetSymbolPathWide -> Buffer:PWSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSymbolPathWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(76, "GetSymbolPathWide"),
 #SetSymbolPathWide -> Path:PCWSTR
 "SetSymbolPathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(77, "SetSymbolPathWide"),
 #AppendSymbolPathWide -> Addition:PCWSTR
 "AppendSymbolPathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(78, "AppendSymbolPathWide"),
 #GetImagePathWide -> Buffer:PWSTR, BufferSize:ULONG, PathSize:PULONG
 "GetImagePathWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(79, "GetImagePathWide"),
 #SetImagePathWide -> Path:PCWSTR
 "SetImagePathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(80, "SetImagePathWide"),
 #AppendImagePathWide -> Addition:PCWSTR
 "AppendImagePathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(81, "AppendImagePathWide"),
 #GetSourcePathWide -> Buffer:PWSTR, BufferSize:ULONG, PathSize:PULONG
 "GetSourcePathWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(82, "GetSourcePathWide"),
 #GetSourcePathElementWide -> Index:ULONG, Buffer:PWSTR, BufferSize:ULONG, ElementSize:PULONG
 "GetSourcePathElementWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PWSTR, ULONG, PULONG)(83, "GetSourcePathElementWide"),
 #SetSourcePathWide -> Path:PCWSTR
 "SetSourcePathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(84, "SetSourcePathWide"),
 #AppendSourcePathWide -> Addition:PCWSTR
 "AppendSourcePathWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR)(85, "AppendSourcePathWide"),
 #FindSourceFileWide -> StartElement:ULONG, File:PCWSTR, Flags:ULONG, FoundElement:PULONG, Buffer:PWSTR, BufferSize:ULONG, FoundSize:PULONG
 "FindSourceFileWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, ULONG, PULONG, PWSTR, ULONG, PULONG)(86, "FindSourceFileWide"),
 #GetSourceFileLineOffsetsWide -> File:PCWSTR, Buffer:PULONG64, BufferLines:ULONG, FileLines:PULONG
 "GetSourceFileLineOffsetsWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, PULONG64, ULONG, PULONG)(87, "GetSourceFileLineOffsetsWide"),
 #GetModuleVersionInformationWide -> Index:ULONG, Base:ULONG64, Item:PCWSTR, Buffer:PVOID, BufferSize:ULONG, VerInfoSize:PULONG
 "GetModuleVersionInformationWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64, PCWSTR, PVOID, ULONG, PULONG)(88, "GetModuleVersionInformationWide"),
 #GetModuleNameStringWide -> Which:ULONG, Index:ULONG, Base:ULONG64, Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG
 "GetModuleNameStringWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64, PWSTR, ULONG, PULONG)(89, "GetModuleNameStringWide"),
 #GetConstantNameWide -> Module:ULONG64, TypeId:ULONG, Value:ULONG64, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetConstantNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG64, PWSTR, ULONG, PULONG)(90, "GetConstantNameWide"),
 #GetFieldNameWide -> Module:ULONG64, TypeId:ULONG, FieldIndex:ULONG, NameBuffer:PWSTR, NameBufferSize:ULONG, NameSize:PULONG
 "GetFieldNameWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PWSTR, ULONG, PULONG)(91, "GetFieldNameWide"),
 #IsManagedModule -> Index:ULONG, Base:ULONG64
 "IsManagedModule": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(92, "IsManagedModule"),
 #GetModuleByModuleName2 -> Name:PCSTR, StartIndex:ULONG, Flags:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleName2": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, ULONG, PULONG, PULONG64)(93, "GetModuleByModuleName2"),
 #GetModuleByModuleName2Wide -> Name:PCWSTR, StartIndex:ULONG, Flags:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByModuleName2Wide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, ULONG, PULONG, PULONG64)(94, "GetModuleByModuleName2Wide"),
 #GetModuleByOffset2 -> Offset:ULONG64, StartIndex:ULONG, Flags:ULONG, Index:PULONG, Base:PULONG64
 "GetModuleByOffset2": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, ULONG, PULONG, PULONG64)(95, "GetModuleByOffset2"),
 #AddSyntheticModule -> Base:ULONG64, Size:ULONG, ImagePath:PCSTR, ModuleName:PCSTR, Flags:ULONG
 "AddSyntheticModule": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, PCSTR, ULONG)(96, "AddSyntheticModule"),
 #AddSyntheticModuleWide -> Base:ULONG64, Size:ULONG, ImagePath:PCWSTR, ModuleName:PCWSTR, Flags:ULONG
 "AddSyntheticModuleWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCWSTR, PCWSTR, ULONG)(97, "AddSyntheticModuleWide"),
 #RemoveSyntheticModule -> Base:ULONG64
 "RemoveSyntheticModule": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(98, "RemoveSyntheticModule"),
 #GetCurrentScopeFrameIndex -> Index:PULONG
 "GetCurrentScopeFrameIndex": ctypes.WINFUNCTYPE(HRESULT, PULONG)(99, "GetCurrentScopeFrameIndex"),
 #SetScopeFrameByIndex -> Index:ULONG
 "SetScopeFrameByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG)(100, "SetScopeFrameByIndex"),
 #SetScopeFromJitDebugInfo -> OutputControl:ULONG, InfoOffset:ULONG64
 "SetScopeFromJitDebugInfo": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG64)(101, "SetScopeFromJitDebugInfo"),
 #SetScopeFromStoredEvent -> 
 "SetScopeFromStoredEvent": ctypes.WINFUNCTYPE(HRESULT)(102, "SetScopeFromStoredEvent"),
 #OutputSymbolByOffset -> OutputControl:ULONG, Flags:ULONG, Offset:ULONG64
 "OutputSymbolByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, ULONG64)(103, "OutputSymbolByOffset"),
 #GetFunctionEntryByOffset -> Offset:ULONG64, Flags:ULONG, Buffer:PVOID, BufferSize:ULONG, BufferNeeded:PULONG
 "GetFunctionEntryByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PVOID, ULONG, PULONG)(104, "GetFunctionEntryByOffset"),
 #GetFieldTypeAndOffset -> Module:ULONG64, ContainerTypeId:ULONG, Field:PCSTR, FieldTypeId:PULONG, Offset:PULONG
 "GetFieldTypeAndOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, PULONG, PULONG)(105, "GetFieldTypeAndOffset"),
 #GetFieldTypeAndOffsetWide -> Module:ULONG64, ContainerTypeId:ULONG, Field:PCWSTR, FieldTypeId:PULONG, Offset:PULONG
 "GetFieldTypeAndOffsetWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCWSTR, PULONG, PULONG)(106, "GetFieldTypeAndOffsetWide"),
 #AddSyntheticSymbol -> Offset:ULONG64, Size:ULONG, Name:PCSTR, Flags:ULONG, Id:PDEBUG_MODULE_AND_ID
 "AddSyntheticSymbol": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCSTR, ULONG, PDEBUG_MODULE_AND_ID)(107, "AddSyntheticSymbol"),
 #AddSyntheticSymbolWide -> Offset:ULONG64, Size:ULONG, Name:PCWSTR, Flags:ULONG, Id:PDEBUG_MODULE_AND_ID
 "AddSyntheticSymbolWide": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PCWSTR, ULONG, PDEBUG_MODULE_AND_ID)(108, "AddSyntheticSymbolWide"),
 #RemoveSyntheticSymbol -> Id:PDEBUG_MODULE_AND_ID
 "RemoveSyntheticSymbol": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID)(109, "RemoveSyntheticSymbol"),
 #GetSymbolEntriesByOffset -> Offset:ULONG64, Flags:ULONG, Ids:PDEBUG_MODULE_AND_ID, Displacements:PULONG64, IdsCount:ULONG, Entries:PULONG
 "GetSymbolEntriesByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PDEBUG_MODULE_AND_ID, PULONG64, ULONG, PULONG)(110, "GetSymbolEntriesByOffset"),
 #GetSymbolEntriesByName -> Symbol:PCSTR, Flags:ULONG, Ids:PDEBUG_MODULE_AND_ID, IdsCount:ULONG, Entries:PULONG
 "GetSymbolEntriesByName": ctypes.WINFUNCTYPE(HRESULT, PCSTR, ULONG, PDEBUG_MODULE_AND_ID, ULONG, PULONG)(111, "GetSymbolEntriesByName"),
 #GetSymbolEntriesByNameWide -> Symbol:PCWSTR, Flags:ULONG, Ids:PDEBUG_MODULE_AND_ID, IdsCount:ULONG, Entries:PULONG
 "GetSymbolEntriesByNameWide": ctypes.WINFUNCTYPE(HRESULT, PCWSTR, ULONG, PDEBUG_MODULE_AND_ID, ULONG, PULONG)(112, "GetSymbolEntriesByNameWide"),
 #GetSymbolEntryByToken -> ModuleBase:ULONG64, Token:ULONG, Id:PDEBUG_MODULE_AND_ID
 "GetSymbolEntryByToken": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PDEBUG_MODULE_AND_ID)(113, "GetSymbolEntryByToken"),
 #GetSymbolEntryInformation -> Id:PDEBUG_MODULE_AND_ID, Info:PDEBUG_SYMBOL_ENTRY
 "GetSymbolEntryInformation": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID, PDEBUG_SYMBOL_ENTRY)(114, "GetSymbolEntryInformation"),
 #GetSymbolEntryString -> Id:PDEBUG_MODULE_AND_ID, Which:ULONG, Buffer:PSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSymbolEntryString": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID, ULONG, PSTR, ULONG, PULONG)(115, "GetSymbolEntryString"),
 #GetSymbolEntryStringWide -> Id:PDEBUG_MODULE_AND_ID, Which:ULONG, Buffer:PWSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSymbolEntryStringWide": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID, ULONG, PWSTR, ULONG, PULONG)(116, "GetSymbolEntryStringWide"),
 #GetSymbolEntryOffsetRegions -> Id:PDEBUG_MODULE_AND_ID, Flags:ULONG, Regions:PDEBUG_OFFSET_REGION, RegionsCount:ULONG, RegionsAvail:PULONG
 "GetSymbolEntryOffsetRegions": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID, ULONG, PDEBUG_OFFSET_REGION, ULONG, PULONG)(117, "GetSymbolEntryOffsetRegions"),
 #GetSymbolEntryBySymbolEntry -> FromId:PDEBUG_MODULE_AND_ID, Flags:ULONG, ToId:PDEBUG_MODULE_AND_ID
 "GetSymbolEntryBySymbolEntry": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_MODULE_AND_ID, ULONG, PDEBUG_MODULE_AND_ID)(118, "GetSymbolEntryBySymbolEntry"),
 #GetSourceEntriesByOffset -> Offset:ULONG64, Flags:ULONG, Entries:PDEBUG_SYMBOL_SOURCE_ENTRY, EntriesCount:ULONG, EntriesAvail:PULONG
 "GetSourceEntriesByOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, ULONG, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PULONG)(119, "GetSourceEntriesByOffset"),
 #GetSourceEntriesByLine -> Line:ULONG, File:PCSTR, Flags:ULONG, Entries:PDEBUG_SYMBOL_SOURCE_ENTRY, EntriesCount:ULONG, EntriesAvail:PULONG
 "GetSourceEntriesByLine": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCSTR, ULONG, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PULONG)(120, "GetSourceEntriesByLine"),
 #GetSourceEntriesByLineWide -> Line:ULONG, File:PCWSTR, Flags:ULONG, Entries:PDEBUG_SYMBOL_SOURCE_ENTRY, EntriesCount:ULONG, EntriesAvail:PULONG
 "GetSourceEntriesByLineWide": ctypes.WINFUNCTYPE(HRESULT, ULONG, PCWSTR, ULONG, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PULONG)(121, "GetSourceEntriesByLineWide"),
 #GetSourceEntryString -> Entry:PDEBUG_SYMBOL_SOURCE_ENTRY, Which:ULONG, Buffer:PSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSourceEntryString": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PSTR, ULONG, PULONG)(122, "GetSourceEntryString"),
 #GetSourceEntryStringWide -> Entry:PDEBUG_SYMBOL_SOURCE_ENTRY, Which:ULONG, Buffer:PWSTR, BufferSize:ULONG, StringSize:PULONG
 "GetSourceEntryStringWide": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PWSTR, ULONG, PULONG)(123, "GetSourceEntryStringWide"),
 #GetSourceEntryOffsetRegions -> Entry:PDEBUG_SYMBOL_SOURCE_ENTRY, Flags:ULONG, Regions:PDEBUG_OFFSET_REGION, RegionsCount:ULONG, RegionsAvail:PULONG
 "GetSourceEntryOffsetRegions": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PDEBUG_OFFSET_REGION, ULONG, PULONG)(124, "GetSourceEntryOffsetRegions"),
 #GetSourceEntryBySourceEntry -> FromEntry:PDEBUG_SYMBOL_SOURCE_ENTRY, Flags:ULONG, ToEntry:PDEBUG_SYMBOL_SOURCE_ENTRY
 "GetSourceEntryBySourceEntry": ctypes.WINFUNCTYPE(HRESULT, PDEBUG_SYMBOL_SOURCE_ENTRY, ULONG, PDEBUG_SYMBOL_SOURCE_ENTRY)(125, "GetSourceEntryBySourceEntry"),
    }


class IDebugSystemObjects(COMInterface):
    IID = generate_IID(0x6B86FE2C, 0x2C4F, 0x4F0C, 0x9D, 0xA2, 0x17, 0x43, 0x11, 0xAC, 0xC3, 0x27, name="IDebugSystemObjects", strid="6B86FE2C-2C4F-4F0C-9DA2-174311ACC327")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetEventThread -> Id:PULONG
 "GetEventThread": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetEventThread"),
 #GetEventProcess -> Id:PULONG
 "GetEventProcess": ctypes.WINFUNCTYPE(HRESULT, PULONG)(4, "GetEventProcess"),
 #GetCurrentThreadId -> Id:PULONG
 "GetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetCurrentThreadId"),
 #SetCurrentThreadId -> Id:ULONG
 "SetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetCurrentThreadId"),
 #GetCurrentProcessId -> Id:PULONG
 "GetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(7, "GetCurrentProcessId"),
 #SetCurrentProcessId -> Id:ULONG
 "SetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "SetCurrentProcessId"),
 #GetNumberThreads -> Number:PULONG
 "GetNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG)(9, "GetNumberThreads"),
 #GetTotalNumberThreads -> Total:PULONG, LargestProcess:PULONG
 "GetTotalNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(10, "GetTotalNumberThreads"),
 #GetThreadIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetThreadIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(11, "GetThreadIdsByIndex"),
 #GetThreadIdByProcessor -> Processor:ULONG, Id:PULONG
 "GetThreadIdByProcessor": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(12, "GetThreadIdByProcessor"),
 #GetCurrentThreadDataOffset -> Offset:PULONG64
 "GetCurrentThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetCurrentThreadDataOffset"),
 #GetThreadIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(14, "GetThreadIdByDataOffset"),
 #GetCurrentThreadTeb -> Offset:PULONG64
 "GetCurrentThreadTeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(15, "GetCurrentThreadTeb"),
 #GetThreadIdByTeb -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByTeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(16, "GetThreadIdByTeb"),
 #GetCurrentThreadSystemId -> SysId:PULONG
 "GetCurrentThreadSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetCurrentThreadSystemId"),
 #GetThreadIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetThreadIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(18, "GetThreadIdBySystemId"),
 #GetCurrentThreadHandle -> Handle:PULONG64
 "GetCurrentThreadHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(19, "GetCurrentThreadHandle"),
 #GetThreadIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetThreadIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(20, "GetThreadIdByHandle"),
 #GetNumberProcesses -> Number:PULONG
 "GetNumberProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG)(21, "GetNumberProcesses"),
 #GetProcessIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetProcessIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(22, "GetProcessIdsByIndex"),
 #GetCurrentProcessDataOffset -> Offset:PULONG64
 "GetCurrentProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetCurrentProcessDataOffset"),
 #GetProcessIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(24, "GetProcessIdByDataOffset"),
 #GetCurrentProcessPeb -> Offset:PULONG64
 "GetCurrentProcessPeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(25, "GetCurrentProcessPeb"),
 #GetProcessIdByPeb -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByPeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(26, "GetProcessIdByPeb"),
 #GetCurrentProcessSystemId -> SysId:PULONG
 "GetCurrentProcessSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetCurrentProcessSystemId"),
 #GetProcessIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetProcessIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(28, "GetProcessIdBySystemId"),
 #GetCurrentProcessHandle -> Handle:PULONG64
 "GetCurrentProcessHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(29, "GetCurrentProcessHandle"),
 #GetProcessIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetProcessIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(30, "GetProcessIdByHandle"),
 #GetCurrentProcessExecutableName -> Buffer:PSTR, BufferSize:ULONG, ExeSize:PULONG
 "GetCurrentProcessExecutableName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(31, "GetCurrentProcessExecutableName"),
    }


class IDebugSystemObjects2(COMInterface):
    IID = generate_IID(0x0AE9F5FF, 0x1852, 0x4679, 0xB0, 0x55, 0x49, 0x4B, 0xEE, 0x64, 0x07, 0xEE, name="IDebugSystemObjects2", strid="0AE9F5FF-1852-4679-B055-494BEE6407EE")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetEventThread -> Id:PULONG
 "GetEventThread": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetEventThread"),
 #GetEventProcess -> Id:PULONG
 "GetEventProcess": ctypes.WINFUNCTYPE(HRESULT, PULONG)(4, "GetEventProcess"),
 #GetCurrentThreadId -> Id:PULONG
 "GetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetCurrentThreadId"),
 #SetCurrentThreadId -> Id:ULONG
 "SetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetCurrentThreadId"),
 #GetCurrentProcessId -> Id:PULONG
 "GetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(7, "GetCurrentProcessId"),
 #SetCurrentProcessId -> Id:ULONG
 "SetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "SetCurrentProcessId"),
 #GetNumberThreads -> Number:PULONG
 "GetNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG)(9, "GetNumberThreads"),
 #GetTotalNumberThreads -> Total:PULONG, LargestProcess:PULONG
 "GetTotalNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(10, "GetTotalNumberThreads"),
 #GetThreadIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetThreadIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(11, "GetThreadIdsByIndex"),
 #GetThreadIdByProcessor -> Processor:ULONG, Id:PULONG
 "GetThreadIdByProcessor": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(12, "GetThreadIdByProcessor"),
 #GetCurrentThreadDataOffset -> Offset:PULONG64
 "GetCurrentThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetCurrentThreadDataOffset"),
 #GetThreadIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(14, "GetThreadIdByDataOffset"),
 #GetCurrentThreadTeb -> Offset:PULONG64
 "GetCurrentThreadTeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(15, "GetCurrentThreadTeb"),
 #GetThreadIdByTeb -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByTeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(16, "GetThreadIdByTeb"),
 #GetCurrentThreadSystemId -> SysId:PULONG
 "GetCurrentThreadSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetCurrentThreadSystemId"),
 #GetThreadIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetThreadIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(18, "GetThreadIdBySystemId"),
 #GetCurrentThreadHandle -> Handle:PULONG64
 "GetCurrentThreadHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(19, "GetCurrentThreadHandle"),
 #GetThreadIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetThreadIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(20, "GetThreadIdByHandle"),
 #GetNumberProcesses -> Number:PULONG
 "GetNumberProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG)(21, "GetNumberProcesses"),
 #GetProcessIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetProcessIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(22, "GetProcessIdsByIndex"),
 #GetCurrentProcessDataOffset -> Offset:PULONG64
 "GetCurrentProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetCurrentProcessDataOffset"),
 #GetProcessIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(24, "GetProcessIdByDataOffset"),
 #GetCurrentProcessPeb -> Offset:PULONG64
 "GetCurrentProcessPeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(25, "GetCurrentProcessPeb"),
 #GetProcessIdByPeb -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByPeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(26, "GetProcessIdByPeb"),
 #GetCurrentProcessSystemId -> SysId:PULONG
 "GetCurrentProcessSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetCurrentProcessSystemId"),
 #GetProcessIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetProcessIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(28, "GetProcessIdBySystemId"),
 #GetCurrentProcessHandle -> Handle:PULONG64
 "GetCurrentProcessHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(29, "GetCurrentProcessHandle"),
 #GetProcessIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetProcessIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(30, "GetProcessIdByHandle"),
 #GetCurrentProcessExecutableName -> Buffer:PSTR, BufferSize:ULONG, ExeSize:PULONG
 "GetCurrentProcessExecutableName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(31, "GetCurrentProcessExecutableName"),
 #GetCurrentProcessUpTime -> UpTime:PULONG
 "GetCurrentProcessUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(32, "GetCurrentProcessUpTime"),
 #GetImplicitThreadDataOffset -> Offset:PULONG64
 "GetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(33, "GetImplicitThreadDataOffset"),
 #SetImplicitThreadDataOffset -> Offset:ULONG64
 "SetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(34, "SetImplicitThreadDataOffset"),
 #GetImplicitProcessDataOffset -> Offset:PULONG64
 "GetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(35, "GetImplicitProcessDataOffset"),
 #SetImplicitProcessDataOffset -> Offset:ULONG64
 "SetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(36, "SetImplicitProcessDataOffset"),
    }


class IDebugSystemObjects3(COMInterface):
    IID = generate_IID(0xE9676E2F, 0xE286, 0x4EA3, 0xB0, 0xF9, 0xDF, 0xE5, 0xD9, 0xFC, 0x33, 0x0E, name="IDebugSystemObjects3", strid="E9676E2F-E286-4EA3-B0F9-DFE5D9FC330E")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetEventThread -> Id:PULONG
 "GetEventThread": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetEventThread"),
 #GetEventProcess -> Id:PULONG
 "GetEventProcess": ctypes.WINFUNCTYPE(HRESULT, PULONG)(4, "GetEventProcess"),
 #GetCurrentThreadId -> Id:PULONG
 "GetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetCurrentThreadId"),
 #SetCurrentThreadId -> Id:ULONG
 "SetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetCurrentThreadId"),
 #GetCurrentProcessId -> Id:PULONG
 "GetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(7, "GetCurrentProcessId"),
 #SetCurrentProcessId -> Id:ULONG
 "SetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "SetCurrentProcessId"),
 #GetNumberThreads -> Number:PULONG
 "GetNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG)(9, "GetNumberThreads"),
 #GetTotalNumberThreads -> Total:PULONG, LargestProcess:PULONG
 "GetTotalNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(10, "GetTotalNumberThreads"),
 #GetThreadIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetThreadIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(11, "GetThreadIdsByIndex"),
 #GetThreadIdByProcessor -> Processor:ULONG, Id:PULONG
 "GetThreadIdByProcessor": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(12, "GetThreadIdByProcessor"),
 #GetCurrentThreadDataOffset -> Offset:PULONG64
 "GetCurrentThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetCurrentThreadDataOffset"),
 #GetThreadIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(14, "GetThreadIdByDataOffset"),
 #GetCurrentThreadTeb -> Offset:PULONG64
 "GetCurrentThreadTeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(15, "GetCurrentThreadTeb"),
 #GetThreadIdByTeb -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByTeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(16, "GetThreadIdByTeb"),
 #GetCurrentThreadSystemId -> SysId:PULONG
 "GetCurrentThreadSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetCurrentThreadSystemId"),
 #GetThreadIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetThreadIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(18, "GetThreadIdBySystemId"),
 #GetCurrentThreadHandle -> Handle:PULONG64
 "GetCurrentThreadHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(19, "GetCurrentThreadHandle"),
 #GetThreadIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetThreadIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(20, "GetThreadIdByHandle"),
 #GetNumberProcesses -> Number:PULONG
 "GetNumberProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG)(21, "GetNumberProcesses"),
 #GetProcessIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetProcessIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(22, "GetProcessIdsByIndex"),
 #GetCurrentProcessDataOffset -> Offset:PULONG64
 "GetCurrentProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetCurrentProcessDataOffset"),
 #GetProcessIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(24, "GetProcessIdByDataOffset"),
 #GetCurrentProcessPeb -> Offset:PULONG64
 "GetCurrentProcessPeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(25, "GetCurrentProcessPeb"),
 #GetProcessIdByPeb -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByPeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(26, "GetProcessIdByPeb"),
 #GetCurrentProcessSystemId -> SysId:PULONG
 "GetCurrentProcessSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetCurrentProcessSystemId"),
 #GetProcessIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetProcessIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(28, "GetProcessIdBySystemId"),
 #GetCurrentProcessHandle -> Handle:PULONG64
 "GetCurrentProcessHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(29, "GetCurrentProcessHandle"),
 #GetProcessIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetProcessIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(30, "GetProcessIdByHandle"),
 #GetCurrentProcessExecutableName -> Buffer:PSTR, BufferSize:ULONG, ExeSize:PULONG
 "GetCurrentProcessExecutableName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(31, "GetCurrentProcessExecutableName"),
 #GetCurrentProcessUpTime -> UpTime:PULONG
 "GetCurrentProcessUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(32, "GetCurrentProcessUpTime"),
 #GetImplicitThreadDataOffset -> Offset:PULONG64
 "GetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(33, "GetImplicitThreadDataOffset"),
 #SetImplicitThreadDataOffset -> Offset:ULONG64
 "SetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(34, "SetImplicitThreadDataOffset"),
 #GetImplicitProcessDataOffset -> Offset:PULONG64
 "GetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(35, "GetImplicitProcessDataOffset"),
 #SetImplicitProcessDataOffset -> Offset:ULONG64
 "SetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(36, "SetImplicitProcessDataOffset"),
 #GetEventSystem -> Id:PULONG
 "GetEventSystem": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetEventSystem"),
 #GetCurrentSystemId -> Id:PULONG
 "GetCurrentSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(38, "GetCurrentSystemId"),
 #SetCurrentSystemId -> Id:ULONG
 "SetCurrentSystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(39, "SetCurrentSystemId"),
 #GetNumberSystems -> Number:PULONG
 "GetNumberSystems": ctypes.WINFUNCTYPE(HRESULT, PULONG)(40, "GetNumberSystems"),
 #GetSystemIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG
 "GetSystemIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(41, "GetSystemIdsByIndex"),
 #GetTotalNumberThreadsAndProcesses -> TotalThreads:PULONG, TotalProcesses:PULONG, LargestProcessThreads:PULONG, LargestSystemThreads:PULONG, LargestSystemProcesses:PULONG
 "GetTotalNumberThreadsAndProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PULONG, PULONG)(42, "GetTotalNumberThreadsAndProcesses"),
 #GetCurrentSystemServer -> Server:PULONG64
 "GetCurrentSystemServer": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(43, "GetCurrentSystemServer"),
 #GetSystemByServer -> Server:ULONG64, Id:PULONG
 "GetSystemByServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(44, "GetSystemByServer"),
 #GetCurrentSystemServerName -> Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetCurrentSystemServerName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(45, "GetCurrentSystemServerName"),
    }


class IDebugSystemObjects4(COMInterface):
    IID = generate_IID(0x489468E6, 0x7D0F, 0x4AF5, 0x87, 0xAB, 0x25, 0x20, 0x74, 0x54, 0xD5, 0x53, name="IDebugSystemObjects4", strid="489468E6-7D0F-4AF5-87AB-25207454D553")

    _functions_ = {
 #QueryInterface -> InterfaceId:REFIID, Interface:*PVOID
 "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))(0, "QueryInterface"),
 #AddRef -> 
 "AddRef": ctypes.WINFUNCTYPE(ULONG)(1, "AddRef"),
 #Release -> 
 "Release": ctypes.WINFUNCTYPE(ULONG)(2, "Release"),
 #GetEventThread -> Id:PULONG
 "GetEventThread": ctypes.WINFUNCTYPE(HRESULT, PULONG)(3, "GetEventThread"),
 #GetEventProcess -> Id:PULONG
 "GetEventProcess": ctypes.WINFUNCTYPE(HRESULT, PULONG)(4, "GetEventProcess"),
 #GetCurrentThreadId -> Id:PULONG
 "GetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(5, "GetCurrentThreadId"),
 #SetCurrentThreadId -> Id:ULONG
 "SetCurrentThreadId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(6, "SetCurrentThreadId"),
 #GetCurrentProcessId -> Id:PULONG
 "GetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(7, "GetCurrentProcessId"),
 #SetCurrentProcessId -> Id:ULONG
 "SetCurrentProcessId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(8, "SetCurrentProcessId"),
 #GetNumberThreads -> Number:PULONG
 "GetNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG)(9, "GetNumberThreads"),
 #GetTotalNumberThreads -> Total:PULONG, LargestProcess:PULONG
 "GetTotalNumberThreads": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG)(10, "GetTotalNumberThreads"),
 #GetThreadIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetThreadIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(11, "GetThreadIdsByIndex"),
 #GetThreadIdByProcessor -> Processor:ULONG, Id:PULONG
 "GetThreadIdByProcessor": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(12, "GetThreadIdByProcessor"),
 #GetCurrentThreadDataOffset -> Offset:PULONG64
 "GetCurrentThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(13, "GetCurrentThreadDataOffset"),
 #GetThreadIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(14, "GetThreadIdByDataOffset"),
 #GetCurrentThreadTeb -> Offset:PULONG64
 "GetCurrentThreadTeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(15, "GetCurrentThreadTeb"),
 #GetThreadIdByTeb -> Offset:ULONG64, Id:PULONG
 "GetThreadIdByTeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(16, "GetThreadIdByTeb"),
 #GetCurrentThreadSystemId -> SysId:PULONG
 "GetCurrentThreadSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(17, "GetCurrentThreadSystemId"),
 #GetThreadIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetThreadIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(18, "GetThreadIdBySystemId"),
 #GetCurrentThreadHandle -> Handle:PULONG64
 "GetCurrentThreadHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(19, "GetCurrentThreadHandle"),
 #GetThreadIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetThreadIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(20, "GetThreadIdByHandle"),
 #GetNumberProcesses -> Number:PULONG
 "GetNumberProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG)(21, "GetNumberProcesses"),
 #GetProcessIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG, SysIds:PULONG
 "GetProcessIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG, PULONG)(22, "GetProcessIdsByIndex"),
 #GetCurrentProcessDataOffset -> Offset:PULONG64
 "GetCurrentProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(23, "GetCurrentProcessDataOffset"),
 #GetProcessIdByDataOffset -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(24, "GetProcessIdByDataOffset"),
 #GetCurrentProcessPeb -> Offset:PULONG64
 "GetCurrentProcessPeb": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(25, "GetCurrentProcessPeb"),
 #GetProcessIdByPeb -> Offset:ULONG64, Id:PULONG
 "GetProcessIdByPeb": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(26, "GetProcessIdByPeb"),
 #GetCurrentProcessSystemId -> SysId:PULONG
 "GetCurrentProcessSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(27, "GetCurrentProcessSystemId"),
 #GetProcessIdBySystemId -> SysId:ULONG, Id:PULONG
 "GetProcessIdBySystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG, PULONG)(28, "GetProcessIdBySystemId"),
 #GetCurrentProcessHandle -> Handle:PULONG64
 "GetCurrentProcessHandle": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(29, "GetCurrentProcessHandle"),
 #GetProcessIdByHandle -> Handle:ULONG64, Id:PULONG
 "GetProcessIdByHandle": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(30, "GetProcessIdByHandle"),
 #GetCurrentProcessExecutableName -> Buffer:PSTR, BufferSize:ULONG, ExeSize:PULONG
 "GetCurrentProcessExecutableName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(31, "GetCurrentProcessExecutableName"),
 #GetCurrentProcessUpTime -> UpTime:PULONG
 "GetCurrentProcessUpTime": ctypes.WINFUNCTYPE(HRESULT, PULONG)(32, "GetCurrentProcessUpTime"),
 #GetImplicitThreadDataOffset -> Offset:PULONG64
 "GetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(33, "GetImplicitThreadDataOffset"),
 #SetImplicitThreadDataOffset -> Offset:ULONG64
 "SetImplicitThreadDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(34, "SetImplicitThreadDataOffset"),
 #GetImplicitProcessDataOffset -> Offset:PULONG64
 "GetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(35, "GetImplicitProcessDataOffset"),
 #SetImplicitProcessDataOffset -> Offset:ULONG64
 "SetImplicitProcessDataOffset": ctypes.WINFUNCTYPE(HRESULT, ULONG64)(36, "SetImplicitProcessDataOffset"),
 #GetEventSystem -> Id:PULONG
 "GetEventSystem": ctypes.WINFUNCTYPE(HRESULT, PULONG)(37, "GetEventSystem"),
 #GetCurrentSystemId -> Id:PULONG
 "GetCurrentSystemId": ctypes.WINFUNCTYPE(HRESULT, PULONG)(38, "GetCurrentSystemId"),
 #SetCurrentSystemId -> Id:ULONG
 "SetCurrentSystemId": ctypes.WINFUNCTYPE(HRESULT, ULONG)(39, "SetCurrentSystemId"),
 #GetNumberSystems -> Number:PULONG
 "GetNumberSystems": ctypes.WINFUNCTYPE(HRESULT, PULONG)(40, "GetNumberSystems"),
 #GetSystemIdsByIndex -> Start:ULONG, Count:ULONG, Ids:PULONG
 "GetSystemIdsByIndex": ctypes.WINFUNCTYPE(HRESULT, ULONG, ULONG, PULONG)(41, "GetSystemIdsByIndex"),
 #GetTotalNumberThreadsAndProcesses -> TotalThreads:PULONG, TotalProcesses:PULONG, LargestProcessThreads:PULONG, LargestSystemThreads:PULONG, LargestSystemProcesses:PULONG
 "GetTotalNumberThreadsAndProcesses": ctypes.WINFUNCTYPE(HRESULT, PULONG, PULONG, PULONG, PULONG, PULONG)(42, "GetTotalNumberThreadsAndProcesses"),
 #GetCurrentSystemServer -> Server:PULONG64
 "GetCurrentSystemServer": ctypes.WINFUNCTYPE(HRESULT, PULONG64)(43, "GetCurrentSystemServer"),
 #GetSystemByServer -> Server:ULONG64, Id:PULONG
 "GetSystemByServer": ctypes.WINFUNCTYPE(HRESULT, ULONG64, PULONG)(44, "GetSystemByServer"),
 #GetCurrentSystemServerName -> Buffer:PSTR, BufferSize:ULONG, NameSize:PULONG
 "GetCurrentSystemServerName": ctypes.WINFUNCTYPE(HRESULT, PSTR, ULONG, PULONG)(45, "GetCurrentSystemServerName"),
 #GetCurrentProcessExecutableNameWide -> Buffer:PWSTR, BufferSize:ULONG, ExeSize:PULONG
 "GetCurrentProcessExecutableNameWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(46, "GetCurrentProcessExecutableNameWide"),
 #GetCurrentSystemServerNameWide -> Buffer:PWSTR, BufferSize:ULONG, NameSize:PULONG
 "GetCurrentSystemServerNameWide": ctypes.WINFUNCTYPE(HRESULT, PWSTR, ULONG, PULONG)(47, "GetCurrentSystemServerNameWide"),
    }
