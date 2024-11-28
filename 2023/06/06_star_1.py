"""
https://adventofcode.com/2023/day/6

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor
from itertools import combinations
from dataclasses import dataclass


def compute_solutions(distance, time):
    low = (time - sqrt(time**2 - 4*distance)) / 2
    high = (time + sqrt(time**2 - 4*distance)) / 2
    if low == ceil(low):
        low += 1
    if high == floor(high):
        high -= 1
    return ceil(low), floor(high)


def parse_input_and_solve(filename):
    file = open(filename)
    times = [int(x) for x in file.readline().split(":")[-1].split()]
    records = [int(x) for x in file.readline().split(":")[-1].split()]
    beats = []
    for time, record in zip(times, records):
        low, high = compute_solutions(record, time)
        beats.append(high - low + 1)

    return prod(beats)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
