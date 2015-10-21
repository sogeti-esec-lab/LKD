"""A simple demonstration of LKD to display IDT and KINTERRUPT associated"""
import sys
import ctypes
import os

if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))

import windows
from windows.generated_def.winstructs import *
from dbginterface import LocalKernelDebugger


# lkd> dt nt!_KIDTENTRY
#    +0x000 Offset           : Uint2B
#    +0x002 Selector         : Uint2B
#    +0x004 Access           : Uint2B
#    +0x006 ExtendedOffset   : Uint2B
# Struct _IDT32 definitions
class _IDT32(ctypes.Structure):
        _fields_ = [
            ("Offset", WORD),
            ("Selector", WORD),
            ("Access", WORD),
            ("ExtendedOffset", WORD)
        ]
PIDT32 = POINTER(_IDT32)
IDT32 = _IDT32


# lkd> dt nt!_KIDTENTRY64
#  +0x000 OffsetLow        : Uint2B
#  +0x002 Selector         : Uint2B
#  +0x004 IstIndex         : Pos 0, 3 Bits
#  +0x004 Reserved0        : Pos 3, 5 Bits
#  +0x004 Type             : Pos 8, 5 Bits
#  +0x004 Dpl              : Pos 13, 2 Bits
#  +0x004 Present          : Pos 15, 1 Bit
#  +0x006 OffsetMiddle     : Uint2B
#  +0x008 OffsetHigh       : Uint4B
#  +0x00c Reserved1        : Uint4B
#  +0x000 Alignment        : Uint8B
# Struct _IDT64 definitions
class _IDT64(ctypes.Structure):
        _fields_ = [
            ("OffsetLow", WORD),
            ("Selector", WORD),
            ("IstIndex", WORD),
            ("OffsetMiddle", WORD),
            ("OffsetHigh", DWORD),
            ("Reserved1", DWORD)
        ]
PIDT64 = POINTER(_IDT64)
IDT64 = _IDT64


# lkd> dt nt!_KINTERRUPT Type DispatchCode
#   +0x000 Type         : Int2B
#   +0x090 DispatchCode : [4] Uint4B
def get_kinterrupt_64(kdbg, addr_entry):
    # You can get the type ID of any name from  module to which the type belongs
    # IDebugSymbols::GetTypeId
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549376%28v=vs.85%29.aspx
    KINTERRUPT = kdbg.get_type_id("nt", "_KINTERRUPT")
    # You can get the offset of a symbol identified by its name
    # IDebugSymbols::GetOffsetByName
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff548035(v=vs.85).aspx
    dispatch_code_offset = kdbg.get_field_offset("nt", KINTERRUPT, "DispatchCode")
    type_offset = kdbg.get_field_offset("nt", KINTERRUPT, "Type")

    addr_kinterrupt = addr_entry - dispatch_code_offset
    # Read a byte from virtual memory
    # IDebugDataSpaces::ReadVirtual
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554359(v=vs.85).aspx
    type = kdbg.read_byte(addr_kinterrupt + type_offset)
    if type == 0x16:
        return addr_kinterrupt
    else:
        return None


# lkd> dt nt!_KPCR IdtBase
#   +0x038 IdtBase : Ptr64 _KIDTENTRY64
# ...
# lkd> dt nt!_UNEXPECTED_INTERRUPT
#   +0x000 PushImm          : UChar
#   +0x001 Vector           : UChar
#   +0x002 PushRbp          : UChar
#   +0x003 JmpOp            : UChar
#   +0x004 JmpOffset        : Int4B
def get_idt_64(kdbg, num_proc=0):
    l_idt = []
    DEBUG_DATA_KPCR_OFFSET = 0

    KPCR = kdbg.get_type_id("nt", "_KPCR")
    # You can get the number of bytes of memory an instance of the specified type requires
    # IDebugSymbols::GetTypeSize
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff549457(v=vs.85).aspx
    size_unexpected_interrupt = kdbg.get_type_size("nt", "_UNEXPECTED_INTERRUPT")
    idt_base_offset = kdbg.get_field_offset("nt", KPCR, "IdtBase")
    # You can get the location (VA) of a symbol identified by its name
    # IDebugSymbols::GetOffsetByName
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff548035(v=vs.85).aspx
    addr_nt_KxUnexpectedInterrupt0 = kdbg.get_symbol_offset("nt!KxUnexpectedInterrupt0")

    # You can data by their type about the specified processor
    # IDebugDataSpaces::ReadProcessorSystemData
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff554326(v=vs.85).aspx
    kpcr_addr = kdbg.read_processor_system_data(num_proc, DEBUG_DATA_KPCR_OFFSET)

    # You can read a pointer-size value, it doesn't depend of the target computer's architecture processor
    idt_base = kdbg.read_ptr(kpcr_addr + idt_base_offset)
    for i in xrange(0, 0xFF):
        idt64 = IDT64()
        # You can read data from  virtual address into a ctype structure
        kdbg.read_virtual_memory_into(idt_base + i * sizeof(IDT64), idt64)
        addr = (idt64.OffsetHigh << 32) | (idt64.OffsetMiddle << 16) | idt64.OffsetLow
        if addr < addr_nt_KxUnexpectedInterrupt0 or addr > (addr_nt_KxUnexpectedInterrupt0 + 0xFF * size_unexpected_interrupt):
            l_idt.append((addr, get_kinterrupt_64(kdbg, addr)))
        else:
            l_idt.append((None, None))
    return l_idt


# lkd> dt nt!_KPCR PrcbData.VectorToInterruptObject
#   +0x120 PrcbData                         :
#      +0x41a0 VectorToInterruptObject          : [208] Ptr32 _KINTERRUPT
# ...
# lkd> dt nt!_KINTERRUPT Type
#   +0x000 Type : Int2B
def get_kinterrupt_32(kdbg, kpcr_addr, index):
    KPCR = kdbg.get_type_id("nt", "_KPCR")
    KINTERRUPT = kdbg.get_type_id("nt", "_KINTERRUPT")
    pcrbdata_offset = kdbg.get_field_offset("nt", KPCR, "PrcbData.VectorToInterruptObject")
    type_offset = kdbg.get_field_offset("nt", KINTERRUPT, "Type")

    if index < 0x30:
        return None
    addr_kinterrupt = kdbg.read_ptr(kpcr_addr + pcrbdata_offset + (4 * index - 0xC0))
    if addr_kinterrupt == 0:
        return None
    type = kdbg.read_byte(addr_kinterrupt + type_offset)
    if type == 0x16:
        return addr_kinterrupt
    return None


# lkd> dt nt!_KPCR IDT
#   +0x038 IDT : Ptr32 _KIDTENTRY
#   +0x120 PrcbData                         :
#      +0x41a0 VectorToInterruptObject          : [208] Ptr32 _KINTERRUPT
def get_idt_32(kdbg, num_proc=0):
    l_idt = []
    DEBUG_DATA_KPCR_OFFSET = 0

    KPCR = kdbg.get_type_id("nt", "_KPCR")
    idt_base_offset = kdbg.get_field_offset("nt", KPCR, "IDT")
    try:
        pcrbdata_offset = kdbg.get_field_offset("nt", KPCR, "PrcbData.VectorToInterruptObject")
    except WindowsError:
        pcrbdata_offset = 0
    addr_nt_KiStartUnexpectedRange = kdbg.get_symbol_offset("nt!KiStartUnexpectedRange")
    addr_nt_KiEndUnexpectedRange = kdbg.get_symbol_offset("nt!KiEndUnexpectedRange")
    if pcrbdata_offset == 0:
        get_kinterrupt = lambda kdbg, addr, kpcr, i: get_kinterrupt_64(kdbg, addr)
    else:
        get_kinterrupt = lambda kdbg, addr, kpcr, i: get_kinterrupt_32(kdbg, kpcr, i)

    kpcr_addr = kdbg.read_processor_system_data(num_proc, DEBUG_DATA_KPCR_OFFSET)
    idt_base = kdbg.read_ptr(kpcr_addr + idt_base_offset)
    for i in xrange(0, 0xFF):
        idt32 = IDT32()
        kdbg.read_virtual_memory_into(idt_base + i * sizeof(IDT32), idt32)
        if (idt32.ExtendedOffset == 0 or idt32.Offset == 0):
            l_idt.append((None, None))
            continue
        addr = (idt32.ExtendedOffset << 16) | idt32.Offset
        if (addr < addr_nt_KiStartUnexpectedRange or addr > addr_nt_KiEndUnexpectedRange):
            l_idt.append((addr, get_kinterrupt(kdbg, addr, kpcr_addr, i)))
        else:
            addr_kinterrupt = get_kinterrupt(kdbg, addr, kpcr_addr, i)
            if addr_kinterrupt is None:
                addr = None
            l_idt.append((addr, addr_kinterrupt))
    return l_idt


if __name__ == '__main__':
    kdbg = LocalKernelDebugger()
    if windows.current_process.bitness == 32:
        l_idt = get_idt_32(kdbg)
    else:
        l_idt = get_idt_64(kdbg)
    for i in range(len(l_idt)):
        if l_idt[i][0] is not None:
            if l_idt[i][1] is not None:
                print("0x{0:02X} {1} {2} (KINTERRUPT {3})".format(i, hex(l_idt[i][0]), kdbg.get_symbol(l_idt[i][0])[0], hex(l_idt[i][1])))
            else:
                print("0x{0:02X} {1} {2}".format(i, hex(l_idt[i][0]), kdbg.get_symbol(l_idt[i][0])[0]))
