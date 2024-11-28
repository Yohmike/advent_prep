"""
https://adventofcode.com/2023/day/8

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor
from itertools import combinations
from dataclasses import dataclass
from enum import Enum
import functools
from collections import deque


def get_path(line:str) -> Tuple[str, List[str]]:
    key, paths = line.split("=")
    paths = paths.split(",")
    paths = [path.strip(" ()\n") for path in paths]
    return key.strip(), paths


def parse_input_and_solve(filename):
    file = open(filename)
    directions = file.readline()
    directions = [0 if x == "L" else 1 for x in directions]
    num_dir = len(directions) - 1
    file.readline()
    paths = {}
    for line in file:
        key, path = get_path(line)
        paths[key] = path
    print(paths)
    index = 0
    instructions = deque()
    instructions.append("AAA")

    while instructions:
        instruction = instructions.popleft()
        if instruction == "ZZZ":
            break
        next_instruction = paths[instruction][directions[index % num_dir]]
        print(index, instruction, next_instruction, directions[index % num_dir])
        instructions.append(next_instruction)
        index += 1

    return index






def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
