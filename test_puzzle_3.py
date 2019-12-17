import unittest
from puzzle_3 import *

class Puzzle3(unittest.TestCase):
    def test_puzzle_3(self):
        grid = WireGrid()
        w1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        w2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")
        grid.add_wire(w1)
        grid.add_wire(w2)
        self.assertEqual(grid.get_shortest_intersection(), 610)

    def test_puzzle_3_input2(self):
        grid = WireGrid()
        w1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        w2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        grid.add_wire(w1)
        grid.add_wire(w2)
        self.assertEqual(grid.get_shortest_intersection(), 410)
    
    def test_puzzle_3_input3(self):
        grid = WireGrid()
        w1 = Wire("R8,U5,L5,D3")
        w2 = Wire("U7,R6,D4,L4")
        grid.add_wire(w1)
        grid.add_wire(w2)
        self.assertEqual(grid.get_shortest_intersection(), 30)