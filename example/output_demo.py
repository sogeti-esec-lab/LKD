"""A simple demonstration of the output possibilities of the LDK"""
import sys
import os
if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))

from dbginterface import LocalKernelDebugger

# A default LKD can be quiet or not
# A quiet LKD will have no output
# A noisy one will have the exact same output as windbg
kdbg = LocalKernelDebugger(quiet=True)

# With a quiet LKD this ligne will have no output
print('Executing "lm m nt*" in quiet LKD')
kdbg.execute("lm m nt*")

# To change the quiet state of the LKD just set the variable 'quiet'
kdbg.quiet = False
print("")
print('Executing "lm m nt*" in noisy LKD')
kdbg.execute("lm m nt*")

# If you want to parse the output of a command, kdbg.execute accept the argument 'to_string'
# A command with to_string=True will have no output, even with quiet=False
print("")
disas = kdbg.execute("u nt!NtCreateFile", to_string=True)
print('Here is the 3rd line of the command "u nt!NtCreateFile"')
print(disas.split("\n")[2])


# You can also register a new output callabck that must respect the interface
# IDebugOutputCallbacks::Output (https://msdn.microsoft.com/en-us/library/windows/hardware/ff550815%28v=vs.85%29.aspx)
def my_output_callback(comobj, mask, text):
    print("NEW MESSAGE <{0}>".format(repr(text)))
    # mysocket.send(text)
    return 0

kdbg.set_output_callbacks(my_output_callback)
print("")
print('Executing "u nt!NtCreateFile L1" with custom output callback')
kdbg.execute("u nt!NtCreateFile L1")
