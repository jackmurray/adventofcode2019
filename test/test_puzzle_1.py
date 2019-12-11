import unittest
import puzzle_1.puzzle_1

class Puzzle1(unittest.TestCase):
    def test_puzzle_1(self):
        self.assertEqual(puzzle_1.puzzle_1.calc_module_fuel(12), 2)
        self.assertEqual(puzzle_1.puzzle_1.calc_module_fuel(14), 2)
        self.assertEqual(puzzle_1.puzzle_1.calc_module_fuel(1969), 654)
        self.assertEqual(puzzle_1.puzzle_1.calc_module_fuel(100756), 33583)
    
    def test_puzzle_1_output(self):
        self.assertEqual(puzzle_1.puzzle_1.calc_fuel_requirement(), 4773483)
    
    def test_puzzle_1_fuel(self):
        self.assertEqual(puzzle_1.puzzle_1.calc_fuel_fuel(654), 312)
