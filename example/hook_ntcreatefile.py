"""A demonstration of LKD that display all files opened by hooking nt!NtCreateFile"""
import sys
import time
import ctypes
import os

if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))

import windows
import windows.native_exec.simple_x86 as x86
import windows.native_exec.simple_x64 as x64

from dbginterface import LocalKernelDebugger

kdbg = LocalKernelDebugger()

if windows.system.bitness != 32:
    raise ValueError("Test for kernel32 only")

def hook_ntcreatefile(kdbg, ignore_jump_space_check=False):
    """Hook NtCreateFile, the hook write the filename to a shared memory page"""
    nt_create_file = kdbg.get_symbol_offset("nt!NtCreateFile")
    if not ignore_jump_space_check:
        # Check that function begin with mov edi, edi for the hook short jump
        if kdbg.read_word(nt_create_file) != 0xff8b:  # mov edi, edi
            print(hex(kdbg.read_word(nt_create_file)))
            raise ValueError("Cannot hook fonction that doest not begin with <mov edi,edi> (/f to force if hook already in place)")
        # Check there is 5 bytes free before for the hook long jump
        if kdbg.read_virtual_memory(nt_create_file - 5, 5) not in ["\x90" * 5, "\xCC" * 5]:  #NOP * 5 ; INT 3 * 5
            print(kdbg.read_virtual_memory(nt_create_file - 5, 5))
            raise ValueError("Cannot hook fonction that is not prefixed with 5 nop/int 3")

    # Allocate memory for the shared buffer kernel<->user
    # the format is:
    # [addr] -> size of size already taken
    # then:
    #   DWORD string_size
    #   char[string_size] filename
    data_kernel_addr = kdbg.alloc_memory(0x1000)
    kdbg.write_pfv_memory(data_kernel_addr, "\x00" * 0x1000)
    # Map the shared buffer to userland
    data_user_addr = kdbg.map_page_to_userland(data_kernel_addr, 0x1000)
    # Allocate memory for the hook
    shellcode_addr = kdbg.alloc_memory(0x1000)
    # shellcode
    shellcode = x86.MultipleInstr()
    # Save register
    shellcode += x86.Push('EAX')
    shellcode += x86.Push('ECX')
    shellcode += x86.Push('EDI')
    shellcode += x86.Push('ESI')
    # Check that there is space remaining, else don't write it
    shellcode += x86.Cmp(x86.deref(data_kernel_addr), 0x900)
    shellcode += x86.Jnb(":END")
    # Get 3rd arg (POBJECT_ATTRIBUTES ObjectAttributes)
    shellcode += x86.Mov('EAX', x86.mem('[ESP + 0x1c]')) # 0xc + 0x10 for push
    # Get POBJECT_ATTRIBUTES.ObjectName (PUNICODE_STRING)
    shellcode += x86.Mov('EAX', x86.mem('[EAX + 0x8]'))
    shellcode += x86.Xor('ECX', 'ECX')
    # Get PUNICODE_STRING.Length
    shellcode += x86.Mov('CX', x86.mem('[EAX + 0]'))
    # Get PUNICODE_STRING.Buffer
    shellcode += x86.Mov('ESI', x86.mem('[EAX + 4]'))
    # Get the next free bytes in shared buffer
    shellcode += x86.Mov('EDI', data_kernel_addr + 4)
    shellcode += x86.Add('EDI', x86.deref(data_kernel_addr))
    # Write (DWORD string_size) in our 'struct'
    shellcode += x86.Mov(x86.mem('[EDI]'), 'ECX')
    # update size taken in shared buffer
    shellcode += x86.Add(x86.deref(data_kernel_addr), 'ECX')
    shellcode += x86.Add(x86.deref(data_kernel_addr), 4)
    # Write (char[string_size] filename) in our 'struct'
    shellcode += x86.Add('EDI', 4)
    shellcode += x86.Rep + x86.Movsb()
    shellcode += x86.Label(":END")
    # Restore buffer
    shellcode += x86.Pop('ESI')
    shellcode += x86.Pop('EDI')
    shellcode += x86.Pop('ECX')
    shellcode += x86.Pop('EAX')
    # Jump to NtCreateFile
    shellcode += x86.JmpAt(nt_create_file + 2)

    # Write shellcode
    kdbg.write_pfv_memory(shellcode_addr, shellcode.get_code())
    long_jump = x86.Jmp(shellcode_addr - (nt_create_file - 5))
    # Write longjump to shellcode
    kdbg.write_pfv_memory(nt_create_file - 5, long_jump.get_code())
    # Write shortjump  NtCreateFile -> longjump
    short_jmp = x86.Jmp(-5)
    kdbg.write_pfv_memory(nt_create_file, short_jmp.get_code())
    # Return address of shared buffer in userland
    return data_user_addr

class FilenameReader(object):
    def __init__(self, data_addr):
        self.data_addr = data_addr
        self.current_data = data_addr + 4

    def get_current_filenames(self):
        res = []
        while True:
            t = self.get_one_filename()
            if t is None:
                break
            res.append(t)
        return res

    def get_one_filename(self):
        # Read string size
        size = ctypes.c_uint.from_address(self.current_data).value
        if size == 0:
            return None
        # Read the string
        filename = (ctypes.c_char * size).from_address(self.current_data + 4)[:]
        try:
            filename = filename.decode('utf16')
        except Exception as e:
            import pdb;pdb.set_trace()
            #ignore decode error
            pass
        self.current_data += (size + 4)
        return filename

    def reset_buffer(self):
        ctypes.memmove(self.data_addr, "\x00" * 0x1000, 0x1000)
        self.current_data = data_addr + 4
        
        
try:
    bypass = sys.argv[1] == "/f"
except:
    bypass = False

data_addr = hook_ntcreatefile(kdbg, bypass)
fr = FilenameReader(data_addr)

while True:
    time.sleep(0.1)
    x = fr.get_current_filenames()
    fr.reset_buffer()
    for f in x:
        try:
            print(f)
        except BaseException as e:
            # bypass encode error
            print(repr(f))
