"""A simple demonstration of LKD to activate PEBS and BTS feature from intel CPU"""
import ctypes
import sys
import os

if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))

from windows.generated_def.winstructs import *
from dbginterface import LocalKernelDebugger


# What is BTS?:
# Branch Trace Store (BTS) is an intel's CPU feature that allows to
# store all the branches (src and dst) taken on a CPU to a buffer
#
# To activate the BTS you need to:
#   setup the Debug Store (DS) Area
#   setup the BTS related fields in DS
#   activate BTS
# see in man intel:
#   http://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-manual-325462.pdf
#   Volume 3B: System Programming Guide 17.4.5 (Branch Trace Store (BTS))
#   Volume 3B: System Programming Guide 17.4.9 (BTS and DS area)

# !! BTS buffer can be configured to be circular or not (see 17.4.9.3 (Setting Up the BTS Buffer))

# What is PEBS?:
# Precise Event Based Sampling (PEBS) is an intel's CPU feature that allows to
# store the CPU states (general purpose registers) at a given event.
# This feature rely on the performance counter
# To activate the PEBS you need to:
#   Setup the Debug Store (DS) Area
#   Setup the PEBS related fields in DS
#   Setup the performance counter that will trigger the PEBS (PERFEVTSE0) here
#   Activate PEBS
#   Activate the counter
# see in man intel: (lot of micro-architecture stuff here)
#   http://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-manual-325462.pdf
#   Volume 3B: System Programming Guide 18.4 (PERFORMANCE MONITORING (PROCESSORS BASED ON INTELCORE MICROARCHITECTURE)
#   Volume 3B: System Programming Guide 18.4.4 (Precise Event Based Sampling (PEBS))

#   Volume 3B: System Programming Guide 18.7 (PERFORMANCE MONITORING FOR PROCESSORS BASED ON INTEL MICROARCHITECTURE CODE NAME NEHALEM)
#   Volume 3B: System Programming Guide 18.7.1.1 (Precise Event Based Sampling (PEBS))

# TLDR:
# PEBS will trigger a dump of the PEBSRecord (general purpose registers + some other info) when
# the associated performance counter overflow (PERFEVTSE0 in this code) then 
# the performance counter value is reset to DsManagementAreaStruct.PEBSCounterResetValue
# So if you want to dump the state of the proc often you should set this to a high value
# !! THE PEBS BUFFER IS NOT circular
# you need the reset it manually when the good interrupt is raise (see 18.4.4.3 (Writing a PEBS Interrupt Service Routine))
# This require to inject some code in kerneland (not done in this example)




DEBUG_STORE_MSR_VALUE = 0x600
IA32_DEBUGCTL_MSR_VALUE = 0x1D9
IA32_MISC_ENABLE = 0x1A0
MSR_PEBS_ENABLED = 0x3F1
MSR_PERF_GLOBAL_CTRL = 0x38f
PERF_CAPABILITIES = 0x345

IA32_PMC0 = 0xC1
PERFEVTSE0 = 0x186
PERFEVTSE1 = 0x186 + 1
PERFEVTSE2 = 0x186 + 2
PERFEVTSE3 = 0x186 + 3

PEBS_RECORD_COUNTER_VALUE = 0xffffffffff920000

# Mask for IA32_MISC_ENABLE
# YES this is really BTS_UNAVILABLE in the intel man :D
BTS_UNAVILABLE = 1 << 11
PEBS_UNAVILABLE = 1 << 12
UMON_AVAILABLE = 1 << 7


class DsManagementAreaStruct(ctypes.Structure):
    """The DS management area for 64bits processors"""
    _fields_ = [("BtsBufferBase", ULONG64),
                ("BtsIndex", ULONG64),
                ("BtsAbsoluteMaximum", ULONG64),
                ("BTSThresholdinterupt", ULONG64),
                ("PEBSBufferBase", ULONG64),
                ("PEBSIndex", ULONG64),
                ("PEBSAbsoluteMaximum", ULONG64),
                ("PEBSThresholdinterupt", ULONG64),
                ("PEBSCounterResetValue", ULONG64),  # should be 40bits field
                ("PEBSCounterResetValue2", ULONG64),  # hack to set it to 0
                ("Stuff1", ULONG64),
                ("Stuff2", ULONG64),
                ]


class BtsRecord(ctypes.Structure):
    _fields_ = [("BranchFrom", ULONG64),
                ("BranchTo", ULONG64),
                ("Stuff", ULONG64)
                ]


# 18-58 in http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-3b-part-2-manual.html
# Thanks to https://github.com/andikleen/pmu-tools/blob/master/pebs-grabber/pebs-grabber.c
class PEBSRecordV0(ctypes.Structure):
    _fields_ = [("rflags", ULONG64),
                ("rip", ULONG64),
                ("rax", ULONG64),
                ("rbx", ULONG64),
                ("rcx", ULONG64),
                ("rdx", ULONG64),
                ("rsi", ULONG64),
                ("rdi", ULONG64),
                ("rbp", ULONG64),
                ("rsp", ULONG64),
                ("r8", ULONG64),
                ("r9", ULONG64),
                ("r10", ULONG64),
                ("r11", ULONG64),
                ("r12", ULONG64),
                ("r13", ULONG64),
                ("r14", ULONG64),
                ("r15", ULONG64)
                ]


class PEBSRecordV1(PEBSRecordV0):
    _fields_ = [("IA32_PERF_FLOBAL_STATUS", ULONG64),
                ("DataLinearAddress", ULONG64),
                ("DaaSourceEncoding", ULONG64),
                ("LatencyValue", ULONG64),
                ]


class PEBSRecordV2(PEBSRecordV1):
    _fields_ = [("EventingIP", ULONG64),
                ("TXAbortInformation", ULONG64),
                ]


def check_feature(kdbg):
    """Check that BTS and PEBS features are available"""
    misc_enabled = kdbg.read_msr(IA32_MISC_ENABLE)
    if misc_enabled & BTS_UNAVILABLE:
        print("NO BTS")
    if misc_enabled & PEBS_UNAVILABLE:
        print("NO PEBS")
    if not misc_enabled & UMON_AVAILABLE:
        print("UMON NOT AVAILABLE")

# =================================    BTS
class BTSManager(object):
    def __init__(self, kdbg):
        self.kdbg = kdbg

    def setup_DsManagementArea(self, proc_nb):
        """Setup the setup_DsManagementArea for the proc `proc_nb`
           proc_nb must be the number of the current processor
           
           The write to nt!VfBTSDataManagementArea is where ntokrnl store this information"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        if ds_addr:
            return
        ds_management_area_addr = self.kdbg.alloc_memory(0x1000)
        kdbg.write_virtual_memory(ds_management_area_addr, "\x00" * 0x1000)
        VfBTSDataManagementArea = kdbg.get_symbol_offset("nt!VfBTSDataManagementArea")
        kdbg.write_ptr(VfBTSDataManagementArea + proc_nb * ctypes.sizeof(PVOID), ds_management_area_addr)
        kdbg.write_msr(DEBUG_STORE_MSR_VALUE, ds_management_area_addr)

    def get_DsManagementArea(self, proc_nb):
        """Return the DsManagementAreaStruct and address for the `proc_nb` processor"""
        VfBTSDataManagementArea = kdbg.get_symbol_offset("nt!VfBTSDataManagementArea")
        DataManagementAreaProcX = kdbg.read_ptr(VfBTSDataManagementArea + proc_nb * ctypes.sizeof(PVOID))
        if DataManagementAreaProcX == 0:
            return 0, None
        DsManagementAreaContent = DsManagementAreaStruct()
        self.kdbg.read_virtual_memory_into(DataManagementAreaProcX, DsManagementAreaContent)
        return (DataManagementAreaProcX, DsManagementAreaContent)

    def setup_BTS(self, proc_nb, buffer_size=0x1000):
        """Setup the DsManagementArea BTS fields for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        buffer_addr = kdbg.alloc_memory(buffer_size)
        ds_content.BtsBufferBase = buffer_addr
        ds_content.BtsIndex = buffer_addr
        ds_content.BtsAbsoluteMaximum = buffer_addr + buffer_size + 1
        ds_content.BtsThresholdinterupt = 0  # or buffer_addr + buffer_size + 1 to trigger it
        self.kdbg.write_virtual_memory(ds_addr, ds_content)

    def stop_BTS(self):
        """Stop BTS on current processor"""
        kdbg.write_msr(IA32_DEBUGCTL_MSR_VALUE, 0x0)

    def start_BTS(self, enable, off_user=0, off_os=0):
        """Start the BTS (see 17.4.1 IA32_DEBUGCTL MSR) as circular buffer"""
        value = enable << 6 | enable << 7 | off_user << 10 | off_os << 9
        kdbg.write_msr(IA32_DEBUGCTL_MSR_VALUE, value)

    def get_number_bts_records(self, proc_nb):
        """Get the number of BTS entries stored in the buffer for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        return (ds_content.BtsIndex - ds_content.BtsBufferBase) / ctypes.sizeof(BtsRecord)

    def get_bts_records(self, proc_nb, max_dump=0xffffffffffffffff):
        """Get the BTS entries stored in the buffer for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        nb_bts_entry = self.get_number_bts_records(proc_nb)
        print("Buffer contains {0} entries".format(nb_bts_entry))
        nb_bts_entry = min(nb_bts_entry, max_dump)
        print("Dumping {0} first entries".format(nb_bts_entry))
        bts_entries_buffer = (BtsRecord * nb_bts_entry)()
        kdbg.read_virtual_memory_into(ds_content.BtsBufferBase, bts_entries_buffer)
        return bts_entries_buffer

    def dump_bts(self):
        ds_addr, ds_content = self.get_DsManagementArea(0)
        print("BtsBufferBase = {0}".format(hex(ds_content.BtsBufferBase)))
        records = self.get_bts_records(0, max_dump=20)
        for rec in records:
            from_sym, from_disp = kdbg.get_symbol(rec.BranchFrom)
            from_disp = hex(from_disp) if from_disp is not None else None
            from_str = "Jump {0} ({1} + {2})".format(hex(rec.BranchFrom), from_sym, from_disp)
                
            to_sym, to_disp = kdbg.get_symbol(rec.BranchTo)
            to_disp = hex(to_disp) if to_disp is not None else None
            to_str = "Jump {0} ({1} + {2})".format(hex(rec.BranchTo), to_sym, to_disp)
            
            print("{0} -> {1}".format(from_str, to_str))


# =================================    PEBS
class PEBSManager(object):
    def __init__(self, kdbg):
        self.kdbg = kdbg
        pebs_record_v = self.get_pebs_records_version()
        if pebs_record_v == 0:
            self.PEBSRecord = PEBSRecordV0
        elif pebs_record_v == 1:
            self.PEBSRecord = PEBSRecordV1
        elif pebs_record_v == 2:
            self.PEBSRecord = PEBSRecordV2
        else:
            raise ValueError("Don't know the format of PEBS Records of version {0}".format(pebs_record_v))

    def setup_perfevtsel0(self, enable, mask=0, eventselect=0xc0, user_mod=1, os_mod=1):
        """Setup the PERFEVTSE0 MSR to manage the IA32_PMC0 perf counter
        Default eventselect 0xc0 is 'Instruction retired'"""
        # Instruction retired
        MASK = mask << 8
        EVENTSELECT = eventselect << 0
        USER_MOD = user_mod << 16
        OS_MOD = os_mod << 17
        ENABLE = enable << 22
        value = MASK | EVENTSELECT | USER_MOD | OS_MOD | ENABLE
        self.kdbg.write_msr(PERFEVTSE0, value)

    def get_pebs_records_version(self):
        return (self.kdbg.read_msr(PERF_CAPABILITIES) >> 8) & 0xf

    def setup_DsManagementArea(self, proc_nb):
        """Setup the setup_DsManagementArea for the proc `proc_nb`
           proc_nb must be the number of the current processor
           
           The write to nt!VfBTSDataManagementArea is where ntokrnl store this information"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        if ds_addr:
            return
        ds_management_area_addr = self.kdbg.alloc_memory(0x1000)
        self.kdbg.write_virtual_memory(ds_management_area_addr, "\x00" * 0x1000)
        VfBTSDataManagementArea = kdbg.get_symbol_offset("nt!VfBTSDataManagementArea")
        kdbg.write_ptr(VfBTSDataManagementArea + proc_nb * ctypes.sizeof(PVOID), ds_management_area_addr)
        kdbg.write_msr(DEBUG_STORE_MSR_VALUE, ds_management_area_addr)

    def get_DsManagementArea(self, proc_nb):
        """Return the DsManagementAreaStruct and address for the `proc_nb` processor"""
        VfBTSDataManagementArea = kdbg.get_symbol_offset("nt!VfBTSDataManagementArea")
        DataManagementAreaProcX = kdbg.read_ptr(VfBTSDataManagementArea + proc_nb * ctypes.sizeof(PVOID))
        if DataManagementAreaProcX == 0:
            return 0, None
        DsManagementAreaContent = DsManagementAreaStruct()
        self.kdbg.read_virtual_memory_into(DataManagementAreaProcX, DsManagementAreaContent)
        return (DataManagementAreaProcX, DsManagementAreaContent)

    def setup_pebs(self, proc_nb, buffer_size=0x1000):
        """Setup de DsManagementArea PEBS fields for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        buffer_addr = kdbg.alloc_memory(buffer_size)
        ds_content.PEBSBufferBase = buffer_addr
        ds_content.PEBSIndex = buffer_addr
        ds_content.PEBSAbsoluteMaximum = buffer_addr + buffer_size + 1
        ds_content.PEBSThresholdinterupt = 0  # or buffer_addr + buffer_size + 1 to trigger it
        ds_content.PEBSThresholdinterupt = 0
        ds_content.PEBSCounterResetValue = PEBS_RECORD_COUNTER_VALUE
        ds_content.PEBSCounterResetValue2 = 0xffffffffffffffff
        self.kdbg.write_virtual_memory(ds_addr, ds_content)

    def stop_PEBS(self):
        # Does the second line is enough ?
        self.kdbg.write_msr(PERFEVTSE0, 0)
        self.kdbg.write_msr(MSR_PERF_GLOBAL_CTRL, 0)
        self.kdbg.write_msr(MSR_PEBS_ENABLED, 0)

    def start_PEBS(self):
        """Start the PEBS by:
            Setup the event counter associated with PEBS (perfevtsel0)
            Enable PEBS
            Enable the counter perfevtsel0
        """
        # Stop counter IA32_PMC0 (needed to write it)
        self.stop_PEBS()
        # 0xc0 -> Instruction retired
        self.setup_perfevtsel0(enable=1, mask=0, eventselect=0xc0, user_mod=1, os_mod=1)
        # TODO: change counter value (sign extended)
        kdbg.write_msr(IA32_PMC0, 0xfffa0000)
        # Activate PEBS
        kdbg.write_msr(MSR_PEBS_ENABLED, 1)
        # Re-activate IA32_PMC0
        kdbg.write_msr(MSR_PERF_GLOBAL_CTRL, 1)

    # PEBS records getters
    def get_number_pebs_records(self, proc_nb):
        """Get the number of PEBS entries stored in the buffer for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        return (ds_content.PEBSIndex - ds_content.PEBSBufferBase) / ctypes.sizeof(self.PEBSRecord)

    def get_pebs_records(self, proc_nb, max_dump=0xffffffffffffffff):
        """Get the PEBS entries stored in the buffer for proc `proc_nb`"""
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        nb_pebs_entry = self.get_number_pebs_records(proc_nb)
        print("Buffer contains {0} entries".format(nb_pebs_entry))
        nb_pebs_entry = min(nb_pebs_entry, max_dump)
        print("Dumping {0} first entries".format(nb_pebs_entry))
        pebs_entries_buffer = (self.PEBSRecord * nb_pebs_entry)()
        kdbg.read_virtual_memory_into(ds_content.PEBSBufferBase, pebs_entries_buffer)
        return pebs_entries_buffer

    def dump_PEBS_records(self):
        ds_addr, ds_content = self.get_DsManagementArea(proc_nb)
        print("PEBSBufferBase = {0}".format(hex(ds_content.PEBSBufferBase)))
        x = self.get_pebs_records(0)
        for pebs_record in x:
            print("    {0} = {1}".format("rip", hex(pebs_record.rip)))            
            
            

# BTS
kdbg = LocalKernelDebugger()
check_feature(kdbg)
kdbg.reload()
kdbg.set_current_processor(0)
btsm = BTSManager(kdbg)
btsm.setup_DsManagementArea(0)
btsm.setup_BTS(0, buffer_size=0x100000)
btsm.start_BTS(enable=1)
import time
time.sleep(1)
btsm.stop_BTS()
btsm.dump_bts()


# # PEBS
# kdbg = LocalKernelDebugger()
# check_feature(kdbg)
# kdbg.set_current_processor(0)
# pebsm = PEBSManager(kdbg)
# pebsm.setup_DsManagementArea(0)
# pebsm.setup_pebs(0, buffer_size=0x1000)
# pebsm.start_PEBS()
# pebsm.dump_PEBS_records()
# import time
# time.sleep(1)
# pebsm.dump_PEBS_records()
# pebsm.stop_PEBS()
