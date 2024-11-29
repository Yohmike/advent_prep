"""
https://adventofcode.com/2017/day/2

"""

from typing import List


def get_divizor(elements: List[int]) -> int:
    for el in elements:
        for el2 in elements:
            if el != el2:
                if el % el2 == 0:
                    return el // el2
                if el2 % el == 0:
                    return el2 // el


def parse_input_and_solve(filename):

    with open(filename) as file:
        spreadsheet_matrix = []
        for line in file:
            row = [int(x) for x in line.split("\t")]
            spreadsheet_matrix.append(row)

    spreadsheet_checksum = sum([get_divizor(row) for row in spreadsheet_matrix])

    return spreadsheet_checksum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
