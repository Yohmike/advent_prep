"""
https://adventofcode.com/2024/day/3

"""

from typing import List
import re


def parse_input_and_solve(filename: str) -> int:
    mul_count = 0
    do = True
    with open(filename) as file:
        corrupted_mem = "".join(file.readlines())
    m = re.findall("do\(\)|mul\(\d+,\d+\)|don't\(\)", corrupted_mem)
    for el in m:
        if el[:3] == "do(":
            do = True
        elif el[:3] == "don":
            do = False
        elif el[:3] == "mul":
            if do:
                m2 = re.match("mul\((?P<first>\d+),(?P<second>\d+)\)", el)
                mul_count += int(m2.group(1)) * int(m2.group(2))

    return mul_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
