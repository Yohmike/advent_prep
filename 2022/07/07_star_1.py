"""
https://adventofcode.com/2022/day/7

"""
from enum import Enum

class FileType(Enum):
    DIR = 1
    FILE = 2

class File(object):

    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0
        self.type = FileType.DIR

    @classmethod
    def update_size(self, node):
        if node.type == FileType.FILE:
            while(node.parent is not None):
                node.parent.size += node.size
                node = node.parent
        elif node.type == FileType.DIR:
            for node in node.children:
                self.update_size(node)

    @classmethod
    def traverse_size(self, node, threshold, sum):
        # print(node.name, "traverse")
        if node.type == FileType.FILE:
            return 0
        if node.type == FileType.DIR:
            for child in node.children:
                if child.type == FileType.DIR:
                    sum += self.traverse_size(child, threshold, 0)
                    # print(sum, node.name)
            if node.size <= threshold:
                sum += node.size
                # print("curent node", sum, node.name)
        return sum

    @classmethod
    def get_root(self, node):
        while node.parent is not None:
            node = node.parent
        return node

    def __str__(self, level=0):
        if self.type == FileType.FILE:
            ret = "\t"*level + f"File: {self.name}, {self.size}\n"
        if self.type == FileType.DIR:
            ret = "\t"*level + f"Dir: {self.name}, {self.size}\n"
            for child in self.children:
                ret += child.__str__(level=level + 1)
        return ret

def parse_ls_command(arguments, dir_node):
    """
    :param arguments: list of command results (after a "ls" command)
    :param dir_node: node to the current directory before ls command
    :return: Nothing, filesystem_tree will be updated
    """
    # print("LS", arguments, dir_node.name)
    for argument in arguments:
        node = File(argument[1], dir_node)
        if argument[0] == "dir":
            node.type = FileType.DIR
        else:
            size = int(argument[0])
            node.size = size
            node.type = FileType.FILE
        dir_node.children.append(node)

def parse_cd_command(argument, dir_node):
    """

    :param argument: current target dir for "cd"
    :param dir_node: position in the filesystem node from before the command
    :return:
    """
    # print("CD", argument, dir_node.name)
    if argument == "..":
        dir_node = dir_node.parent
    else:
        for child in dir_node.children:
            if child.name == argument:
                dir_node = child
    return dir_node


def parse_input_and_solve(filename):
    file = open(filename)
    total_score = 0
    compartments = []
    root = None
    ls_results = []
    is_ls = False
    for i, line in enumerate(file, start=1):
        bits = line.strip("\n").split(" ")
        if bits[0] == "$":
            if bits[1] == "cd":
                if is_ls:
                    parse_ls_command(ls_results, root)
                    is_ls = False
                if bits[2] == "/":
                    root = File("/", None)
                    ## print("ROOT", root.name, root.children)
                else:
                    root = parse_cd_command(bits[2], root)
                    # print(root.name)
            elif bits[1] == "ls":
                is_ls = True
                ls_results = []
        else:
            ls_results.append(bits)
    if is_ls:
        parse_ls_command(ls_results, root)
        is_ls = False
    root = File.get_root(root)
    File.update_size(root)
    threshold = 100000
    dir_sum = 0
    dir_sum = File.traverse_size(root,threshold, dir_sum)
    # print("Result: ", dir_sum)
    # print(root.name)
    print(root)
    # print(root.children)
    return dir_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
