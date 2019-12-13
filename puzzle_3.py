from collections import defaultdict

class Wire:
    path = []
    head = {"x": 0, "y": 0}

    def __init__(self, pathstring):
        self.path = pathstring.split(",")

class WireGrid:
    visit_list = defaultdict(lambda: defaultdict(int))

    def add_wire(self, wire: Wire):
        for move in wire.path:
            direction = move[0]
            distance = int(move[1:])

            if direction == 'U':
                wire.head['y'] += distance
            if direction == 'D':
                wire.head['y'] -= distance
            if direction == 'L':
                wire.head['x'] -= distance
            if direction == 'R':
                wire.head['x'] += distance
            
            self.visit_list[wire.head['x']][wire.head['y']] += 1

if __name__ == "__main__":
    grid = WireGrid()
    wire = Wire("R15,U10")

    grid.add_wire(wire)
            
