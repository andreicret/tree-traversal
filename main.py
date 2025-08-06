from tree import Tree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()


def test_find_existing_node():
    tree = Tree()
    for val in [5, 3, 7, 1, 4]:
        tree.add(val)
    node = tree.find(3)
    assert node is not None
    assert node.data == 3

def test_find_nonexistent_node():
    tree = Tree()
    for val in [5, 3, 7]:
        tree.add(val)
    node = tree.find(10)
    assert node is None
