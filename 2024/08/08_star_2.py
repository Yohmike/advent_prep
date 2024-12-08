"""
https://adventofcode.com/2024/day/8

"""

from collections import defaultdict
from itertools import combinations


def inbounds(row, col, node):
    return 0 <= node[0] < row and 0 <= node[1] < col


def get_antinodes(row, col, nodes):
    pairs = list(combinations(nodes, 2))
    antinodes = []
    pairs_turned_antinodes = []
    for pair in pairs:
        left, right = pair
        diff_x = left[0] - right[0]
        diff_y = left[1] - right[1]
        left_antinodes = []
        right_antinodes = []
        left_antinode = (left[0] + diff_x, left[1] + diff_y)
        while inbounds(row, col, left_antinode):
            left_antinodes.append(left_antinode)
            left_antinode = (left_antinode[0] + diff_x, left_antinode[1] + diff_y)
        right_antinode = (right[0] - diff_x, right[1] - diff_y)
        while inbounds(row, col, right_antinode):
            right_antinodes.append(right_antinode)
            right_antinode = (right_antinode[0] - diff_x, right_antinode[1] - diff_y)
        if len(left_antinode) >= 2 or len(right_antinode) >= 2:
            if left not in pairs_turned_antinodes:
                pairs_turned_antinodes.append(left)
            if right not in pairs_turned_antinodes:
                pairs_turned_antinodes.append(right)
        antinodes += left_antinodes + right_antinodes
    antinodes += pairs_turned_antinodes
    return antinodes


def parse_input_and_solve(filename: str) -> int:
    frequency_locations = defaultdict(list)
    row = 0
    col = 0
    with open(filename) as file:
        for i, line in enumerate(file):
            row += 1
            for j, el in enumerate(line.strip("\n")):
                if el != ".":
                    frequency_locations[el].append((i, j))
        col = len(line)
    antinodes = []
    for key in frequency_locations.keys():
        new_antinodes = get_antinodes(row, col, frequency_locations[key])
        for new_antinode in new_antinodes:
            if new_antinode not in antinodes:
                antinodes.append(new_antinode)
    return len(antinodes)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
