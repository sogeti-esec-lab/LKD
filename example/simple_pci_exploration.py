import sys
import struct
import os

if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))
    
import dbginterface
import pci_vendor


class PciExplorer(object):
    PCIConfiguration = 4

    def __init__(self, quiet=True):
        self.kdbg = dbginterface.LocalKernelDebugger(quiet)

    def read_pci(self, busnumber, device, function, offset, size):
        return self.kdbg.read_bus_data(self.PCIConfiguration, busnumber, device + (function << 5), offset, size)

    def read_pci_word(self, busnumber, device, function, offset):
        raw = self.read_pci(busnumber, device, function, offset, 2)
        return struct.unpack("<H", raw)[0]

pci = PciExplorer()
bus = 0
f = 0
for device in range(32):
    vendor_id = pci.read_pci_word(bus, device, f, 0)
    device_id = pci.read_pci_word(bus, device, f, 2)
    if vendor_id == 0xffff:
        continue
    if vendor_id in pci_vendor.pci_vendor:
        print("0x{0:04X} Vendor {1:30} | DeviceId 0x{2:04X}".format(device, pci_vendor.pci_vendor[vendor_id], device_id))
    else:
        print("0x{0:04X} Vendor {1:30} | DeviceId 0x{2:04X}".format(device, hex(vendor_id), device_id))
