"""
https://adventofcode.com/2023/day/2

"""
from typing import Tuple

valid_game_constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def valid_game(line: str) -> Tuple[bool, int]:
    game, rounds = line.split(":")
    _, game_id = game.split()
    rounds = rounds.split(";")
    for round in rounds:
        cube_subsets = round.split(",")
        for cube_set in cube_subsets:
            number, color = cube_set.split()
            if valid_game_constraints[color] < int(number):
                return False, -1
    return True, int(game_id)




def parse_input_and_solve(filename):
    file = open(filename)
    valid_games_sum = 0
    for line in file:
        valid, game_id = valid_game(line)
        if valid:
            valid_games_sum += game_id
    return valid_games_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
