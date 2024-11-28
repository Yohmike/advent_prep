"""
https://adventofcode.com/2023/day/9

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor, lcm
from itertools import combinations
from dataclasses import dataclass
from enum import Enum
import functools
from collections import deque


def get_diffs(sequence: List[int]) -> List[List[int]]:
    diffs = []
    while sum(sequence) != 0:
        diffs.append(sequence)
        sequence = [sequence[i+1] - x for i, x in enumerate(sequence[:-1])]

    print(sequence, diffs)
    return diffs


def extrapolate_next(diffs: List[List[int]]) -> int:
    y = 0
    for x in diffs[::-1]:
        y = x[0] - y
    return y


def parse_input_and_solve(filename):
    file = open(filename)
    sequences = []
    history = 0
    for line in file:
        sequence = [int(x) for x in line.split()]
        sequences.append(sequence)
        print(sequence)
        sequence_val = extrapolate_next(get_diffs(sequence))
        print(sequence_val)
        history += sequence_val

    print(history)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
