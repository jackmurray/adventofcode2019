import math
import sys

inputs = []

def calc_module_fuel(module_mass):
    return math.floor(module_mass / 3) - 2

def calc_fuel_fuel(fuel_mass):
    fuel = calc_module_fuel(fuel_mass)
    if fuel < 0:
        return 0
    else:
        return fuel + calc_fuel_fuel(fuel)

def load_file(filename):
    with open(filename) as file_data:
        for line in file_data.readlines():
            inputs.append(int(line))

def calc_fuel_requirement():
    load_file("inputs/puzzle_1.txt")
    sum = 0
    for module in inputs:
        fuel = calc_module_fuel(module)
        sum += fuel
        sum += calc_fuel_fuel(fuel)
    return sum

if __name__ == "__main__":
    print(calc_fuel_requirement())
