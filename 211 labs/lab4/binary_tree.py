"""
Binary Tree
"""

class Node():

    def __init__(self, node_data:int):
        self.node_data = node_data

    def sum_node_data(self):
        raise NotImplementedError("abstract!!")

    def __str__(self):
        raise NotImplementedError("blah")


class Leaf(Node):

    def __init__(self, node_data: int):
        super().__init__(node_data)

    def sum_node_data(self):
        return self.node_data

    def __str__(self):
        return f"{self.node_data}"


class Internal(Node):

    def __init__(self, node_data: int, left: Node, right: Node):
        super().__init__(node_data)
        self.left = left
        self.right = right

    def sum_node_data(self):
        return self.node_data + self.left.sum_node_data() + self.right.sum_node_data()


    def __str__(self):
        return f"<{self.node_data}, {self.left.sum_node_data()}, {self.right.__str__()}>"

def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_node_data())
    print(root)

if __name__ == '__main__':
    main()