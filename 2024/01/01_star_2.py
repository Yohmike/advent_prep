"""
https://adventofcode.com/2024/day/1

"""

from collections import defaultdict


def parse_input_and_solve(filename:str) -> int:
    left = []
    right = defaultdict(int)
    with open(filename) as file:
        for line in file:
            ids = line.split(" ")
            left.append(int(ids[0]))
            right[int(ids[-1])] += 1
    return sum([l * right.get(l, 0) for l in left])


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
