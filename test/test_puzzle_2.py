import unittest
from puzzle_2 import IntcodeComputer

class Puzzle2(unittest.TestCase):
    def test_puzzle_2(self):
        computer = IntcodeComputer()
        computer.program = [1,0,0,0,99]
        computer.execute()
        self.assertEqual(computer.program, [2,0,0,0,99])

        computer.program = [2,3,0,3,99]
        computer.execute()
        self.assertEqual(computer.program, [2,3,0,6,99])
        
        computer.program = [2,4,4,5,99,0]  
        computer.execute()
        self.assertEqual(computer.program, [2,4,4,5,99,9801])

        computer.program = [1,1,1,4,99,5,6,0,99]
        computer.execute()
        self.assertEqual(computer.program, [30,1,1,4,2,5,6,0,99])