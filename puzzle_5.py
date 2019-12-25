class IntcodeComputer:
    program = []
    ip = 0

    def load_file(self, filename):
        with open(filename) as file_data:
            self.program = list(map(int, file_data.readline().split(','))) # Read data and convert each element to an int.

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

    def execute(self):
        self.ip = 0
        while True:
            opcode = self.program[self.ip]
            func = self.opcode_handler.get(int(opcode), lambda self: print("Unknown opcode {0}".format(opcode)))['func']
            result = func(self)
            if result == -1:
                break


def bruteforce_output(computer, desired_output):
    for i in range(0, 99):
        for j in range(0, 99):
            computer.load_file("inputs/puzzle_2.txt")
            computer.program[1] = i
            computer.program[2] = j
            computer.execute()
            if computer.program[0] == desired_output:
                print("Solution found for i, j = {0}, {1}".format(i, j))
                return
    raise "No solution found"

if __name__ == "__main__":
    computer = IntcodeComputer()
    computer.load_file("inputs/puzzle_2.txt")
    computer.execute()
    print("Final program state: {0}".format(computer.program))