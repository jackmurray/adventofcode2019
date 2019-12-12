class IntcodeComputer:
    program = []
    ip = 0

    def load_file(self, filename):
        with open(filename) as file_data:
            self.program = file_data.readline().split(',')

    def op_add(self):
        self.program[self.program[self.ip+3]] = self.program[self.program[self.ip+1]] + self.program[self.program[self.ip+2]]
        return 0

    def op_mul(self):
        self.program[self.program[self.ip+3]] = self.program[self.program[self.ip+1]] * self.program[self.program[self.ip+2]]
        return 0

    def op_exit(self):
        return -1

    opcode_handler = {
        1: op_add,
        2: op_mul,
        99: op_exit
    }

    def execute(self):
        self.ip = 0
        while True:
            opcode = self.program[self.ip]
            func = self.opcode_handler.get(opcode, lambda: "Invalid opcode")
            result = func(self)
            if result == -1:
                break
            self.ip += 4

computer = IntcodeComputer()
computer.program = [1,0,0,0,99]
computer.execute()
print("Final program state: {0}".format(computer.program))