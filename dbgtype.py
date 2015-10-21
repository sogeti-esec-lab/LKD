# # Experimental code # #

# Idea: make 2 type
# One for field (with field name / bitfield / parentclass / etc)
# One for the type above (fieldname.type)
# That have info about array size and co

import struct
from windows.generated_def.winstructs import *

class DbgEngTypeBase(object):
    def __init__(self, module, typeid, kdbg):
        self.module = module
        self.module_name = kdbg.get_symbol(module)[0]
        self.typeid = typeid
        self.kdbg = kdbg

    def SymGetTypeInfo(self, GetType):
        return self.kdbg.SymGetTypeInfo(self.module, self.typeid, GetType)

    @property
    def size(self):
        return self.kdbg.get_type_size(self.module, self.typeid)

    @property
    def type(self):
        #if not self.is_array:
        #    raise ValueError("array_type on non array type")
        sub_type = self.kdbg.SymGetTypeInfo(self.module, self.typeid, TI_GET_TYPE)
        return DbgEngType(self.module, sub_type, self.kdbg)

    @property
    def base_type(self):
        #if not self.is_array:
        #    raise ValueError("array_type on non array type")
        sub_type = self.kdbg.SymGetTypeInfo(self.module, self.typeid, TI_GET_BASETYPE)
        return DbgEngType(self.module, sub_type, self.kdbg)

    @property
    def raw_name(self):
        return str(self.SymGetTypeInfo(TI_GET_SYMNAME))

    def __call__(self, addr):
        return DbgEngtypeMapping(self, addr)

class DbgEngType(DbgEngTypeBase):
    @property
    def name(self):
        return self.kdbg.get_type_name(self.module, self.typeid)

    @property
    def is_array(self):
        "Todo: Il doit bien y avoir un truc moins crade :D"
        return self.name.endswith("[]")

    @property
    def is_pointer(self):
        "Todo: Il doit bien y avoir un truc moins crade :D"
        return self.name.endswith("*")

    @property
    def fields(self):
        children = self.kdbg.get_childs_types(self.module, self.typeid)
        return [DbgEngField(self.module, x, self.kdbg) for x in children.Types]

    @property
    def fields_dict(self):
        return {x.name: x for x in self.fields}

    @property
    def number_elt(self):
        return self.SymGetTypeInfo(TI_GET_COUNT)

    def __repr__(self):
        return '<DbgEngType "{0}">'.format(self.name)

    def __call__(self, addr):
        return get_mapped_type(self, addr)

class DbgEngField(DbgEngTypeBase):
    name = DbgEngTypeBase.raw_name

    @property
    def parent(self):
        parent_typeid = self.SymGetTypeInfo(TI_GET_CLASSPARENTID)
        return  DbgEngType(self.module, parent_typeid, self.kdbg)

    @property
    def offset(self):
        return self.SymGetTypeInfo(TI_GET_OFFSET)

    @property
    def bitoff(self):
        return self.SymGetTypeInfo(TI_GET_BITPOSITION)

    def __repr__(self):
        return '<Field <{0}.{1}> at offset <{2}> of type <{3}>>'.format(self.parent.name, self.raw_name, hex(self.offset), self.type.name)


def get_mapped_type(type, addr):

    if type.is_array:
            return DbgEngtypeMappingPtr(type, addr)

    if type.is_pointer and type.name not in ["void*"]:
            return DbgEngtypeMappingPtr(type, addr)

    # basic type: no fields
    if not type.fields:
        unpack_by_size = {1:"B", 2:'H', 4:'I', 8:'Q'}
        data = type.kdbg.read_virtual_memory(addr, type.size)
        return struct.unpack("<" + unpack_by_size[type.size], data)[0]
    return DbgEngtypeMapping(type, addr)


class DbgEngtypeMapping(object):
    def __init__(self, type, addr):
        self.type = type
        self.type_field_dict = {x.name : x for x in type.fields}
        self.addr = addr
        self.kdbg = type.kdbg

    def __getattr__(self, name):
        if name not in self.type_field_dict:
            raise AttributeError

        field = self.type_field_dict[name]
        addr = self.addr + field.offset

        # TODO: bitfield

        return get_mapped_type(field.type, addr)

    def __repr__(self):
        return "<Mapped {0} on addr {1}>".format(self.type.name, hex(self.addr))

        
class DbgEngtypeMappingPtr(object):
    def __init__(self, type, addr):
        self.type = type
        self.addr = addr
        self.kdbg = type.kdbg

        if not self.type.is_array and not self.type.is_pointer:
            raise ValueError('DbgEngtypeMappingPtr on non ptr type')

    def __getitem__(self, n):
        if self.type.is_array:
            addr = self.addr + self.type.size * n
        else:
            addr = self.type.kdbg.read_ptr(self.addr)
            addr += self.type.size * n

        target_t = self.type.type
        return get_mapped_type(target_t, addr)


# Example
# >>> k = kdbg.get_type("nt", "_KPRCB")
# >>> t = k(0xfffff8016c167000)
# >>> t.WheaInfo
# 18446708889364968624L
