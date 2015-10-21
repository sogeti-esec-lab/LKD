import sys
sys.path.append(".")
import unittest
import os
import struct

import windows.utils
import windows.pe_parse
import windows.native_exec.cpuid as cpuid

from windows import winproxy
import ctypes
from ctypes import byref, create_string_buffer, WINFUNCTYPE, HRESULT, WinError, sizeof
import dbginterface
from dbginterface import LocalKernelDebugger
from windows.generated_def.winstructs import *

# Bitness attribute to skip test

is_32_bits = windows.current_process.bitness == 32
is_64_bits = windows.current_process.bitness == 64

test_32bit_only = unittest.skipIf(not is_32_bits, "Test for 32bits Kernel only")
test_64bit_only = unittest.skipIf(not is_64_bits, "Test for 64bits Kernel only")

def get_kl

class RequireSymbol(object):
    def __init__(self, *args):
        self.required_symbols = args
        
    def __call__(self, f):
        self.f = f
        # non-class associated function to get the wrapped 'self' (type TestCase) and call
        # a RequireSymbol method to also have our self (type RequireSymbol)
        def mywrapper(testcase):
            return self.do_call(testcase)
        return mywrapper
        
    def do_call(self, testcase):
        for sym in self.required_symbols:
            if testcase.kdbg.get_symbol_offset(sym) is None:
                raise testcase.skipTest("Cannot get symbol <{0}>".format(sym))
        return self.f(testcase)
        
    

class IDebugSymbolsTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    @classmethod
    def setUpClass(self):
        windows.winproxy.SetThreadAffinityMask(dwThreadAffinityMask=(1 << 0))
        self.kdbg = LocalKernelDebugger()
        modules = windows.utils.get_kernel_modules()
        self.modules = modules
        self.ntkernelbase = modules[0].Base
        self.kernelpath = modules[0].ImageName[:]
        self.kernelpath = os.path.expandvars(self.kernelpath.replace("\SystemRoot", "%SystemRoot%"))
        self.kernelmod = winproxy.LoadLibraryA(self.kernelpath)
        pe = windows.pe_parse.PEFile(self.kernelmod)
        self.NtCreateFileVA = pe.exports['NtCreateFile'] - self.kernelmod + self.ntkernelbase

    def tearDown(self):
        #self.kdbg.detach()
        self.kdbg = None

    def test_get_symbol_offset(self):
        # IDebugSymbols::GetOffsetByName
        x = self.kdbg.get_symbol_offset("nt")
        self.assertEqual(x, self.ntkernelbase)

    @RequireSymbol("ntdll!NtCreateFile")
    def test_get_symbol_offset_user(self):
        # IDebugSymbols::GetOffsetByName
        x = windows.utils.get_func_addr("ntdll", "NtCreateFile")
        y = self.kdbg.get_symbol_offset("ntdll!NtCreateFile")
        self.assertEqual(x, y)
        
    @RequireSymbol("nt!NtCreateFile")
    def test_get_symbol(self):
        # IDebugSymbols::GetNameByOffset
        x = self.kdbg.get_symbol(self.NtCreateFileVA)
        self.assertEqual(x[0], 'nt!NtCreateFile')
        self.assertEqual(x[1], 0x00)
        
    @RequireSymbol("ntdll!NtCreateFile")
    def test_get_symbol_user(self):
        # IDebugSymbols::GetNameByOffset
        x = windows.utils.get_func_addr("ntdll", "NtCreateFile")
        y = self.kdbg.get_symbol(x)
        self.assertIn(y[0], ["ntdll!NtCreateFile", "ntdll!ZwCreateFile"])

    def test_get_number_modules(self):
        # IDebugSymbols::GetNumberModules
        loaded, unloaded = self.kdbg.get_number_modules()

    def test_get_module_by_index(self):
        # IDebugSymbols::GetModuleByIndex
        for i in range(self.kdbg.get_number_modules()[0]):
            x = self.kdbg.get_module_by_index(i)
            if x == self.ntkernelbase:
                return
        raise AssertionError("ntoskrnl not found")

    def test_get_module_name_by_index(self):
        # IDebugSymbols::GetModuleNames
        for i in range(self.kdbg.get_number_modules()[0]):
            x = self.kdbg.get_module_name_by_index(i)
            if x[1] == "nt":
                return
        raise AssertionError("ntoskrnl not found")

    def test_symbol_match(self):
        # IDebugSymbols::StartSymbolMatch | IDebugSymbols::GetNextSymbolMatch | IDebugSymbols::EndSymbolMatch
        x = list(self.kdbg.symbol_match("nt!NtCreateF*"))
        self.assertEqual(x[0][0], 'nt!NtCreateFile')
        self.assertEqual(x[0][1], self.NtCreateFileVA)

class IDebugDataSpacesTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    @classmethod
    def setUpClass(self):
        windows.winproxy.SetThreadAffinityMask(dwThreadAffinityMask=(1 << 0))
        self.kdbg = LocalKernelDebugger()
        modules = windows.utils.get_kernel_modules()
        self.ntkernelbase = modules[0].Base
        self.kernelpath = modules[0].ImageName[:]
        self.kernelpath = os.path.expandvars(self.kernelpath.replace("\SystemRoot", "%SystemRoot%"))
        self.kernelbuf = open(self.kernelpath, "rb").read()
        self.kernelmod = winproxy.LoadLibraryA(self.kernelpath)
        pe = windows.pe_parse.PEFile(self.kernelmod)
        self.kernel_section_data = [section for section in pe.sections if section.name == ".data"][0]

    def tearDown(self):
        #self.kdbg.detach()
        self.kdbg = None

    def test_read_byte(self):
        # IDebugDataSpaces::ReadVirtual
        x = self.kdbg.read_byte(self.kdbg.get_symbol_offset("nt"))
        self.assertEqual(x, ord(self.kernelbuf[0]))

    def test_read_word(self):
        # IDebugDataSpaces::ReadVirtual
        x = self.kdbg.read_word(self.kdbg.get_symbol_offset("nt"))
        self.assertEqual(x, struct.unpack("<H", self.kernelbuf[:2])[0])

    def test_read_dword(self):
        # IDebugDataSpaces::ReadVirtual
        x = self.kdbg.read_dword(self.kdbg.get_symbol_offset("nt"))
        self.assertEqual(x, struct.unpack("<I", self.kernelbuf[:4])[0])

    def test_read_qword(self):
        # IDebugDataSpaces::ReadVirtual
        x = self.kdbg.read_qword(self.kdbg.get_symbol_offset("nt"))
        self.assertEqual(x, struct.unpack("<Q", self.kernelbuf[:8])[0])

    def test_read_byte_p(self):
        # IDebugDataSpaces::ReadPhysical
        x = self.kdbg.read_byte(self.kdbg.get_symbol_offset("nt"))
        y = self.kdbg.read_byte_p(self.kdbg.virtual_to_physical(self.kdbg.get_symbol_offset("nt")))
        self.assertEqual(x, y)

    def test_read_word_p(self):
        # IDebugDataSpaces::ReadPhysical
        x = self.kdbg.read_word(self.kdbg.get_symbol_offset("nt"))
        y = self.kdbg.read_word_p(self.kdbg.virtual_to_physical(self.kdbg.get_symbol_offset("nt")))
        self.assertEqual(x, y)

    def test_read_dword_p(self):
        # IDebugDataSpaces::ReadPhysical
        x = self.kdbg.read_dword(self.kdbg.get_symbol_offset("nt"))
        y = self.kdbg.read_dword_p(self.kdbg.virtual_to_physical(self.kdbg.get_symbol_offset("nt")))
        self.assertEqual(x, y)

    def test_read_qword_p(self):
        # IDebugDataSpaces::ReadPhysical
        x = self.kdbg.read_qword(self.kdbg.get_symbol_offset("nt"))
        y = self.kdbg.read_qword_p(self.kdbg.virtual_to_physical(self.kdbg.get_symbol_offset("nt")))
        self.assertEqual(x, y)


    @test_32bit_only
    @RequireSymbol('nt!KiFastCallEntry')
    def test_read_msr32(self):
        # IDebugDataSpaces::ReadMsr
        IA32_SYSENTER_EIP = 0x176
        x = self.kdbg.read_msr(IA32_SYSENTER_EIP)
        y = self.kdbg.get_symbol(x)
        self.assertEqual(y[0], 'nt!KiFastCallEntry')

    @test_64bit_only
    @RequireSymbol('nt!KiSystemCall64')
    def test_read_msr64(self):
        # IDebugDataSpaces::ReadMsr
        LSTAR = 0xC0000082
        x = self.kdbg.read_msr(LSTAR)
        y = self.kdbg.get_symbol(x)
        self.assertEqual(y[0], 'nt!KiSystemCall64')

    @test_32bit_only
    def test_read_processor_system_data32(self):
        # IDebugDataSpaces::ReadProcessorSystemData
        DEBUG_DATA_PROCESSOR_IDENTIFICATION = 4
        x = self.kdbg.read_processor_system_data(0, DEBUG_DATA_PROCESSOR_IDENTIFICATION)
        self.assertEqual(cpuid.get_vendor_id(), x.X86.VendorString)
        self.assertEqual(cpuid.get_proc_family_model(), (x.X86.Family, x.X86.Model))

    @test_64bit_only
    def test_read_processor_system_data64(self):
        # IDebugDataSpaces::ReadProcessorSystemData
        DEBUG_DATA_PROCESSOR_IDENTIFICATION = 4
        x = self.kdbg.read_processor_system_data(0, DEBUG_DATA_PROCESSOR_IDENTIFICATION)
        self.assertEqual(cpuid.get_vendor_id(), x.Amd64.VendorString)
        self.assertEqual(cpuid.get_proc_family_model(), (x.Amd64.Family, x.Amd64.Model))

    def test_write_byte(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 1
        self.kdbg.write_byte(addr, 0x42)
        x = self.kdbg.read_byte(addr)
        self.assertEqual(0x42, x)

    def test_write_byte_p(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 1
        self.kdbg.write_byte_p(self.kdbg.virtual_to_physical(addr), 0x43)
        x = self.kdbg.read_byte(addr)
        self.assertEqual(0x43, x)

    def test_write_word(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 2
        self.kdbg.write_word(addr, 0x4444)
        x = self.kdbg.read_word(addr)
        self.assertEqual(0x4444, x)

    def test_write_word_p(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 2
        self.kdbg.write_word_p(self.kdbg.virtual_to_physical(addr), 0x4545)
        x = self.kdbg.read_word(addr)
        self.assertEqual(0x4545, x)

    def test_write_dword(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 4
        self.kdbg.write_dword(addr, 0x46464646)
        x = self.kdbg.read_dword(addr)
        self.assertEqual(0x46464646, x)

    def test_write_dword_p(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 4
        self.kdbg.write_dword_p(self.kdbg.virtual_to_physical(addr), 0x47474747)
        x = self.kdbg.read_dword(addr)
        self.assertEqual(0x47474747, x)

    def test_write_qword(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 8
        self.kdbg.write_qword(addr, 0x4848484848484848)
        x = self.kdbg.read_qword(addr)
        self.assertEqual(0x4848484848484848, x)

    def test_write_qword_p(self):
        kernel_base = self.kdbg.get_symbol_offset("nt")
        addr = kernel_base + self.kernel_section_data.VirtualAddress + self.kernel_section_data.VirtualSize - 8
        self.kdbg.write_qword_p(self.kdbg.virtual_to_physical(addr), 0x4949494949494949)
        x = self.kdbg.read_qword(addr)
        self.assertEqual(0x4949494949494949, x)
        
        
        
# Testing read_bus_data and read_io and write_io by exploring the PCI bus   
class PciExplorer(object):
    CONFIG_ADDRESS = 0xCF8
    CONFIG_DATA    = 0xCFC
    PCIConfiguration = 4

    def __init__(self, quiet=True):
        self.kdbg = dbginterface.LocalKernelDebugger(quiet)
    
    def read_pci(self, busnumber, device, function, offset, size):
        return self.kdbg.read_bus_data(self.PCIConfiguration, busnumber, device + (function << 5), offset, size)
    
    def read_pci_word(self, busnumber, device, function, offset):
        raw = self.read_pci(busnumber, device, function, offset, 2)
        return struct.unpack("<H", raw)[0]
        
    def manual_read_pci_word(self, busnumber, device, function, offset):
        value = 1 << 31
        value |= busnumber << 16
        value |= device << 11
        value |= function << 8
        value |= (offset & 0xfc) << 2
        self.kdbg.write_io(self.CONFIG_ADDRESS, value, 4)
        return ((self.kdbg.read_io(self.CONFIG_DATA, 4) >> ((offset & 2) * 8)) & 0xffff)
    
   
class PCITestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    @classmethod
    def setUpClass(self):
        self.pciexplorer = PciExplorer()
        
    def test_iter_pci_device(self):
        bus = 0x00
        f = 0
        for device in range(32):
            pci_vendor = self.pciexplorer.read_pci_word(bus, device, f, 0)
            pci_device = self.pciexplorer.read_pci_word(bus, device, f, 2)
            
            manual_pci_vendor = self.pciexplorer.manual_read_pci_word(bus, device, f, 0)
            manual_pci_device = self.pciexplorer.manual_read_pci_word(bus, device, f, 2)
            self.assertEqual(pci_vendor, manual_pci_vendor)
            self.assertEqual(pci_device, manual_pci_device)
        
    def tearDown(self):
        pass
        
class DriverUpgradeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.kdbg = LocalKernelDebugger()
        
    def test_alloc_memory(self):
        addr = self.kdbg.alloc_memory(0x1000)
        self.kdbg.write_byte(addr, 0x42)
        self.assertEqual(self.kdbg.read_byte(addr), 0x42)

        self.kdbg.write_byte(addr + 0xfff, 0x42)
        self.assertEqual(self.kdbg.read_byte(addr + 0xfff), 0x42)

    def test_full_driver_upgrade(self):
        upgrader = self.kdbg.upgrader
        upgrader.registered_ioctl = []
        upgrader.full_driver_upgrade()
        self.test_alloc_memory()
        
    def test_retrieve_driver_upgrade(self):
        # Get current registered IO
        registered_io = self.kdbg.upgrader.registered_ioctl
        # Verif that some IO are registered
        self.assertTrue(registered_io)
        new_upgrader = type(self.kdbg.upgrader)(self.kdbg)
        # Verif that new upgrader see that driver is upgraded
        self.assertTrue(new_upgrader.is_driver_already_upgraded())
        # Verif IOCTL retrieving
        new_upgrader.retrieve_upgraded_info()
        self.assertItemsEqual(registered_io, new_upgrader.registered_ioctl)
        
    def test_map_page_to_userland(self):
        kpage = self.kdbg.alloc_memory(0x1000)
        userpage = self.kdbg.map_page_to_userland(kpage, 0x1000)
        
        self.kdbg.write_dword(kpage, 0x11223344)
        self.assertEqual(ctypes.c_uint.from_address(userpage).value, 0x11223344)
        
        ctypes.c_uint.from_address(userpage + 4).value = 0x12345678
        self.assertEqual(self.kdbg.read_dword(kpage + 4), 0x12345678)

if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(unittest.makeSuite(IDebugSymbolsTestCase))
    alltests.addTest(unittest.makeSuite(IDebugDataSpacesTestCase))
    alltests.addTest(unittest.makeSuite(PCITestCase))
    alltests.addTest(unittest.makeSuite(DriverUpgradeTestCase))
    unittest.TextTestRunner(verbosity=2).run(alltests)