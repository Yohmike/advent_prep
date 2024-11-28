"""
https://adventofcode.com/2023/day/8

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor, lcm
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
    original = [key for key in paths.keys() if key[-1] == "A"]
    instructions.append(original)
    zs = {i: 0 for i in range(len(original))}

    while instructions:
        instruction_list = instructions.popleft()
        #print(instruction_list)
        destinations = [instruction[-1] for instruction in instruction_list]
        #print(set(destinations), set("Z"))
        if set(destinations) == set("Z"):
            break
        if "Z" in destinations:
            #print(destinations, index)
            for i, el in enumerate(destinations):
                if el == "Z":
                    zs[i] = index
            if 0 not in zs.values():
                break
        next_instruction_list = []
        for i, instruction in enumerate(instruction_list):
            next_instruction = paths[instruction][directions[index % num_dir]]
            next_instruction_list.append(next_instruction)
            if next_instruction == original[i]:
                print(i, instruction, index)
        instructions.append(next_instruction_list)
        index += 1
        if index % 1000000 == 0:
            print(index)
            print(zs)
    result = lcm(*zs.values())
    return result


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
