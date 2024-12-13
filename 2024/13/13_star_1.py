"""
https://adventofcode.com/2024/day/12

"""

import re
from dataclasses import dataclass


@dataclass
class Button:
    name: str
    x: int
    y: int


@dataclass
class Prize:
    x: int
    y: int


def get_button(line):
    parts = line.split(" ")
    name = parts[1][0]
    x = int(parts[2][:-1].split("+")[-1])
    y = int(parts[3][:-1].split("+")[-1])
    return Button(name, x, y)


def get_prize(line):
    parts = line.strip("\n").split(" ")
    x = int(parts[1][:-1].split("=")[-1])
    y = int(parts[2].split("=")[-1])
    return Prize(x, y)


def solve_equation(button_a, button_b, prize):
    b_times = (prize.x * button_a.y - prize.y * button_a.x) / (
        button_b.x * button_a.y - button_b.y * button_a.x
    )
    a_times = (prize.x - b_times * button_b.x) / button_a.x
    if int(a_times) == a_times and int(b_times) == b_times:
        if a_times > 100 and b_times > 100:
            print("high numbers", a_times, b_times)
            return 0, 0
        return a_times, b_times
    return 0, 0


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    prize_entries = []
    for i in range(0, len(lines), 4):
        button_a = get_button(lines[i])
        button_b = get_button(lines[i + 1])
        prize = get_prize(lines[i + 2])
        prize_entries.append((button_a, button_b, prize))
    tokens = 0
    for entry in prize_entries:
        a_pushes, b_pushes = solve_equation(*entry)
        tokens += a_pushes * 3 + b_pushes
    return int(tokens)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
