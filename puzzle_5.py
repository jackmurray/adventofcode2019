class IntcodeComputer:
    program = []
    ip = 0
    current_params = []

    def load_file(self, filename):
        with open(filename) as file_data:
            self.program = list(map(int, file_data.readline().split(','))) # Read data and convert each element to an int.

    def mem_read(self, addr, addrmode):
        if addrmode == 0: # Position mode
            return self.program[addr]
        if addrmode == 1: # Immediate mode
            return addr
    
    def mem_write(self, addr, value, addrmode):
        if addrmode == 0: # Position mode
            self.program[addr] = value
        raise ValueError("Only position mode supported for memory writes.")
    

    def op_add(self):
        self.program[self.program[self.ip+3]] = self.program[self.program[self.ip+1]] + self.program[self.program[self.ip+2]]
        self.advance(4)
        return 0

    def op_mul(self):
        self.program[self.program[self.ip+3]] = self.program[self.program[self.ip+1]] * self.program[self.program[self.ip+2]]
        self.advance(4)
        return 0

    def op_input(self):
        val = int(input("Enter value: "))
        self.program[self.program[self.ip+1]] = val
        self.advance(2)

    def op_output(self):
        print(self.program[self.program[self.ip+1]])
        self.advance(2)

    def op_exit(self):
        return -1

    opcode_handler = {
        1: { "func": op_add, "paramcount": 3},
        2: { "func": op_mul, "paramcount": 3},
        3: { "func": op_input, "paramcount": 1},
        4: { "func": op_output, "paramcount": 1},
        99: { "func": op_exit, "paramcount": 0}
    }

    def advance(self, instructioncount):
        self.ip += instructioncount

    def load_params(self, paramcount, modes):
        self.current_params = []
        for i in range(1,paramcount+1):
            raw_val = self.program[self.ip+i]
            current_mode = modes % 10
            val = self.mem_read(raw_val, current_mode)
            self.current_params.append(val)
            modes = int(modes/10) # shift-right


    def execute(self):
        self.ip = 0
        while True:
            raw_opcode = self.program[self.ip]
            opcode = raw_opcode % 100 # opcodes are 2-digit so this is like a bitmask to extract the bottom 2 digits

            # Work out which instruction we have from the last digit of the opcode
            instruction = self.opcode_handler.get(opcode)
            func = instruction['func']
            paramcount = instruction['paramcount']
            # Work out the addressing mode for each instruction and store them ready for use.
            modes = int((raw_opcode - opcode)/100) # Strip off the actual opcode and leave just the addressing modes.
            
            self.load_params(paramcount, modes)

            result = func(self)
            if result == -1:
                break


if __name__ == "__main__":
    computer = IntcodeComputer()
    computer.load_file("inputs/puzzle_2.txt")
    computer.execute()
    print("Final program state: {0}".format(computer.program))