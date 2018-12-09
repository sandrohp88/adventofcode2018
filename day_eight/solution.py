from collections import namedtuple
from collections import defaultdict
file_handler = open('input')
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
data_input = list(map(int, file_handler.read().split()))
# data_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


class Node:
    def __init__(self, n_children, n_data):
        self.data = []
        self.children = []
        self.header = (n_children, n_data)

    def add_child(self, child):
        self.children.append(child)

    def add_data(self, value):
        self.data.append(value)

    def number_of_children(self):
        return self.header[0]

    def get_sum_data(self):
        return sum(self.data)

    def __str__(self):
        node_info = f'children: {self.number_of_children()} data: {self.data} '
        return node_info


index = 0

total = 0


def part1(tree_info):
    global index
    global total
    n_children = tree_info[index]
    index += 1
    n_data = tree_info[index]
    index += 1
    node = Node(n_children, n_data)
    for _ in range(n_children):
        node.add_child(part1(tree_info))
    for _ in range(n_data):
        node.add_data(tree_info[index])
        index += 1
    total += node.get_sum_data()
    return node


def part2(children, meta):
    if not children:
        return sum(meta)
    else:
        value = 0
        for data in meta:
            if data <= len(children):
                child = children[data - 1]
                value += part2(child.children, child.data)
        return value


root = part1(data_input)
print(total)
print(part2(root.children, root.data))
