import sys
import os

# Import test purpose
BAD_PFW = "C:\\Users\\hakril\\Documents\\Work\\PythonForWindows"

if BAD_PFW in sys.path:
    print("Removing <{0}> form sys.path".format(BAD_PFW))
    sys.path.remove(BAD_PFW)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, r"..\PythonForWindows"))



from dbginterface import RemoteDebugger
