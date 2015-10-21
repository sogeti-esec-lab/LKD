import struct
import ctypes
import functools
from ctypes.wintypes import HRESULT

# Simple Abstraction to call COM interface in Python (Python -> COM)
IID_PACK = "<I", "<H", "<H", "<B", "<B", "<B", "<B", "<B", "<B", "<B", "<B"


def get_IID_from_raw(raw):
    return "".join([struct.pack(i, j) for i, j in zip(IID_PACK, raw)])


class COMInterface(ctypes.c_void_p):
    _functions_ = {
        "QueryInterface": ctypes.WINFUNCTYPE(HRESULT, ctypes.c_void_p, ctypes.c_void_p)(0, "QueryInterface"),
        "AddRef": ctypes.WINFUNCTYPE(HRESULT)(1, "AddRef"),
        "Release": ctypes.WINFUNCTYPE(HRESULT)(2, "Release")
    }

    def __getattr__(self, name):
        if name in self._functions_:
            return functools.partial(self._functions_[name], self)
        return super(COMInterface, self).__getattribute__(name)


# Simple Implem to create COM Interface in Python (COM -> Python)
def BasicQueryInterface(self, *args):
    return 1


def BasicAddRef(self, *args):
    return 1


def BasicRelease(self, *args):
    return 0


def create_c_callable(func, types, keepalive=[]):
    func_type = ctypes.WINFUNCTYPE(*types)
    c_callable = func_type(func)
    # Dirty, but other methods require native code execution
    c_callback_addr = ctypes.c_ulong.from_address(id(c_callable._objects['0']) + 3 * ctypes.sizeof(ctypes.c_void_p)).value
    keepalive.append(c_callable)
    return c_callback_addr


class ComVtable(object):
    # Name, types, DefaultImplem
    _funcs_ = [("QueryInterface", [ctypes.HRESULT, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], BasicQueryInterface),
               ("AddRef", [ctypes.HRESULT, ctypes.c_void_p], BasicAddRef),
               ("Release", [ctypes.HRESULT, ctypes.c_void_p], BasicRelease)
               ]

    def __init__(self):
        raise NotImplementedError("Nop: use create_vtable")

    @classmethod
    def create_vtable(cls, **implem_overwrite):
        vtables_names = [x[0] for x in cls._funcs_]
        non_expected_args = [func_name for func_name in implem_overwrite if func_name not in vtables_names]
        if non_expected_args:
            raise ValueError("Non expected function : {0}".format(non_expected_args))

        implems = []
        for name, types, func_implem in cls._funcs_:
            func_implem = implem_overwrite.get(name, func_implem)
            if func_implem is None:
                raise ValueError("Missing implementation for function <{0}>".format(name))
            implems.append(create_c_callable(func_implem, types))

        class Vtable(ctypes.Structure):
            _fields_ = [(name, ctypes.c_void_p) for name in vtables_names]

        return Vtable(*implems)


class IDebugOutputCallbacksVtable(ComVtable):
    _funcs_ = ComVtable._funcs_ + [("Output", [ctypes.HRESULT, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_char_p], None)]
