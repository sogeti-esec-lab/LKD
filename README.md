# Local Kernel Debugger

Local Kernel Debugger (LKD) is a python wrapper around `dbgengine.dll` to 
perform local kernel debugging of a Windows kernel booted in DEBUG mode.

## How does LKD work ?

Local Kernel Debugging is the ability to perform kernel-mode debugging on a 
single computer. In other words, the debugger runs on the same computer 
that is being debugged.
Windows offers this functionality through WinDbg and KD binaries which allow to
read/write the kernel memory, perform in/out and access MSRs.
WinDbg and KD use `dbgengine.dll` to offer this functionality, but `dbgengine` only 
allows binary with name `windbg.exe` or `kd.exe` and also requires that the said 
binary embeds a driver used to perform the local kernel debugging actions.

To bypass these restrictions we used IAT hook against `dbgengine.dll` to emulate the
resource (that is read from a file) and also change the result of 
`GetModuleFileNameW` to `C:\\windbg.exe`.

With that we are able to retrieve some COM interfaces offered by `dbgengine` and 
used to perform Local Kernel Debugging.
Last problem is that some functionalities we find useful are missing in the 
LKD driver (memory allocation, custom kernel call, ...) so we
use the LKD driver to rewrite some part of it in memory to upgrade its features.

## What you need to know to use LKD

### Symbols

The LKD try to use the usual environment variable `_NT_SYMBOL_PATH` to retrieve the symbol path.
If this variable does not exist it will use the `.\symbols` directory in the current path
of `dbginterface.py`

Some part of LKD need (for now) to have access to the `ntoskrnl` symbols so the 
debugged computer must be connected to Internet at least once.

### 32bits vs 64bits

LKD cannot be done in a SysWow64 process, if you try to debug a 64bits kernel
you will need a 64bits python.

You can find every MSI you need at https://www.python.org/downloads/windows/

### Examples

See the [example directory][EX_DIRECTORY].

## files / directories description

- `dbginterface.py` The main file of the project, LKD objects that setup the IAT hooks for the WinDbg imposture, attach to the local kernel, retrieve the COM interfaces and wrap them.
    
- `resource_emulation.py` IAT hooks that allow to emulate a resource from a file in the File System.
    
- `simple_com.py` Simple wrapper to COM interface (used in [example\output_demo.py][OUTPUT_DEMO]).
    
- `driver_upgrade.py` Code that rewrite part of the LKD driver in memory to upgrade its features
    
- `bin\windbg_driver_x86.sys` LKD (signed) driver for 32bits kernel extracted from WinDbg's resources

- `bin\windbg_driver_x64.sys` LKD (signed) driver for 64bits kernel extracted from WinDbg's resources
    
- `bin\DBGDLL\` dbgengine + symbol engine for windows 32bits
    
- `bin\DBGDLL64\` dbgengine + symbol engine for windows 64bits
    
- `test\` Our test, need to be launched on 32bits and 64bits kernels to be complete
    
- `example\` Our demos code of the use and interest of LKD

- `doc\` Sphinx documentation
    
- `windows\`
Side project with some windows helpers, some part of this are not directly used by LKD.  
The features used are:
    - IAT Hooks
    - Windows API proxy
    - Native execution
    - simple_x86 / simple_x64 assembler

## Shady part of LKD    
  
### `do_in` / `do_out` VS `read_io` / `write_io`

There is a COM API to perform I/O: `WriteIo` and `ReadIo` but it seems that
these API check (`nt!KdpSysReadIoSpace` & `nt!KdpSysWriteIoSpace`) for some alignment in the port and the size.

A ReadIo(size=4) must be on a port aligned on 4.

For performing any I/O, LKD offers two function: `do_in`, `do_out`.

    do_in(self, port, size)
        <require upgraded driver>
        Perform IN instruction in kernel mode
    do_out(self, port, value, size)
        <require upgraded driver>
        Perform OUT instruction in kernel mode

### `expand_address_to_ulong64` / `trim_ulong64_to_address`

Used to convert a symbol address to an ULONG64 requested by the API and vice versa.
Problem is that in a 32bits kernel the kernel addresses are bit expended.

`ntoskrnl` base in 32bits kernel would not be `0x8XXXXXXX` but `0xffffffff8XXXXXXX`.

[EX_DIRECTORY]: https://github.com/sogeti-esec-lab/LKD/tree/master/example
[OUTPUT_DEMO]: https://github.com/sogeti-esec-lab/LKD/blob/master/example/output_demo.py
