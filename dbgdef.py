from simple_com import get_IID_from_raw

# COM IID for the interface we need
IID_IDebugClient_raw = 0x27fe5639, 0x8407, 0x4f47, 0x83, 0x64, 0xee, 0x11, 0x8f, 0xb0, 0x8a, 0xc8
IID_IDebugDataSpaces_raw = 0x88f7dfab, 0x3ea7, 0x4c3a, 0xae, 0xfb, 0xc4, 0xe8, 0x10, 0x61, 0x73, 0xaa
IID_IDebugDataSpaces2_raw = 0x7a5e852f, 0x96e9, 0x468f, 0xac, 0x1b, 0x0b, 0x3a, 0xdd, 0xc4, 0xa0, 0x49
IID_IDebugSymbols_raw = 0x8c31e98c, 0x983a, 0x48a5, 0x90, 0x16, 0x6f, 0xe5, 0xd6, 0x67, 0xa9, 0x50
IID_IDebugSymbols2_raw = 0x3a707211, 0xafdd, 0x4495, 0xad, 0x4f, 0x56, 0xfe, 0xcd, 0xf8, 0x16, 0x3f
IID_IDebugSymbols3_raw = 0xf02fbecc, 0x50ac, 0x4f36, 0x9a, 0xd9, 0xc9, 0x75, 0xe8, 0xf3, 0x2f, 0xf8
IID_IDebugControl_raw = 0x5182e668, 0x105e, 0x416e, 0xad, 0x92, 0x24, 0xef, 0x80, 0x04, 0x24, 0xba
IID_IDebugRegisters_raw = 0xce289126, 0x9e84, 0x45a7, 0x93, 0x7e, 0x67, 0xbb, 0x18, 0x69, 0x14, 0x93

IID_IDebugClient = get_IID_from_raw(IID_IDebugClient_raw)
IID_IDebugDataSpaces = get_IID_from_raw(IID_IDebugDataSpaces_raw)
IID_IDebugDataSpaces2 = get_IID_from_raw(IID_IDebugDataSpaces2_raw)
IID_IDebugSymbols = get_IID_from_raw(IID_IDebugSymbols_raw)
IID_IDebugSymbols2 = get_IID_from_raw(IID_IDebugSymbols2_raw)
IID_IDebugSymbols3 = get_IID_from_raw(IID_IDebugSymbols3_raw)
IID_IDebugControl = get_IID_from_raw(IID_IDebugControl_raw)
IID_IDebugRegisters = get_IID_from_raw(IID_IDebugRegisters_raw)

# defines related to IDebug interfaces

# Symbol options for symopt:
SYMOPT_CASE_INSENSITIVE      = 0x00000001
SYMOPT_UNDNAME               = 0x00000002
SYMOPT_DEFERRED_LOADS        = 0x00000004
SYMOPT_LOAD_LINES            = 0x00000010
SYMOPT_OMAP_FIND_NEAREST     = 0x00000020
SYMOPT_NO_UNQUALIFIED_LOADS  = 0x00000100
SYMOPT_FAIL_CRITICAL_ERRORS  = 0x00000200
SYMOPT_AUTO_PUBLICS          = 0x00010000
SYMOPT_NO_IMAGE_SEARCH       = 0x00020000


DEBUG_ATTACH_LOCAL_KERNEL = 1
DEBUG_END_PASSIVE = 0
DEBUG_END_ACTIVE_DETACH = 0x00000002

SE_DEBUG_NAME          = "SeDebugPrivilege"

DEBUG_DATA_KPCR_OFFSET                          = 0
DEBUG_DATA_KPRCB_OFFSET                         = 1
DEBUG_DATA_KTHREAD_OFFSET                       = 2
DEBUG_DATA_BASE_TRANSLATION_VIRTUAL_OFFSET      = 3
DEBUG_DATA_PROCESSOR_IDENTIFICATION             = 4
DEBUG_DATA_PROCESSOR_SPEED                      = 5


# Values for MmMapLockedPagesSpecifyCache
UserMode = 1
MmNonCached = 0
NormalPagePriority = 16


DEBUG_VALUE_INVALID      = 0
DEBUG_VALUE_INT8         = 1
DEBUG_VALUE_INT16        = 2
DEBUG_VALUE_INT32        = 3
DEBUG_VALUE_INT64        = 4
DEBUG_VALUE_FLOAT32      = 5
DEBUG_VALUE_FLOAT64      = 6
DEBUG_VALUE_FLOAT80      = 7
DEBUG_VALUE_FLOAT82      = 8
DEBUG_VALUE_FLOAT128     = 9
DEBUG_VALUE_VECTOR64     = 10
DEBUG_VALUE_VECTOR128    = 11