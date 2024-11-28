"""
https://adventofcode.com/2023/day/2

"""
from typing import Tuple
from math import prod

def valid_game(line: str) ->int:
    game, rounds = line.split(":")
    minimum_game_constraints = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    _, game_id = game.split()
    rounds = rounds.split(";")
    for game_round in rounds:
        cube_subsets = game_round.split(",")
        for cube_set in cube_subsets:
            number, color = cube_set.split()
            if minimum_game_constraints[color] < int(number):
                minimum_game_constraints[color] = int(number)

    power = prod(minimum_game_constraints.values())
    return power


def parse_input_and_solve(filename):
    file = open(filename)
    valid_games_sum = 0
    for line in file:
        valid_games_sum += valid_game(line)
    return valid_games_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
