"""
https://adventofcode.com/2017/day/3

"""

from typing import List


def get_biggest_quare_smaller_than(number: int) -> int:
    i = 1
    while i * i <= number:
        i += 2
    return i - 2


def get_corners(circle_radius):
    if circle_radius == 1:
        return [1, 1, 1, 1]
    corners = [circle_radius**2 - i * (circle_radius - 1) for i in range(0, 4)]
    sides = [
        circle_radius**2 - (circle_radius - 1) // 2 - i * (circle_radius - 1)
        for i in range(0, 4)
    ]
    return corners, sides


def manhattan_dist(dest, corners, sides, radius):
    if dest in corners:
        return radius - 1
    if dest in sides:
        return (radius - 1) // 2
    side_distance = [abs(side - dest) for side in sides]
    return min(side_distance) + (radius - 1) // 2


def parse_input_and_solve(filename):

    with open(filename) as file:
        destination_square = int(file.readline())
        square = get_biggest_quare_smaller_than(destination_square)
        if square**2 == destination_square:
            return square - 1
        elif square**2 < destination_square:
            corners, sides = get_corners(square + 2)
            dist = manhattan_dist(destination_square, corners, sides, square + 2)

    return dist


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
