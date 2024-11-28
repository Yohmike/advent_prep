"""
https://adventofcode.com/2023/day/3

"""
from typing import Tuple, List
from math import prod
from dataclasses import dataclass
from collections import defaultdict

def check_symbol(symbol: str) -> int:
    #print(symbol)
    return 1 if symbol == "*" else 0


@dataclass
class Numbers:
    value: int
    x_index: int
    y_index: int
    size: int
    gear_spot: (int, int) = (0,0)

    def any_adjacent_symbols(self, schematic: List[str], debug=False) -> bool:
        result = \
            self.check_left_and_right(schematic, debug) + \
            self.check_corners(schematic, debug) + \
            self.check_top_and_bottom(schematic, debug)
        if result > 1:
            print(self)
        return result == 1

    def check_top_and_bottom(self, schematic: List[str], debug=False) -> int:
        if debug:
            print("check_top ")
        valid_symbol = 0
        if self.x_index - 1 > 0:
            symbols = [x for x in schematic[self.x_index - 1][self.y_index: self.y_index + self.size]
                       if check_symbol(x) == 1]
            if len(symbols) == 1:
                self.gear_spot = (
                    self.x_index - 1,
                    self.y_index + schematic[self.x_index - 1][self.y_index: self.y_index + self.size].index("*")
                )
                valid_symbol += 1

        if self.x_index + 1 < len(schematic):
            symbols = [x for x in schematic[self.x_index + 1][self.y_index: self.y_index + self.size]
                       if check_symbol(x) == 1]
            if debug:
                print(symbols)
            if len(symbols) == 1:
                self.gear_spot = (
                    self.x_index + 1,
                    self.y_index + schematic[self.x_index + 1][self.y_index: self.y_index + self.size].index("*")
                )
                valid_symbol += 1
        return valid_symbol

    def check_left_and_right(self, schematic: List[str], debug=False) -> int:
        valid_symbol = 0
        if self.y_index - 1 > 0:
            left = schematic[self.x_index][self.y_index - 1]
            if check_symbol(left) == 1:
                self.gear_spot = (self.x_index, self.y_index - 1)
                valid_symbol += 1
        if self.y_index + self.size < len(schematic[0]) - 1:
            right = schematic[self.x_index][self.y_index + self.size]
            if check_symbol(right) == 1:
                self.gear_spot = (self.x_index, self.y_index + self.size)
                valid_symbol += 1
        return valid_symbol

    def check_corners(self, schematic: List[str], debug=False) -> int:
        if debug:
            print("check corners")
        valid_symbol = 0
        if self.x_index - 1 > 0 and self.y_index - 1 > 0:
            symbol = schematic[self.x_index - 1][self.y_index - 1]
            if check_symbol(symbol) == 1:
                self.gear_spot = (self.x_index - 1,self.y_index - 1)
                valid_symbol += 1
        if self.x_index - 1 > 0 and self.y_index + self.size < len(schematic[0]) - 1:
            symbol = schematic[self.x_index - 1][self.y_index + self.size]
            if check_symbol(symbol) == 1:
                self.gear_spot = (self.x_index - 1, self.y_index + self.size)
                valid_symbol += 1
        if self.x_index + 1 < len(schematic) and self.y_index - 1 > 0:
            symbol = schematic[self.x_index + 1][self.y_index - 1]
            if check_symbol(symbol) == 1:
                self.gear_spot = (self.x_index + 1, self.y_index - 1)
                valid_symbol += 1
        if self.x_index + 1 < len(schematic) and self.y_index + self.size < len(schematic[0]) - 1:
            symbol = schematic[self.x_index + 1][self.y_index + self.size]
            if check_symbol(symbol) == 1:
                self.gear_spot = (self.x_index + 1, self.y_index + self.size)
                valid_symbol += 1
        if debug:
            print(self.value, valid_symbol)
        return valid_symbol


def find_numbers(line: str, line_index: int) -> List[Numbers]:
    number_started = False
    number = ""
    numbers = []
    index = 0
    for i, char in enumerate(line):
        if char.isdigit():
            if not number_started:
                number_started = True
                number = char
                index = i
            else:
                number += char
        if not char.isdigit():
            if number_started:
                number_started = False
                save_number = Numbers(int(number), line_index, index, len(number), (0, 0))
                numbers.append(save_number)

    return numbers


def parse_input_and_solve(filename):
    file = open(filename)
    numbers = []
    game_sum = 0
    schematic = []
    gears = defaultdict(list)
    for i, line in enumerate(file):
        schematic.append(line)
        numbers.extend(find_numbers(line, i))
    #print(numbers)
    debug = False
    for number in numbers:
        if number.any_adjacent_symbols(schematic, debug):
            print("Adding this one", number)
            gears[number.gear_spot].append(number.value)
    print(gears)
    for valid_numbers in gears.values():
        if len(valid_numbers) == 2:
            game_sum += valid_numbers[0] * valid_numbers[1]
    return game_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
