import anytree
import anytree.search

class OrbitMap:
    def __init__(self):
        self.orbit_list = []

    def add(self, orbitspec: str):
        s = orbitspec.split(")")
        parent = s[0].strip()
        child = s[1].strip()

        # create nodes for the parent and child if they don't exist already
        parent_node = self.search(parent)
        if not parent_node:
            parent_node = self.create_node(parent)

        child_node = self.search(child)
        if not child_node:
            child_node = self.create_node(child)
        
        child_node.parent = parent_node # and record the parent/child relationship

    def create_node(self, nodename: str):
        node = anytree.Node(nodename)
        self.orbit_list.append(node)
        return node

    def search(self, nodename: str):
        for node in self.orbit_list:
            if node.name == nodename:
                return node
        return None

    def count_all_orbits(self):
        sum = 0
        for n in self.orbit_list:
            sum += n.depth

        return sum

    def load_file(self, filename):
        with open(filename) as file_data:
            for orbit in file_data.readlines():
                self.add(orbit)

if __name__ == "__main__":
    o = OrbitMap()
    with open("inputs/puzzle_6.txt") as file_data:
        for orbit in file_data.readlines():
            o.add(orbit)

    print(o.count_all_orbits())