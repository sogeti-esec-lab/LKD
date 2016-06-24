"""Code that rewrite part of the LKD driver in memory to upgrade its features"""
import itertools
import windows.native_exec.simple_x86 as x86
import windows.native_exec.simple_x64 as x64

DU_MEMALLOC_IOCTL = 0x220027
DU_KCALL_IOCTL = 0x220037
DU_OUT_IOCTL = 0x220057
DU_IN_IOCTL = 0x220067
DU_TEST_INT3_IOCTL = 0x220077

class DriverUpgrader(object):
    PTR_SIZE = None

    def __init__(self, kdbg):
        self.kdbg = kdbg
        self.is_upgraded = False
        self.kldbgdrv = kdbg.get_symbol_offset("kldbgdrv")
        self.ioctl_array = None
        self.ioctl_array_ptr = None
        self.next_code_addr = None
        self.registered_ioctl = []

    def write_pfv_ptr(self, addr, data):
            return self.kdbg.write_ptr_p(self.kdbg.virtual_to_physical(addr), data)

    def register_test(self):
        DOINT3 = x86.MultipleInstr()
        DOINT3 += x86.Int3()
        DOINT3 += x86.Ret()
        self.upgrade_driver_add_new_ioctl_handler(DU_TEST_INT3_IOCTL, DOINT3.get_code())

    def upgrade_driver(self):
        """Upgrade the driver if needed, retrieve infomation
           if driver was already upgraded by a previous session"""
        if self.is_driver_already_upgraded():
            return self.retrieve_upgraded_info()
        return self.full_driver_upgrade()

    def is_driver_already_upgraded(self):
        raise NotImplementedError("Driver dependent")

    def full_driver_upgrade(self):
        raise NotImplementedError("Driver dependent")

    def retrieve_upgraded_info(self):
        """retrieve all information of the upgraded driver state from memory"""
        kldbgdrv = self.kldbgdrv
        self.registered_ioctl = self.parse_driver_ioctl_table()
        registered_ioctl_code = [x[0] for x in self.registered_ioctl]
        if DU_MEMALLOC_IOCTL not in registered_ioctl_code:
            # Already upgraded driver cannot perform memory allocation
            # It would be complicated to retrieve a stable state
            # Perform a full upgrade instead
            self.registered_ioctl = []
            return self.full_driver_upgrade()

        self.next_code_addr = self.kdbg.alloc_memory(0x1000)
        self.ioctl_array = self.kdbg.read_ptr(kldbgdrv + self.HANDLE_ARRAY_ADDR)
        self.is_upgraded = True

    def parse_driver_ioctl_table(self):
        kldbgdrv = self.kldbgdrv
        handle_array_addr = self.kdbg.read_ptr(kldbgdrv + self.HANDLE_ARRAY_ADDR)
        res = []
        for i in itertools.count():
            ioctl = self.kdbg.read_ptr(handle_array_addr + (self.PTR_SIZE * 2) * i)
            code_addr = self.kdbg.read_ptr(handle_array_addr + (self.PTR_SIZE * 2) * i + self.PTR_SIZE)
            if ioctl == 0:
                return res
            res.append((ioctl, code_addr))

    def upgrade_driver_add_new_ioctl_handler(self, iocode, code):
        """Add an handler for a new IOCODE
            the code of the handler is written somewhere in kernel and the address is added
            the the IOCODE/Handler array
        """
        next_array_entry = self.ioctl_array + (len(self.registered_ioctl) * (self.PTR_SIZE * 2))
        self.kdbg.write_pfv_memory(self.next_code_addr, code)
        # Set following entry a 0 for safety
        self.write_pfv_ptr(next_array_entry + (2 * self.PTR_SIZE), 0)
        self.write_pfv_ptr(next_array_entry + (3 * self.PTR_SIZE), 0)
        # Setup new entry
        self.write_pfv_ptr(next_array_entry, iocode)
        self.write_pfv_ptr(next_array_entry + (1 * self.PTR_SIZE), self.next_code_addr)

        self.registered_ioctl.append((iocode, self.next_code_addr))
        self.next_code_addr += len(code)





class DriverUpgrader32(DriverUpgrader):
    """Upgrader for windbg_driver_x86.sys (sha-1 D766D6393C3BEC3D4AB1568D373B565BB85EB665)

    Explanation:

        the function `upgrade_driver` will add some code to the DeviceIoControl handler
        The added code will replace the code of the driver initialisation

        The new code search the IoControlCode in an array of IOCODE/Handler and call
        the corresponding handler with the following parameters:

            ESI -> IO_STACK_LOCATION that contains:
                : The input buffer size
                : The input buffer
                : The output buffer size

            EDI -> IRP that contains:
                : The output buffer

            The handler must:
                - Verify the size of input / output buffer
                - Do whatever it wants
                - Write the returned values in the output buffer
                - Return 0 if everything went well
                - Return an error code otherwise

        Adding a new handler is simple, we just need to add the IOCODE/HANDLER to the handler array.
        It can be done by calling:

            self.upgrade_driver_add_new_ioctl_handler(IOCODE, HANDLER_CODE)
    """
    PTR_SIZE = 4
    # Offset of the function we will rewrite in the driver
    init_function_offset = 0xD10
    # Offset of the jump in the iohandle that we will hijack
    hijack_offset = 0xb1f
    # Offset to the `fail` function end
    failed_offset = 0xC2B
    # Offset to `success` function end
    normal_end = 0xC32
    # Address of the pointer to the IOCODE/HANDLER array
    HANDLE_ARRAY_ADDR = 0xCBA
    FIRST_ARRAY_ADDR = HANDLE_ARRAY_ADDR + 4

    # Memory access often used in new handler: based on the parameters expected
    IO_STACK_OUPUT_BUFFER_LEN = x86.mem('[ESI + 4]')
    IO_STACK_INPUT_BUFFER_LEN = x86.mem('[ESI + 8]')
    IO_STACK_INPUT_BUFFER =     x86.mem('[ESI + 0x10]')
    IRP_OUTPUT_BUFFER =         x86.mem('[EDI + 0x3c]')

    def _upgrade_driver_inject_base_upgrade(self):
        kldbgdrv = self.kldbgdrv
        upgrade = x86.MultipleInstr()
        IoControlCode_on_stack = x86.create_displacement(base='EBP', disp=-0x30)
        IO_STACK_LOCATION_on_stack = x86.create_displacement(base='EBP', disp=-0x34)
        IoStatus_on_stack = x86.create_displacement(base='EBP', disp=-0x3c)
        IRP_on_stack = x86.create_displacement(base='EBP', disp=+0x0c)

        upgrade += x86.Mov('EBX', IoControlCode_on_stack)
        upgrade += x86.Mov('EAX', x86.create_displacement(disp=kldbgdrv + self.HANDLE_ARRAY_ADDR))
        upgrade += x86.Label(":LOOP")
        upgrade +=      x86.Mov('ECX', x86.create_displacement('EAX'))
        upgrade +=      x86.Cmp('EBX', 'ECX')
        upgrade +=      x86.Jnz(':END')
        upgrade +=          x86.Mov('EAX', x86.create_displacement('EAX', disp=4))
        # ESI -> IO_STACK_LOCATION
        # EDI -> IRP
        upgrade +=          x86.Mov('ESI', IO_STACK_LOCATION_on_stack)
        upgrade +=          x86.Mov('EDI', IRP_on_stack)
        upgrade +=          x86.Call('EAX')
        upgrade +=          x86.Mov(IoStatus_on_stack, 'EAX')
        upgrade +=          x86.JmpAt(kldbgdrv + self.normal_end)
        upgrade +=      x86.Label(":END")
        upgrade +=      x86.Cmp('ECX', 0)
        upgrade +=      x86.Jnz(':NEXT')
        upgrade +=          x86.JmpAt(kldbgdrv + self.failed_offset)
        upgrade +=      x86.Label(":NEXT")
        upgrade +=      x86.Add('EAX', 8)
        upgrade += x86.Jmp(':LOOP')

        # Write new driver code
        self.kdbg.write_pfv_memory(kldbgdrv + self.init_function_offset, str(upgrade.get_code()))
        # Write first array dest
        self.write_pfv_ptr(kldbgdrv + self.HANDLE_ARRAY_ADDR, kldbgdrv + self.FIRST_ARRAY_ADDR)
        self.write_pfv_ptr(kldbgdrv + self.FIRST_ARRAY_ADDR, 0)
        self.write_pfv_ptr(kldbgdrv + self.FIRST_ARRAY_ADDR + 4, 0)
        # Jump hijack
        jump_init_function = x86.Jmp(self.init_function_offset - (self.hijack_offset))
        self.kdbg.write_pfv_memory(kldbgdrv + self.hijack_offset, str(jump_init_function.get_code()))

        self.is_upgraded = True
        self.ioctl_array = kldbgdrv + self.FIRST_ARRAY_ADDR
        self.ioctl_array_ptr = kldbgdrv + self.HANDLE_ARRAY_ADDR
        self.next_code_addr = kldbgdrv + self.init_function_offset + len(upgrade.get_code())

    def is_driver_already_upgraded(self):
        """Check if the driver have already been upgraded by checking if the jump hijack is in place"""
        jump_hijack = x86.Jmp(self.init_function_offset - (self.hijack_offset)).get_code()
        mem = self.kdbg.read_virtual_memory(self.kldbgdrv + self.hijack_offset, len(jump_hijack))
        return mem == str(jump_hijack)

    def full_driver_upgrade(self):
        """Upgrade the driver, bootstrap it and add new features

            We don't want to write all the handler in the driver init code.
            We bootstrap by only adding the `mem_alloc` feature and use it to:
                - Alloc a new page for the IOCODE/HANDLER array
                - Alloc a new page for the handlers code
            We move the IOCODE/HANDLER array
            Finally we add the other features
        """
        self._upgrade_driver_inject_base_upgrade()
        self.register_alloc_memory()
        new_ioctl_array_page = self.kdbg.alloc_memory(0x1000)

        alloc_ioctl, alloc_code_addr = self.registered_ioctl[0]
        # Write first array dest
        self.write_pfv_ptr(self.ioctl_array_ptr, new_ioctl_array_page)
        self.write_pfv_ptr(new_ioctl_array_page, alloc_ioctl)
        self.write_pfv_ptr(new_ioctl_array_page + 4, alloc_code_addr)
        self.write_pfv_ptr(new_ioctl_array_page + 8, 0)
        self.write_pfv_ptr(new_ioctl_array_page + 0xc, 0)

        self.ioctl_array = new_ioctl_array_page
        new_code_page = self.kdbg.alloc_memory(0x1000)
        self.next_code_addr = new_code_page
        # Register other ioctl
        self.register_kernel_call()
        self.register_io_in()
        self.register_io_out()

    def register_alloc_memory(self):
        ExAllocatePoolWithTag = self.kdbg.get_symbol_offset("nt!ExAllocatePoolWithTag")
        if ExAllocatePoolWithTag is None:
            raise ValueError("Could not resolve <ExAllocatePoolWithTag>")

        INPUT_BUFFER_ALLOC_TYPE = x86.mem('[ECX]')
        INPUT_BUFFER_ALLOC_SIZE = x86.mem('[ECX + 4]')
        INPUT_BUFFER_ALLOC_TAG = x86.mem('[ECX + 8]')

        Alloc_IOCTL = x86.MultipleInstr()
        Alloc_IOCTL += x86.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 0xc)
        Alloc_IOCTL += x86.Jnz(':FAIL')
        Alloc_IOCTL +=     x86.Mov('ECX', self.IO_STACK_INPUT_BUFFER)
        Alloc_IOCTL +=     x86.Mov('EBX', INPUT_BUFFER_ALLOC_TAG)
        Alloc_IOCTL +=     x86.Push('EBX')
        Alloc_IOCTL +=     x86.Mov('EBX', INPUT_BUFFER_ALLOC_SIZE)
        Alloc_IOCTL +=     x86.Push('EBX')
        Alloc_IOCTL +=     x86.Mov('EBX', INPUT_BUFFER_ALLOC_TYPE)
        Alloc_IOCTL +=     x86.Push('EBX')
        Alloc_IOCTL +=     x86.Mov('EAX', ExAllocatePoolWithTag)
        Alloc_IOCTL +=     x86.Call('EAX')
        Alloc_IOCTL +=     x86.Mov('EDX', self.IRP_OUTPUT_BUFFER)
        Alloc_IOCTL +=     x86.Mov(x86.mem('[EDX]'), 'EAX')
        Alloc_IOCTL +=     x86.Xor('EAX', 'EAX')
        Alloc_IOCTL +=     x86.Ret()
        Alloc_IOCTL += x86.Label(":FAIL")
        Alloc_IOCTL += x86.Mov('EAX', 0x0C000000D)
        Alloc_IOCTL += x86.Ret()
        self.upgrade_driver_add_new_ioctl_handler(DU_MEMALLOC_IOCTL, Alloc_IOCTL.get_code())

    def register_kernel_call(self):
        # expect in buffer: the address to call and all dword to push on the stack
        CCall_IOCTL = x86.MultipleInstr()
        CCall_IOCTL += x86.Mov('EAX', self.IO_STACK_INPUT_BUFFER_LEN)
        CCall_IOCTL += x86.Cmp('EAX', 0)
        CCall_IOCTL += x86.Jz(":FAIL")  # Need at least the function to call
        CCall_IOCTL += x86.Mov('ECX', self.IO_STACK_INPUT_BUFFER)
        CCall_IOCTL += x86.Label(':PUSH_NEXT_ARG')
        CCall_IOCTL += x86.Cmp('EAX', 4)
        CCall_IOCTL += x86.Jz(":DO_CALL")
        CCall_IOCTL += x86.Sub('EAX', 4)
        INPUT_BUFFER_NEXT_ARG = x86.create_displacement(base='ECX', index='EAX')
        CCall_IOCTL += x86.Mov('EBX', INPUT_BUFFER_NEXT_ARG)
        CCall_IOCTL += x86.Push('EBX')
        CCall_IOCTL += x86.Jmp(':PUSH_NEXT_ARG')
        CCall_IOCTL += x86.Label(":DO_CALL")
        CCall_IOCTL += x86.Mov('EAX', x86.mem('[ECX]'))
        CCall_IOCTL += x86.Call('EAX')

        CCall_IOCTL += x86.Mov('EDX', self.IRP_OUTPUT_BUFFER)
        CCall_IOCTL += x86.Mov(x86.mem('[EDX]'), 'EAX')
        CCall_IOCTL += x86.Xor('EAX', 'EAX')
        CCall_IOCTL += x86.Ret()
        CCall_IOCTL += x86.Label(":FAIL")
        CCall_IOCTL += x86.Mov('EAX', 0x0C000000D)
        CCall_IOCTL += x86.Ret()
        self.upgrade_driver_add_new_ioctl_handler(DU_KCALL_IOCTL, CCall_IOCTL.get_code())

    def register_io_out(self):
        out_ioctl = x86.MultipleInstr()

        INPUT_BUFFER_SIZE =  x86.mem('[ECX]')
        INPUT_BUFFER_PORT =  x86.mem('[ECX + 4]')
        INPUT_BUFFER_VALUE = x86.mem('[ECX + 8]')

        out_ioctl += x86.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 0xc)  # size indicator / port / value
        out_ioctl += x86.Jnz(":FAIL")
        out_ioctl +=    x86.Mov('ECX', self.IO_STACK_INPUT_BUFFER)
        out_ioctl +=    x86.Mov('EDX', INPUT_BUFFER_PORT)
        out_ioctl +=    x86.Mov('EAX', INPUT_BUFFER_VALUE)
        out_ioctl +=    x86.Mov('ECX', INPUT_BUFFER_SIZE)
        out_ioctl +=    x86.Cmp('ECX', 0x1)
        out_ioctl +=    x86.Jnz(":OUT_2_OR_4")
        out_ioctl +=    x86.Out('DX', 'AL')
        out_ioctl +=    x86.Jmp(':SUCCESS')
        out_ioctl +=    x86.Label(":OUT_2_OR_4")
        out_ioctl +=    x86.Cmp('ECX', 0x2)
        out_ioctl +=    x86.Jnz(":OUT_4")
        out_ioctl +=    x86.Out('DX', 'AX')
        out_ioctl +=    x86.Jmp(':SUCCESS')
        out_ioctl +=    x86.Label(":OUT_4")
        out_ioctl +=    x86.Out('DX', 'EAX')
        out_ioctl +=    x86.Label(":SUCCESS")
        out_ioctl +=    x86.Xor('EAX', 'EAX')
        out_ioctl +=    x86.Ret()
        out_ioctl += x86.Label(":FAIL")
        out_ioctl += x86.Mov('EAX', 0x0C000000D)
        out_ioctl += x86.Ret()

        self.upgrade_driver_add_new_ioctl_handler(DU_OUT_IOCTL, out_ioctl.get_code())

    def register_io_in(self):
        in_ioctl = x86.MultipleInstr()

        INPUT_BUFFER_PORT =  x86.mem('[ECX + 4]')
        INPUT_BUFFER_SIZE =  x86.mem('[ECX]')

        in_ioctl += x86.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 8)  # size indicator / port
        in_ioctl += x86.Jnz(":FAIL")
        in_ioctl += x86.Cmp(self.IO_STACK_OUPUT_BUFFER_LEN, 0x4)
        in_ioctl += x86.Jnz(":FAIL")
        in_ioctl += x86.Mov('ECX', self.IO_STACK_INPUT_BUFFER)
        in_ioctl += x86.Mov('EDX', INPUT_BUFFER_PORT)
        in_ioctl += x86.Mov('ECX', INPUT_BUFFER_SIZE)
        in_ioctl += x86.Xor('EAX', 'EAX')
        in_ioctl += x86.Cmp('ECX', 0x1)
        in_ioctl += x86.Jnz(":IN_2_OR_4")
        in_ioctl += x86.In('AL', 'DX')
        in_ioctl += x86.Jmp(':SUCCESS')
        in_ioctl += x86.Label(":IN_2_OR_4")
        in_ioctl += x86.Cmp('ECX', 0x2)
        in_ioctl += x86.Jnz(":IN_4")
        in_ioctl += x86.In('AX', 'DX')
        in_ioctl += x86.Jmp(':SUCCESS')
        in_ioctl += x86.Label(":IN_4")
        in_ioctl += x86.In('EAX', 'DX')
        in_ioctl += x86.Label(":SUCCESS")
        in_ioctl += x86.Mov('EDX', self.IRP_OUTPUT_BUFFER)
        in_ioctl += x86.Mov(x86.mem('[EDX]'), 'EAX')
        in_ioctl += x86.Xor('EAX', 'EAX')
        in_ioctl += x86.Ret()
        in_ioctl += x86.Label(":FAIL")
        in_ioctl += x86.Mov('EAX', 0x0C000000D)
        in_ioctl += x86.Ret()

        self.upgrade_driver_add_new_ioctl_handler(DU_IN_IOCTL, in_ioctl.get_code())


class DriverUpgrader64(DriverUpgrader):
    """Upgrader for windbg_driver_x64.sys (sha-1 6F5B29FFFB021BF80CA91D6D67CFC019D63F7175)

    Explanation:

        the function `upgrade_driver` will add some code to the DeviceIoControl handler
        The added code will be written in in some empty space after the driver code

        The new code search the IoControlCode in an array of IOCODE/Handler and call
        the corresponding handler with the following parameters:

            RSI -> IO_STACK_LOCATION that contains:
                : The input buffer size
                : The input buffer
                : The output buffer size

            RDI -> IRP that contains:
                : The output buffer

            The handler must:
                - Verify the size of input / output buffer
                - Do whatever it wants
                - Write the returned values in the output buffer
                - Return 0 if everythin went well
                - Return an error code otherwise

        Adding a new handler is simple, we just need to add the IOCODE/HANDLER to the handler array.
        It can be done by calling:

            self.upgrade_driver_add_new_ioctl_handler(IOCODE, HANDLER_CODE)
    """
    PTR_SIZE = 8
    # Offset of the code in the iohandle that we will hijack
    hijack_offset = 0x50e8
    # Offset of the normal code path in the iohandle for the standard IO_CODE
    normal_io_offset = 0x50f1
    # Offset of the function we will rewrite in the driver
    init_driver_offset = 0x523a
    # Offset to the `fail` function end
    fail_offset = 0x50f7
    # Offset to `success` function end
    normal_end_offset = 0x51d8

    # Address of the pointer to the IOCODE/HANDLER array
    HANDLE_ARRAY_ADDR = 0x5300
    FIRST_ARRAY_ADDR = HANDLE_ARRAY_ADDR + 8

    # Memory access often used in new handler: based on the parameters expected
    IO_STACK_INPUT_BUFFER_LEN = x64.mem('[RSI + 0x10]')
    IO_STACK_INPUT_BUFFER =     x64.mem('[RSI + 0x20]')
    IRP_OUTPUT_BUFFER =         x64.mem('[RDI + 0x70]')

    NORMAL_IO_CODE = 0x22C007

    def _upgrade_driver_inject_base_upgrade(self):
        kldbgdrv = self.kldbgdrv
        upgrade = x64.MultipleInstr()
        # R14 : IOCODE
        # RSI -> IO_STACK_LOCATION
        # RDI -> IRP
        upgrade = x64.MultipleInstr()
        upgrade += x64.Cmp('R14', self.NORMAL_IO_CODE)
        upgrade += x64.Jz(self.normal_io_offset - (self.init_driver_offset + len(upgrade.get_code())))
        upgrade += x64.Mov('Rax', x64.create_displacement(disp=kldbgdrv + self.HANDLE_ARRAY_ADDR))
        upgrade += x64.Label(":LOOP")
        upgrade +=      x64.Mov('RCX', x64.create_displacement('RAX'))
        upgrade +=      x64.Cmp('R14', 'RCX')
        upgrade +=      x64.Jnz(':END')
        upgrade +=          x64.Mov('RAX', x64.create_displacement('RAX', disp=8))
        upgrade +=          x64.Call('RAX')
        upgrade +=          x64.Mov('RBX', 'RAX')
        upgrade +=          x64.JmpAt(kldbgdrv + self.normal_end_offset)
        upgrade +=      x64.Label(":END")
        upgrade +=      x64.Cmp('RCX', 0)
        upgrade +=      x64.Jnz(':NEXT')
        upgrade +=          x64.JmpAt(kldbgdrv + self.fail_offset)
        upgrade +=      x64.Label(":NEXT")
        upgrade +=      x64.Add('RAX', 0x10)
        upgrade += x64.Jmp(':LOOP')

        self.kdbg.write_pfv_memory(kldbgdrv + self.init_driver_offset, str(upgrade.get_code()))
        # Write first array dest
        self.write_pfv_ptr(kldbgdrv + self.HANDLE_ARRAY_ADDR, kldbgdrv + self.FIRST_ARRAY_ADDR)
        self.write_pfv_ptr(kldbgdrv + self.FIRST_ARRAY_ADDR, 0)
        self.write_pfv_ptr(kldbgdrv + self.FIRST_ARRAY_ADDR + 8, 0)
        # Jump hijack
        jump_init_function = x64.Jmp(self.init_driver_offset - (self.hijack_offset))
        self.kdbg.write_pfv_memory(kldbgdrv + self.hijack_offset, str(jump_init_function.get_code()))

        self.ioctl_array = kldbgdrv + self.FIRST_ARRAY_ADDR
        self.ioctl_array_ptr = kldbgdrv + self.HANDLE_ARRAY_ADDR
        self.next_code_addr = kldbgdrv + self.init_driver_offset + len(upgrade.get_code())
        self.is_upgraded = True

    def is_driver_already_upgraded(self):
        """Check if the driver have already been upgraded by checking if the jump hijack is in place"""
        jump_hijack = x64.Jmp(self.init_driver_offset - (self.hijack_offset)).get_code()
        mem = self.kdbg.read_virtual_memory(self.kldbgdrv + self.hijack_offset, len(jump_hijack))
        return mem == str(jump_hijack)

    def full_driver_upgrade(self):
        """Upgrade the driver, bootstrap it and add new features

            We don't want to write all the handler in the driver init code.
            We bootstrap be only adding the `mem_alloc` feature and use it to:
                - Alloc a new page for the IOCODE/HANDLER array
                - Alloc a new page for the handlers code
            We move the IOCODE/HANDLER array
            Finally we add the other features
        """
        self._upgrade_driver_inject_base_upgrade()
        self.register_alloc_memory()
        new_ioctl_array_page = self.kdbg.alloc_memory(0x1000)
        alloc_ioctl, alloc_code_addr = self.registered_ioctl[0]

        # Write first array dest
        self.write_pfv_ptr(self.ioctl_array_ptr, new_ioctl_array_page)
        self.write_pfv_ptr(new_ioctl_array_page, alloc_ioctl)
        self.write_pfv_ptr(new_ioctl_array_page + 0x8, alloc_code_addr)
        self.write_pfv_ptr(new_ioctl_array_page + 0x10, 0)
        self.write_pfv_ptr(new_ioctl_array_page + 0x18, 0)
        self.ioctl_array = new_ioctl_array_page

        new_code_page = self.kdbg.alloc_memory(0x1000)
        self.next_code_addr = new_code_page
        # Register other IOCTL
        self.register_kernel_call()
        self.register_io_in()
        self.register_io_out()

    def register_alloc_memory(self):
        ExAllocatePoolWithTag = self.kdbg.get_symbol_offset("nt!ExAllocatePoolWithTag")
        if ExAllocatePoolWithTag is None:
            raise ValueError("Could not resolve <ExAllocatePoolWithTag>")

        INPUT_BUFFER_ALLOC_TYPE = x64.mem('[RCX]')
        INPUT_BUFFER_ALLOC_SIZE = x64.mem('[RCX + 0x8]')
        INPUT_BUFFER_ALLOC_TAG = x64.mem('[RCX + 0x10]')

        Alloc_IOCTL = x64.MultipleInstr()
        Alloc_IOCTL += x64.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 0x18)
        Alloc_IOCTL += x64.Jnz(':FAIL')
        Alloc_IOCTL += x64.Mov('RCX', self.IO_STACK_INPUT_BUFFER)
        Alloc_IOCTL += x64.Mov('R8', INPUT_BUFFER_ALLOC_TAG)
        Alloc_IOCTL += x64.Mov('RDX', INPUT_BUFFER_ALLOC_SIZE)
        Alloc_IOCTL += x64.Mov('RCX', INPUT_BUFFER_ALLOC_TYPE)
        Alloc_IOCTL += x64.Mov('RAX', ExAllocatePoolWithTag)
        Alloc_IOCTL += x64.Call('RAX')
        Alloc_IOCTL += x64.Mov('RBX', self.IRP_OUTPUT_BUFFER)
        Alloc_IOCTL += x64.Mov(x64.mem('[RBX]'), 'RAX')
        Alloc_IOCTL += x64.Xor('RAX', 'RAX')
        Alloc_IOCTL += x64.Ret()
        Alloc_IOCTL += x64.Label(":FAIL")
        Alloc_IOCTL += x64.Mov('RAX', 0x0C000000D)
        Alloc_IOCTL += x64.Ret()

        self.upgrade_driver_add_new_ioctl_handler(DU_MEMALLOC_IOCTL, Alloc_IOCTL.get_code())

    def register_kernel_call(self):
        # expect in buffer: the address to call and all dword to push on the stack
        CCall_IOCTL = x64.MultipleInstr()
        CCall_IOCTL += x64.Mov('RAX', self.IO_STACK_INPUT_BUFFER_LEN)
        CCall_IOCTL += x64.Cmp('RAX', 0)
        CCall_IOCTL += x64.Jz(":FAIL")  # Need at least the function to call
        CCall_IOCTL += x64.Mov('R15', 4 * 8)  # Size to pop on the stack at the end (4 * push RDI)
        CCall_IOCTL += x64.Mov('R10', self.IO_STACK_INPUT_BUFFER)
        CCall_IOCTL += x64.Label(':PUSH_NEXT_ARG')
        CCall_IOCTL += x64.Cmp('RAX', (8 * 5))
        CCall_IOCTL += x64.Jbe(":SETUP_REG_ARGS")
        CCall_IOCTL += x64.Sub('RAX', 8)
        INPUT_BUFFER_NEXT_ARG = x64.create_displacement(base='R10', index='RAX')
        CCall_IOCTL += x64.Mov('RBX', INPUT_BUFFER_NEXT_ARG)
        CCall_IOCTL += x64.Push('RBX')
        CCall_IOCTL += x64.Add('R15', 8)  # Add at Size to pop on the stack at the end
        CCall_IOCTL += x64.Jmp(':PUSH_NEXT_ARG')
        CCall_IOCTL += x64.Label(":SETUP_REG_ARGS")
        # Could be done in a loop
        # But do I really want to generate x86 in a loop..
        CCall_IOCTL += x64.Cmp('RAX', (8 * 5))
        CCall_IOCTL += x64.Jz(":SETUP_4_ARGS")
        CCall_IOCTL += x64.Cmp('RAX', (8 * 4))
        CCall_IOCTL += x64.Jz(":SETUP_3_ARGS")
        CCall_IOCTL += x64.Cmp('RAX', (8 * 3))
        CCall_IOCTL += x64.Jz(":SETUP_2_ARGS")
        CCall_IOCTL += x64.Cmp('RAX', (8 * 2))
        CCall_IOCTL += x64.Jz(":SETUP_1_ARGS")
        CCall_IOCTL += x64.Jmp(":SETUP_0_ARGS")
        CCall_IOCTL += x64.Label(":SETUP_4_ARGS")
        CCall_IOCTL += x64.Mov('R9', x64.mem('[R10 + 0x20]'))
        CCall_IOCTL += x64.Label(":SETUP_3_ARGS")
        CCall_IOCTL += x64.Mov('R8', x64.mem('[R10 + 0x18]'))
        CCall_IOCTL += x64.Label(":SETUP_2_ARGS")
        CCall_IOCTL += x64.Mov('RDX', x64.mem('[R10 + 0x10]'))
        CCall_IOCTL += x64.Label(":SETUP_1_ARGS")
        CCall_IOCTL += x64.Mov('RCX', x64.mem('[R10 + 8]'))
        CCall_IOCTL += x64.Label(":SETUP_0_ARGS")
        CCall_IOCTL += x64.Mov('RAX', x64.mem('[R10]'))
        # Fix Reserve space (calling convention)
        CCall_IOCTL += x64.Push('RDI')
        CCall_IOCTL += x64.Push('RDI')
        CCall_IOCTL += x64.Push('RDI')
        CCall_IOCTL += x64.Push('RDI')
        CCall_IOCTL += x64.Call('RAX')
        CCall_IOCTL += x64.Mov('RDX', self.IRP_OUTPUT_BUFFER)
        CCall_IOCTL += x64.Mov(x64.mem('[RDX]'), 'RAX')
        CCall_IOCTL += x64.Xor('RAX', 'RAX')
        CCall_IOCTL += x64.Add('RSP', 'R15')
        CCall_IOCTL += x64.Ret()
        CCall_IOCTL += x64.Label(":FAIL")
        CCall_IOCTL += x64.Mov('RAX', 0x0C000000D)
        CCall_IOCTL += x64.Ret()
        self.upgrade_driver_add_new_ioctl_handler(DU_KCALL_IOCTL, CCall_IOCTL.get_code())

    def register_io_out(self):
        out_ioctl = x64.MultipleInstr()

        INPUT_BUFFER_SIZE =  x64.mem('[RCX]')
        INPUT_BUFFER_PORT =  x64.mem('[RCX + 8]')
        INPUT_BUFFER_VALUE = x64.mem('[RCX + 0x10]')

        out_ioctl += x64.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 0x18)  # size indicator / port / value
        out_ioctl += x64.Jnz(":FAIL")
        out_ioctl +=    x64.Mov('RCX', self.IO_STACK_INPUT_BUFFER)
        out_ioctl +=    x64.Mov('RDX', INPUT_BUFFER_PORT)
        out_ioctl +=    x64.Mov('RAX', INPUT_BUFFER_VALUE)
        out_ioctl +=    x64.Mov('RCX', INPUT_BUFFER_SIZE)
        out_ioctl +=    x64.Cmp('RCX', 0x1)
        out_ioctl +=    x64.Jnz(":OUT_2_OR_4")
        out_ioctl +=    x64.Out('DX', 'AL')
        out_ioctl +=    x64.Jmp(':SUCCESS')
        out_ioctl +=    x64.Label(":OUT_2_OR_4")
        out_ioctl +=    x64.Cmp('RCX', 0x2)
        out_ioctl +=    x64.Jnz(":OUT_4")
        out_ioctl +=    x64.Out('DX', 'AX')
        out_ioctl +=    x64.Jmp(':SUCCESS')
        out_ioctl +=    x64.Label(":OUT_4")
        out_ioctl +=    x64.Out('DX', 'EAX')
        out_ioctl +=    x64.Label(":SUCCESS")
        out_ioctl +=    x64.Xor('RAX', 'RAX')
        out_ioctl +=    x64.Ret()
        out_ioctl += x64.Label(":FAIL")
        out_ioctl += x64.Mov('RAX', 0x0C000000D)
        out_ioctl += x64.Ret()

        self.upgrade_driver_add_new_ioctl_handler(DU_OUT_IOCTL, out_ioctl.get_code())

    def register_io_in(self):
        in_ioctl = x64.MultipleInstr()

        INPUT_BUFFER_SIZE =  x64.mem('[RCX]')
        INPUT_BUFFER_PORT =  x64.mem('[RCX + 8]')

        in_ioctl += x64.Cmp(self.IO_STACK_INPUT_BUFFER_LEN, 0x10)  # size indicator / port
        in_ioctl += x64.Jnz(":FAIL")
        in_ioctl +=    x64.Mov('RCX', self.IO_STACK_INPUT_BUFFER)
        in_ioctl +=    x64.Mov('RDX', INPUT_BUFFER_PORT)
        in_ioctl +=    x64.Mov('RCX', INPUT_BUFFER_SIZE)
        in_ioctl +=    x64.Cmp('RCX', 0x1)
        in_ioctl +=    x64.Jnz(":OUT_2_OR_4")
        in_ioctl +=    x64.In('AL', 'DX')
        in_ioctl +=    x64.Jmp(':SUCCESS')
        in_ioctl +=    x64.Label(":OUT_2_OR_4")
        in_ioctl +=    x64.Cmp('RCX', 0x2)
        in_ioctl +=    x64.Jnz(":OUT_4")
        in_ioctl +=    x64.In('AX', 'DX')
        in_ioctl +=    x64.Jmp(':SUCCESS')
        in_ioctl +=    x64.Label(":OUT_4")
        in_ioctl +=    x64.In('EAX', 'DX')
        in_ioctl +=    x64.Label(":SUCCESS")
        in_ioctl += x64.Mov('RDX', self.IRP_OUTPUT_BUFFER)
        in_ioctl += x64.Mov(x64.mem('[RDX]'), 'RAX')
        in_ioctl += x64.Xor('RAX', 'RAX')
        in_ioctl += x64.Ret()
        in_ioctl += x64.Label(":FAIL")
        in_ioctl += x64.Mov('RAX', 0x0C000000D)
        in_ioctl += x64.Ret()

        self.upgrade_driver_add_new_ioctl_handler(DU_IN_IOCTL, in_ioctl.get_code())
