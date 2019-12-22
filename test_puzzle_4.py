import unittest
from puzzle_4 import *

class Puzzle4(unittest.TestCase):
    def test_addition(self):
        c = Code("100")
        c += 1
        self.assertEqual([1,0,1], c.digits)

    def test_never_decrease(self):
        c = Code("654321")
        self.assertFalse(c.is_valid())

    def test_sample_inputs(self):
        self.assertTrue(Code("111111").is_valid())
        self.assertFalse(Code("223450").is_valid())
        self.assertFalse(Code("123789").is_valid())

if __name__ == "__main__":
    tester = Puzzle4()
    tester.test_addition()
    tester.test_never_decrease()
    tester.test_sample_inputs()