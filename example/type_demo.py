"""A simple demonstration of the type exploration in LDK"""
import sys
import os
if os.getcwd().endswith("example"):
    sys.path.append(os.path.realpath(".."))
else:
    sys.path.append(os.path.realpath("."))

from dbginterface import LocalKernelDebugger


# A lot of IDebugSymbols functions need a type identifier (TypeId) to
# perform operation on said type
# We tried our best to also accept the type name in this case and get
# the type id automatically
# (like the functions that take an address also accept a symbol)

kdbg = LocalKernelDebugger()

type_id = kdbg.get_type_id("nt", "_KPCR")
print('type_id for "nt!_KPCR" is {0}'.format(hex(type_id)))

name = kdbg.get_type_name("nt", type_id)
print("The type name is {0}".format(name))
# proof that you can either use the type_id or the type name in our API
size = kdbg.get_type_size("nt", type_id)
print("The size retrieved using type_id is {0}".format(hex(size)))

size = kdbg.get_type_size("nt", "_KPCR")
print('The size retrieved using "_KPCR" is {0}'.format(hex(size)))

offset = kdbg.get_field_offset("nt", "_KPCR", "IDT")
print('Field "IDT" is at offset {0} in "nt!_KPCR"'.format(hex(offset)))

# Get the type_id and offset of the field PrcbData
prcbdata_type_id, offset = kdbg.get_field_type_and_offset("nt", "_KPCR", "PrcbData")
# Get the name of the type of PrcbData
prcbdata_type_name = kdbg.get_type_name("nt", prcbdata_type_id)
# Get the size of the type of PrcbData
prcbdata_size = kdbg.get_type_size("nt", prcbdata_type_id)
print('PrcbData is a field of type "{0}" (size {1}) at offset {2} in "nt!_KPCR"'.format(prcbdata_type_name, hex(prcbdata_size), hex(offset)))

print("")
print("Listing the 5 firsts fields of {0}".format(prcbdata_type_name))
print("{0}:".format(prcbdata_type_name))
for i in range(5):
    # I don't know a better way of getting the type and offset if field number X than
    # getting the name if field number X
    # getting the type and offset of the field with this name
    name = kdbg.get_field_name("nt", prcbdata_type_id, i)
    type, offset = kdbg.get_field_type_and_offset("nt", prcbdata_type_id, name)
    type_name = kdbg.get_type_name("nt", type)
    print("    +{0} {1:20} {2}".format(hex(offset), name, type_name))




