"""
https://adventofcode.com/2024/day/14

"""

from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Coord(self.row - other.row, self.col - other.col)

    def __mul__(self, other):
        return Coord(self.row * other.row, self.col * other.col)


def parse_line(line):
    pos_string, vel_string = line.split(" ")
    pos_x, pos_y = pos_string[2:].split(",")
    vel_x, vel_y = vel_string[2:].split(",")
    return Coord(int(pos_x), int(pos_y)), Coord(int(vel_x), int(vel_y))


def move_robots(grid, steps, robots):
    moved_robots = []
    for robot in robots:
        robot_pos, robot_vel = robot
        moved = robot_pos + (grid + robot_vel) * Coord(steps, steps)
        moved_coord = Coord(moved.row % grid.row, moved.col % grid.col)
        moved_robots.append(moved_coord)

    return moved_robots


def count_robots(grid, robots):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot.row < grid.row // 2:
            if robot.col < grid.col // 2:
                quadrants[0] += 1
            elif robot.col >= grid.col // 2 + 1:
                quadrants[2] += 1
        if robot.row >= grid.row // 2 + 1:
            if robot.col < grid.col // 2:
                quadrants[1] += 1
            elif robot.col >= grid.col // 2 + 1:
                quadrants[3] += 1
    return quadrants


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        robots = []
        for line in lines:
            pos, vel = parse_line(line.strip("\n"))
            robots.append((pos, vel))
    print(robots)

    grid = Coord(101, 103)
    steps = 100

    future_robots = move_robots(grid, steps, robots)
    robots_in_quadrants = count_robots(grid, future_robots)

    return reduce(mul, robots_in_quadrants)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
