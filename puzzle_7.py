import itertools

class IntcodeComputer:
    def __init__(self):
        self.program = []
        self.ip = 0
        self.current_params = []
        self.input_buffer = [] # Pre-staged inputs that will be used first when input instructions require input. Elements will be used in index order.
        self.output_buffer = [] # Outputs will be placed here as well as printed to the screen.

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
        else:
            raise ValueError("Only position mode supported for memory writes.")
    
    def param_read(self, paramindex):
        return self.mem_read(self.current_params[paramindex]['value'], self.current_params[paramindex]['mode'])

    def param_write(self, paramindex, value):
        return self.mem_write(self.current_params[paramindex]['value'], value, self.current_params[paramindex]['mode'])

    def op_add(self):
        v1 = self.param_read(0)
        v2 = self.param_read(1)
        self.param_write(2, v1 + v2)
        self.advance(4)
        return 0

    def op_mul(self):
        self.param_write(2, self.param_read(0) * self.param_read(1))
        self.advance(4)
        return 0

    def op_input(self):
        if len(self.input_buffer) > 0:
            val = self.input_buffer.pop()
        else:
            val = int(input("Enter value: "))
        self.param_write(0, val)
        self.advance(2)

    def op_output(self):
        #print(self.param_read(0))
        self.output_buffer.append(self.param_read(0))
        self.advance(2)

    def op_jtrue(self):
        if self.param_read(0) != 0:
            self.ip = self.param_read(1)
        else:
            self.advance(3)

    def op_jfalse(self):
        if self.param_read(0) == 0:
            self.ip = self.param_read(1)
        else:
            self.advance(3)

    def op_lessthan(self):
        if self.param_read(0) < self.param_read(1):
            self.param_write(2, 1)
        else:
            self.param_write(2, 0)
        self.advance(4)

    def op_equals(self):
        if self.param_read(0) == self.param_read(1):
            self.param_write(2, 1)
        else:
            self.param_write(2, 0)
        self.advance(4)

    def op_exit(self):
        return -1

    opcode_handler = {
        1: { "func": op_add, "paramcount": 3},
        2: { "func": op_mul, "paramcount": 3},
        3: { "func": op_input, "paramcount": 1},
        4: { "func": op_output, "paramcount": 1},
        5: { "func": op_jtrue, "paramcount": 2},
        6: { "func": op_jfalse, "paramcount": 2},
        7: { "func": op_lessthan, "paramcount": 3},
        8: { "func": op_equals, "paramcount": 3},
        99: { "func": op_exit, "paramcount": 0}
    }

    def advance(self, instructioncount):
        self.ip += instructioncount

    def load_params(self, paramcount, modes):
        self.current_params = []
        for i in range(1,paramcount+1):
            val = self.program[self.ip+i]
            current_mode = modes % 10
            self.current_params.append({ "value": val, "mode": current_mode })
            modes = int(modes/10) # shift-right


    def execute(self):
        self.ip = 0
        if len(self.input_buffer) > 0:
            self.input_buffer.reverse() # Reverse the list so we can use pop() later on to pull elements out.
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


def run_amps(phase_list):
    amp_input = 0 # We start with 0, later will use output from prev amp.
    for i in range(0,5):
        # Set up amplifier computers
        amp = IntcodeComputer()
        amp.load_file("./inputs/puzzle_7.txt") # All computers run the same code
        amp.input_buffer = [phase_list[i], amp_input]
        amp.execute()
        amp_input = amp.output_buffer[0]
    return amp_input # The output from the last amp is the final thruster value

if __name__ == "__main__":
    # We know that the possible inputs is all the permutations of the numbers 0-4.
    input_list = list(itertools.permutations(range(0,5)))
    winner = 0
    winning_input = None
    for attempt in input_list:
        result = run_amps(attempt)
        if result > winner:
            winner = result
            winning_input = attempt
    print(winner)
    print(winning_input)