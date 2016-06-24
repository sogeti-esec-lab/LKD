from lkd.dbgdef import *

resolve_type_dict = {"nt!AlpcPortObjectType": ("nt", "_ALPC_PORT")}
PAGE_SIZE = 0x1000

def resolve_object_type(dbg, typeidex):
    type_table = dbg.resolve_symbol("nt!ObTypeIndexTable")
    targettype = dbg.read_ptr(type_table + (dbg.ptr_size * typeidex))
    for typeptr, rtype in resolve_type_dict.items():
        if dbg.read_ptr(typeptr) == targettype:
            return dbg.get_type(*rtype)
    raise ValueError("Type <0x{0:x}> not found".format(targettype))

tst = ["nt!_OBJECT_HEADER_CREATOR_INFO",
"nt!_OBJECT_HEADER_NAME_INFO",
"nt!_OBJECT_HEADER_HANDLE_INFO",
"nt!_OBJECT_HEADER_QUOTA_INFO",
"nt!_OBJECT_HEADER_PROCESS_INFO"]

def resolve_handle(dbg, handle, process=None):
    if process is None:
        process = dbg.current_process()
    if handle & 0x80000000:
        handle = handle & 0x7fffffff
        raw_table_code = dbg.get_type("nt", "_HANDLE_TABLE")(dbg.read_ptr("nt!ObpKernelHandleTable")).TableCode
    else:
        raw_table_code = process.ObjectTable[0].TableCode
    handle_table_entry_type = dbg.get_type("nt", "_HANDLE_TABLE_ENTRY")
    ptr_size = dbg.ptr_size
    if handle_table_entry_type.size != dbg.ptr_size * 2:
        raise ValueError("Unexpected sizeof(_HANDLE_TABLE_ENTRY): {0}".format(handle_table_entry_type.size))
    nested_level = raw_table_code & 3
    table_code = raw_table_code & 0xfffffffc
    nb_handle_entry_by_page = PAGE_SIZE / handle_table_entry_type.size
    if nested_level:
        if nested_level > 1:
            raise NotImplementedError("Nested handle table with nested > 1")
        table_code = dbg.read_ptr(table_code + ((handle >> 2) / nb_handle_entry_by_page) * ptr_size)

    else:
        if (handle >> 2) > nb_handle_entry_by_page:
            raise ValueError("Not nested by handle nb doest not fit")
    entry_addr = table_code + (((handle >> 2) % nb_handle_entry_by_page) * handle_table_entry_type.size)
    try:
        object_header = handle_table_entry_type(entry_addr).LowValue & 0xfffffff8
    except Exception as e:
        import pdb;pdb.set_trace()
        print("Error reading handle")
        return
    body_offset = dbg.get_type("nt", "_OBJECT_HEADER").fields_dict["Body"].offset
    header = dbg.get_type("nt", "_OBJECT_HEADER")(object_header)
    type_index = header.TypeIndex
    body = resolve_object_type(dbg, type_index)(object_header + body_offset)
    return body

def get_header(dbg, object):
    obj_header = dbg.get_type("nt", "_OBJECT_HEADER")
    return obj_header(object.addr - obj_header.fields_dict["Body"].offset)

def get_name_info(dbg, object):
    # Windows 7 only
    header = get_header(dbg, object)
    info_name_addr = header.addr
    if not header.InfoMask & 2:
        return None
    if header.InfoMask & 1:
        info_name_addr -= dbg.get_type("nt", "_OBJECT_HEADER_CREATOR_INFO").size
    info_name_type = dbg.get_type("nt", "_OBJECT_HEADER_NAME_INFO")
    return info_name_type(info_name_addr - info_name_type.size)


