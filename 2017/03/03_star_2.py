"""
https://adventofcode.com/2017/day/3

"""

from typing import List

from dataclasses import dataclass
from collections import deque


@dataclass
class Coord:
    row: int
    col: int


def generate_empty_matrix(radius):
    matrix = [[] for i in range(radius * 2)]
    for i in range(radius * 2):
        matrix[i] = [0 for i in range(radius * 2)]
    return matrix


def fill_matrix_until(dest):
    # TODO: maybe don't make such a big matrix
    matrix = generate_empty_matrix(50)
    start = Coord(25, 25)
    matrix[start.row][start.col] = 1
    next_step = 1
    coord = start
    dir_q = deque([("R", 1), ("U", 1), ("L", 2), ("D", 2)])
    dir_count = 0
    while next_step <= dest:
        if dir_count == 0:
            dir, dir_count = dir_q.popleft()
            dir_q.append((dir, dir_count + 2))
        next_step, next_coord = fill_next_cell(matrix, coord, dir)
        coord = next_coord
        dir_count -= 1
    return next_step


def fill_next_cell(matrix, coord, dir):
    if dir == "R":
        new_coord = Coord(coord.row, coord.col + 1)
    if dir == "U":
        new_coord = Coord(coord.row - 1, coord.col)
    if dir == "L":
        new_coord = Coord(coord.row, coord.col - 1)
    if dir == "D":
        new_coord = Coord(coord.row + 1, coord.col)
    return fill_cell(matrix, new_coord), new_coord


def fill_cell(matrix, coord):
    matrix[coord.row][coord.col] = sum(
        [
            sum(matrix[coord.row - 1][coord.col - 1 : coord.col + 2]),
            sum(matrix[coord.row][coord.col - 1 : coord.col + 2]),
            sum(matrix[coord.row + 1][coord.col - 1 : coord.col + 2]),
        ]
    )
    return matrix[coord.row][coord.col]


def parse_input_and_solve(filename):

    with open(filename) as file:
        destination_square = int(file.readline())
    return fill_matrix_until(destination_square)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
