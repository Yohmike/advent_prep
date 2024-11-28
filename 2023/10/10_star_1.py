"""
https://adventofcode.com/2023/day/10

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor, lcm
from itertools import combinations
from dataclasses import dataclass
from enum import Enum
import functools
from collections import deque


def parse_input_and_solve(filename):
    file = open(filename)
    sequences = []
    history = 0
    for line in file:
        pass


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
