#Generated file


from ctypes import *
from ctypes.wintypes import *
from lkd.dbgdef import *
from windows.generated_def.winstructs import *


functions = ['DebugCreate', 'SymGetTypeInfo']


#def DebugCreate(InterfaceId, Interface):
#    return DebugCreate.ctypes_function(InterfaceId, Interface)
DebugCreatePrototype = WINFUNCTYPE(HRESULT, REFIID, POINTER(PVOID))
DebugCreateParams = ((1, 'InterfaceId'), (1, 'Interface'))

#def SymGetTypeInfo(hProcess, ModBase, TypeId, GetType, pInfo):
#    return SymGetTypeInfo.ctypes_function(hProcess, ModBase, TypeId, GetType, pInfo)
SymGetTypeInfoPrototype = WINFUNCTYPE(BOOL, HANDLE, DWORD64, ULONG, IMAGEHLP_SYMBOL_TYPE_INFO, PVOID)
SymGetTypeInfoParams = ((1, 'hProcess'), (1, 'ModBase'), (1, 'TypeId'), (1, 'GetType'), (1, 'pInfo'))
