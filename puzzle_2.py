class IntcodeComputer:
    program = []
    ip = 0

    def load_file(self, filename):
        with open(filename) as file_data:
            self.program = list(map(int, file_data.readline().split(','))) # Read data and convert each element to an int.

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
            func = self.opcode_handler.get(int(opcode), lambda self: print("Unknown opcode {0}".format(opcode)))
            result = func(self)
            if result == -1:
                break
            self.ip += 4


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