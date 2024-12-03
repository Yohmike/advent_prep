"""
https://adventofcode.com/2024/day/3

"""

from typing import List
import re


def parse_input_and_solve(filename: str) -> int:
    mul_count = 0
    with open(filename) as file:
        corrupted_mem = "".join(file.readlines())
    m = re.findall("mul\((?P<first>\d+),(?P<second>\d+)\)", corrupted_mem)
    for pair in m:
        mul_count += int(pair[0]) * int(pair[1])
    return mul_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
