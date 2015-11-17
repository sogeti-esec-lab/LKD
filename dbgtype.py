# # Experimental code # #
import itertools
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
    def bitoffset(self):
        return self.SymGetTypeInfo(TI_GET_BITPOSITION)

    @property
    def bitsize(self):
        return self.SymGetTypeInfo(TI_GET_LENGTH)

    @property
    def is_bitfield(self):
        try:
            self.bitoffset
            return True
        except WindowsError:
            return False

    def __repr__(self):
        if self.is_bitfield:
            bits = "bits" if self.bitsize > 1 else "bit"
            return '<Field <{0}.{1}> at offset <{2}> (Pos {3}, {4} {bits})>'.format(self.parent.name, self.raw_name, hex(self.offset), self.bitoffset, self.bitsize, bits=bits)
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
            raise AttributeError(name)
        field = self.type_field_dict[name]
        addr = self.addr + field.offset

        # Works only for list of same elements as initial structure
        # Fails for nt!_EPROCESS ThreadListHead
        if field.type.name == "_LIST_ENTRY":
            return Mapped_LIST_ENTRY(list_entry_field, addr)

        if field.is_bitfield:
            x = get_mapped_type(field.type, addr)
            bitoff = field.bitoffset
            mask = (2 ** field.bitsize) - 1
            return (x & (mask << bitoff)) >> bitoff
        return get_mapped_type(field.type, addr)

    def __dir__(self):
        l = ["addr", "type", "type_field_dict", "kdbg"]
        return l + self.type_field_dict.keys()

    def __repr__(self):
        return "<Mapped {0} on addr {1}>".format(self.type.name, hex(self.addr))

class Mapped_LIST_ENTRY(DbgEngtypeMapping):
    def __init__(self, field, addr):
        super(Mapped_LIST_ENTRY, self).__init__(field.type, addr)
        self.list_entry_field = field

    def next(self):
        parent = self.list_entry_field.parent
        offset = self.list_entry_field.offset
        return parent(self.Flink[0].addr - offset)

    def prev(self):
        parent = self.list_entry_field.parent
        offset = self.list_entry_field.offset
        return parent(self.Blink[0].addr - offset)

    def current(self):
        parent = self.list_entry_field.parent
        offset = self.list_entry_field.offset
        return parent(self.addr - offset)

    def all(self):
        begin_addr = self.addr
        res = [self.current()]
        first_entry = res[0].addr
        v = self
        while True:
            x = v.next()
            if x.addr == first_entry:
                return res
            res.append(x)
            v = getattr(x, self.list_entry_field.name)

    def __repr__(self):
        field = self.list_entry_field
        return "<_LIST_ENTRY {0}.{1} at {2}>".format(field.parent.name, field.name, hex(id(self)))


class DbgEngtypeMappingPtr(object):
    def __init__(self, type, addr):
        if type.is_array:
            self.addr = addr
        else:
            self.addr = type.kdbg.read_ptr(addr)

        self.type = type
        self.kdbg = type.kdbg

        if not self.type.is_array and not self.type.is_pointer:
            raise ValueError('DbgEngtypeMappingPtr on non ptr type')

    def __repr__(self):
        return "<DbgEngTypePtr to {0} at {1}>".format(self.type.name, hex(id(self)))

    def __getitem__(self, n):
        # Todo: slice
        if isinstance(n, slice):
            return [self._get_one_item(i) for i in  range(*n.indices(n.stop))]
        return self._get_one_item(n)

    def _get_one_item(self, n):
        target_t = self.type.type
        addr = self.addr + target_t.size * n
        return get_mapped_type(target_t, addr)

    def as_str(self):
        res = []
        for i in itertools.count():
            x = self._get_one_item(i)
            if not x:
                return "".join(res)
            res.append(chr(x))
        raise Exception("Unreachable code")


# Example
# >>> k = kdbg.get_type("nt", "_KPRCB")
# >>> t = k(0xfffff8016c167000)
# >>> t.WheaInfo
# 18446708889364968624L
