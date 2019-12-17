from collections import defaultdict

class Wire:
    def __init__(self, pathstring):
        self.path = pathstring.split(",")
        self.head = {"x": 0, "y": 0}
        self.length = 0
    
    def update_len(self, direction):
        self.length += 1 # Update the wire's current length to account for the location we're about to enter.

        if direction == "U":
            self.head['y'] += 1
        if direction == "D":
            self.head['y'] -= 1
        if direction == "L":
            self.head['x'] -= 1
        if direction == "R":
            self.head['x'] += 1

class GridSquare:
    def __init__(self):
        self.wire_flags = 0
        self.wire_len_when_visited = {}

class WireGrid:

    def __init__(self):
        self.visit_list = defaultdict(lambda: defaultdict(GridSquare))
        self.wire_flag = 1 # Bit that indicates which wire we're adding

    def add_wire(self, wire: Wire):
        for move in wire.path:
            direction = move[0]
            distance = int(move[1:])

            for i in range(1, distance + 1):
                wire.update_len(direction)
                gridsquare = self.visit_list[wire.head['x']][wire.head['y']]
                gridsquare.wire_flags |= self.wire_flag
                if self.wire_flag not in gridsquare.wire_len_when_visited.keys(): # Only the first visit counts
                    gridsquare.wire_len_when_visited[self.wire_flag] = wire.length
            
        self.wire_flag <<= 1
            
    
    def get_intersections(self):
        # An intersection is any position on the grid with flags for wires 1 and 2 set.
        for x in self.visit_list.keys():
            for y in self.visit_list[x].keys():
                if self.visit_list[x][y].wire_flags == 3: # Wires 1 and 2
                    yield self.visit_list[x][y]

    def get_shortest_intersection(self):
        intersections = self.get_intersections()
        shortest = 0
        for i in intersections:
            length = i.wire_len_when_visited[1] + i.wire_len_when_visited[2]
            if shortest == 0 or length < shortest:
                shortest = length
        return shortest


if __name__ == "__main__":
    grid = WireGrid()
    with open("inputs/puzzle_3.txt") as file_data:
        for line in file_data.readlines():
            wire = Wire(line)
            grid.add_wire(wire)

    print(grid.get_shortest_intersection())
