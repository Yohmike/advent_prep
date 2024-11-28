import pprint
from collections import deque


class Node(object):
    def __init__(self, parent_value=None):
        self._value = parent_value
        self._parent = None
        self._children = []

    @property
    def get_node_value(self):
        return self._value

    @property
    def get_children(self):
        return self._children

    @property
    def get_parent(self):
        return self._parent

    def add_children(self, children):
        self._children.append(children)

    def add_parent(self, parent):
        self._parent = parent
        return self

    def __repr__(self):
        return f"Node -{self._value}- with children {[child for child in self._children]}"


def make_node(current_bag, children_bags):
    bag_node = Node(current_bag)
    for child in children_bags:
        child_bag = Node(child)
        child_bag.add_parent(bag_node)
        bag_node.add_children(child_bag)
    # pprint.pprint(bag_node)
    return bag_node


def find_bag(head_node, node):
    queue_to_check = head_node
    if not head_node.get_children and head_node.get_node_value != node.get_node_value:
        return False, head_node
    else:
        for child in head_node.get_children:
            if child.get_node_value == node.get_node_value:
                return True, child
            else:
                find_bag(child, node)


def add_in_tree(head_node, node):
    additions = 0
    queue = deque()
    queue.append(head_node)
    while queue:
        # print(queue)
        elem = queue.popleft()
        if elem.get_node_value == node.get_node_value:
            # pprint.pprint(f"add {node} to  {elem}")
            # pprint.pprint(f"head noe: {head_node}")
            node.add_parent(elem)
            elem.add_children(node)
            additions += 1
        else:
            # print(f"Moving on , queue size {len(queue)}")
            for child in elem.get_children:
                if child not in queue:
                    queue.append(child)
            # print(f"after: {len(queue)}")
    if additions == 0:
        # print(f"Head children {node}")
        node.add_parent(head_node)
        head_node.add_children(node)


def find_bag(bag_name, head_node):
    queue = deque()
    queue.append(head_node)
    nodes = []
    while queue:
        elem = queue.popleft()
        if elem.get_node_value == bag_name:
            nodes.append(elem)
        else:
            for child in elem.get_children:
                if child not in queue:
                    queue.append(child)
    return nodes


def get_to_head(node):
    to_head = []
    while node.get_parent:
        node = node.get_parent
        to_head.append(node.get_node_value)
    return to_head


def process_line(line):
    bits = line.split(" ")
    parent_node_name = ""
    children_node_name = ""
    children_node_names = []
    parent_done = False
    new_kid = False
    for bit in bits:
        if bit == "bags":
            continue
        elif bit == "bag," or bit == "bags," or bit == "bags.\n" or bit == "bag.\n":
            new_kid = True
            if children_node_name != "no other ":
                children_node_names.append(children_node_name[:-1])
            children_node_name = ""
        elif bit == "contain":
            parent_done = True
            parent_node_name = parent_node_name[:-1]
        else:
            if not parent_done:
                parent_node_name += bit + " "
            else:
                if len(bit) > 1:
                    # skip numbers we don't need them now
                    children_node_name += bit + " "

    return parent_node_name, children_node_names


def parse_input_first_star(filename):
    file = open(filename)
    bag_tree = Node()
    for line in file:
        node_components = process_line(line)
        bag, children_bags = node_components
        bag_node = make_node(bag, children_bags)
        add_in_tree(bag_tree, bag_node)
    number_of_bags = find_bag("shiny gold", bag_tree)
    number_of_distinct_bags = [set(get_to_head(bag)) for bag in number_of_bags]
    print(number_of_distinct_bags)
    return number_of_bags


def main():
    input_file_name = "small input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
