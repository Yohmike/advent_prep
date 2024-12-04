"""
https://adventofcode.com/2024/day/4

"""

from typing import List
import re


def look_diagonally_for(matrix, row, col, letter):
    found = []
    if row - 1 >= 0:
        if col - 1 >= 0:
            if matrix[row - 1][col - 1] == letter:
                found.append([-1, -1, letter])
            if matrix[row - 1][col + 1] == letter:
                found.append([-1, +1, letter])

    if row + 1 < len(matrix):
        if col - 1 >= 0:
            if matrix[row + 1][col - 1] == letter:
                found.append([+1, -1, letter])
        if col + 1 < len(matrix[0]):
            if matrix[row + 1][col + 1] == letter:
                found.append([+1, +1, letter])
    return found


def is_letter_in_direction(matrix, row, col, row_index, col_index, letter):
    if 0 <= row + row_index < len(matrix):
        if 0 <= col + col_index < len(matrix[0]):
            return matrix[row + row_index][col + col_index] == letter
    return False


def parse_input_and_solve(filename: str) -> int:
    xmas_count = 0
    with open(filename) as file:
        xmas_puzzle = file.readlines()

    for row in range(len(xmas_puzzle)):
        for col in range(len(xmas_puzzle[0])):
            if xmas_puzzle[row][col] == "A":
                m_spots = look_diagonally_for(xmas_puzzle, row, col, "M")
                s_spots = 0
                if len(m_spots) == 2:
                    for spot in m_spots:
                        m_row, m_col, _ = spot
                        if is_letter_in_direction(
                            xmas_puzzle, row, col, m_row * -1, m_col * -1, "S"
                        ):
                            s_spots += 1
                if s_spots == 2:
                    xmas_count += 1
    return xmas_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
