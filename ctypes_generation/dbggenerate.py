import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, r"..\PythonForWindows\ctypes_generation"))
import generate

pjoin = os.path.join
from_here = lambda path: pjoin(SCRIPT_DIR, path)

class DBGCOMGenerator(generate.COMGenerator):
    def generate_import(self):
        deps = "\n".join(["from windows.generated_def.{0} import *".format(os.path.basename(dep.outfilename).rsplit(".")[0]) for dep in self.dependances])
        return self.IMPORT_HEADER.format(deps = deps)

class DBGDefGenerator(generate.DefGenerator):
    HEADER = 'SE_DEBUG_NAME = "SeDebugPrivilege"'
    def generate_import(self):
        deps = "\n".join(["from windows.generated_def.{0} import *".format(os.path.basename(dep.outfilename).rsplit(".")[0]) for dep in self.dependances])
        return self.IMPORT_HEADER.format(deps = deps)

    def analyse(self, data):
        for defin in data:
            self.add_exports(defin.name)

class DBGFuncGenerator(generate.FuncGenerator):
    def generate_import(self):
        lkd_deps = "\n".join(["from lkd.{0} import *".format(os.path.basename(dep.outfilename).rsplit(".")[0]) for dep in self.dependances if getattr(dep, "local", False)])
        pfw_deps = "\n".join(["from windows.generated_def.{0} import *".format(os.path.basename(dep.outfilename).rsplit(".")[0]) for dep in self.dependances if not getattr(dep, "local", False)])
        deps = "\n".join([lkd_deps, pfw_deps])
        return self.IMPORT_HEADER.format(deps = deps)


com = DBGCOMGenerator(from_here("dbginterfaces\\*.txt"),  generate.DEFAULT_INTERFACE_TO_IID, from_here("..\\lkd\\dbgcom.py"), dependances=[generate.structs, generate.com])
com.generate()

defs = DBGDefGenerator(from_here("dbgdef.txt"), from_here("..\\lkd\\dbgdef.py"), dependances=[generate.defs_with_ntstatus])
defs.generate()
defs.local = True

funcs = DBGFuncGenerator(from_here("dbgfunc.txt"), from_here("..\\lkd\\dbgfuncs.py"), dependances=[defs, generate.structs])
funcs.generate()