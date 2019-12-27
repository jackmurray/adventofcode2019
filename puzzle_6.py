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

    def search(self, nodename: str) -> anytree.Node:
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

    def calc_path(self, fromname, toname):
        fromnode = self.search(fromname)
        tonode = self.search(toname)

        # To find the path first we find the last node (one with longest path to the root) that is an ancestor of both nodes
        from_path_nodes = list(fromnode.iter_path_reverse())
        common_ancestor = None
        for n in tonode.iter_path_reverse():
            if n in from_path_nodes: # The first match we get is the one we want, since we're up the tree of parents.
                common_ancestor = n
                break
        if common_ancestor == None:
            raise Exception("No common ancestor found.")
        
        len_from_fromnode = fromnode.depth - common_ancestor.depth
        len_from_tonode = tonode.depth - common_ancestor.depth
        return len_from_fromnode + len_from_tonode

if __name__ == "__main__":
    o = OrbitMap()
    with open("inputs/puzzle_6.txt") as file_data:
        for orbit in file_data.readlines():
            o.add(orbit)

    print(o.count_all_orbits())
    print(o.calc_path(o.search("SAN").parent.name, o.search("YOU").parent.name))