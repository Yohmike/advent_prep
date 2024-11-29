import re
from collections import namedtuple
from functools import reduce
import operator
def trees_hit(slope_map, down, right):
    trees_hit_number = 0
    tree = '#'
    map_size = len(slope_map)
    map_width = len(slope_map[0])
    current_position_right = 0
    for i in range(1, map_size + 1, down):
        position_in_map = current_position_right % map_width
        if slope_map[i - 1][position_in_map] == tree:
            trees_hit_number += 1
        current_position_right += right
    return trees_hit_number


def parse_input_first_star(filename):
    file = open(filename)
    trees_hit_list = []
    map = file.readlines()
    map = [x.strip("\n") for x in map]
    # print(map)
    print(len(map))
    SlopePattern = namedtuple("SlopePattern", ["right", "down"])
    patterns = [
        SlopePattern(1, 1),
        SlopePattern(3, 1),
        SlopePattern(5, 1),
        SlopePattern(7, 1),
        SlopePattern(1, 2)
    ]
    for pattern in patterns:
        trees_hit_list.append(trees_hit(map, pattern.down, pattern.right))

    print(trees_hit_list)
    multiplier_trees = reduce(operator.mul, trees_hit_list, 1)
    return multiplier_trees


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()