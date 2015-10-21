"""A simple demonstration of LKD to read data from a system bus using any custom
driver. Here we read the BIOS_CNTL (bus = 0x00, device = 0x1F, function = 0x00, 
offset = 0xDC) PCI register which is in charge of protecting the SPI Flash, 
containing the BIOS, on the Platform Controller HUB (PCH)"""
import os
import sys

if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))
    
from dbginterface import LocalKernelDebugger

# Indicates PCI configuration space.
# Value from _BUS_DATA_TYPE
# https://msdn.microsoft.com/en-us/library/windows/hardware/ff540700(v=vs.85).aspx
PCIConfiguration = 4
# LPC device PCI configuration space
bus_num = 0
device_num = 0x1F
function_num = 0
# BIOS_CNTL register
offset_bios_cntl = 0xDC

SMM_BWP_mask = 1 << 5   # 0x20
BLE_mask = 1 << 1       # 0x2
BIOSWE_mask = 1 << 0    # 0x1

if __name__ == '__main__':
    kdbg = LocalKernelDebugger()
    # You can read data from a system bus by specifying the bus data type, bus number,
    # slot number, offset and size of data to read
    # IDebugDataSpaces::ReadBusData
    # https://msdn.microsoft.com/en-us/library/windows/hardware/ff553519(v=vs.85).aspx
    bios_cntl = ord(kdbg.read_bus_data(PCIConfiguration,
        bus_num, device_num + (function_num << 5),
        offset_bios_cntl, 1))
    if bios_cntl & SMM_BWP_mask:
        print("[+] Speed Racer: Not Vulnerable")
    else:
        print("[-] Speed Racer: Vulnerable")
    if bios_cntl & BIOSWE_mask:
        print("[-] BIOS Rewriting: Enable")
    else:
        print("[+] BIOS Rewriting: Disable")
    if bios_cntl & BLE_mask:
        print("[+] BIOS Rewriting Lock: Not Vulnerable")
    else:
        print("[-] BIOS Rewriting Lock: Vulnerable")