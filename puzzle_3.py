from collections import defaultdict

class Wire:
    def __init__(self, pathstring):
        self.path = pathstring.split(",")
        self.head = {"x": 0, "y": 0}

class WireGrid:

    def __init__(self):
        self.visit_list = defaultdict(lambda: defaultdict(int))
        self.wire_flag = 1 # Bit that indicates which wire we're adding

    def add_wire(self, wire: Wire):
        for move in wire.path:
            direction = move[0]
            distance = int(move[1:])

            if direction == 'U':
                for i in range(1, distance + 1):
                    self.visit_list[wire.head['x']][wire.head['y'] + i] |= self.wire_flag
                wire.head['y'] += distance
            if direction == 'D':
                for i in range(1, distance + 1):
                    self.visit_list[wire.head['x']][wire.head['y'] - i] |= self.wire_flag
                wire.head['y'] -= distance
            if direction == 'L':
                for i in range(1, distance + 1):
                    self.visit_list[wire.head['x'] - i][wire.head['y']] |= self.wire_flag
                wire.head['x'] -= distance
            if direction == 'R':
                for i in range(1, distance + 1):
                    self.visit_list[wire.head['x'] + i][wire.head['y']] |= self.wire_flag
                wire.head['x'] += distance
        self.wire_flag <<= 1
            
    
    def get_intersections(self):
        # An intersection is any position on the grid with flags for wires 1 and 2 set.
        for x in self.visit_list.keys():
            for y in self.visit_list[x].keys():
                if self.visit_list[x][y] == 3: # Wires 1 and 2
                    yield x, y

    def get_shortest_intersection(self):
        intersections = self.get_intersections()
        shortest = 0
        for i in intersections:
            length = i[0] + i[1]
            if shortest == 0 or length < shortest:
                shortest = length
        return shortest


if __name__ == "__main__":
    grid = WireGrid()
    #with open("inputs/puzzle_3.txt") as file_data:
    #    for line in file_data.readlines():
    #        wire = Wire(line)
    #        grid.add_wire(wire)

    w1 = Wire("R8,U5,L5,D3")
    w2 = Wire("U7,R6,D4,L4")
    grid.add_wire(w1)
    grid.add_wire(w2)
    print(grid.get_shortest_intersection())