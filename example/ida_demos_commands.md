List of commands used in IDA for our hack.lu demo:
Notes:
	
- IDA must be launched as administrator
- Only works on 32bits kernel as `idaq64.exe` is not a 64 bits process

Add the path of LKD in list of import directory (you can also install LKD with the `setup.py`)

	import sys
	sys.path.append(r"<path_of_LKD>")

Create a new LocalKernelDebugger
	
	import dbginterface
	kdbg = dbginterface.LocalKernelDebugger()

Config LKD to print all its output

	kdbg.quiet = False

Read some virtual memory at symbol `nt!KiSystemStartup`

	kdbg.read_virtual_memory("nt!KiSystemStartup", 9).encode('hex')
	
List all modules with name beginning by `nt`

	kdbg.execute("lm m nt*")
	
Get the address of the KPCR for the processor 0

	DEBUG_DATA_KPCR_OFFSET = 0
	PROC_NUMBER = 0
	kpcr_addr = kdbg.read_processor_system_data(PROC_NUMBER, DEBUG_DATA_KPCR_OFFSET)

Print the IDT and GDB fields of the KPCR struct
(For scriptable type manipulation see `example/type_demo.py`)

	kdbg.execute("dt nt!_KPCR IDT GDT 0n{0}".format(kpcr_addr))
	

