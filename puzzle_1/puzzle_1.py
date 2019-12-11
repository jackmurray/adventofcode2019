import math
import sys

inputs = []

def calc_module_fuel(module_mass):
    return math.floor(module_mass / 3) - 2

def load_file(filename):
    with open(filename) as file_data:
        for line in file_data.readlines():
            inputs.append(int(line))

if __name__ == "__main__":
    load_file("inputs/puzzle_1.txt")
    sum = 0
    for module in inputs:
        sum += calc_module_fuel(module)
    print(sum)
