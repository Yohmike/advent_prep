"""
https://adventofcode.com/2024/day/14

"""

from dataclasses import dataclass

from time import sleep


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
        moved = robot_pos + robot_vel * Coord(steps, steps)
        moved_coord = Coord(moved.row % grid.row, moved.col % grid.col)
        moved_robots.append((moved_coord, robot_vel))

    return moved_robots


def print_robots(robots, grid):
    orig = [["." for _ in range(grid.col)] for _ in range(grid.row)]
    for robot_pv in robots:
        robot, _ = robot_pv
        orig[robot.row][robot.col] = "*"
    with open("../output", "w") as file:
        for row in orig:
            file.write("".join(row) + "\n")


def clumped(robots, grid):
    orig = [["." for _ in range(grid.col)] for _ in range(grid.row)]
    for robot_pv in robots:
        robot, _ = robot_pv
        if orig[robot.row][robot.col] == "*":
            return False
        else:
            orig[robot.row][robot.col] = "*"
    return True


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        robots = []
        for line in lines:
            pos, vel = parse_line(line.strip("\n"))
            robots.append((pos, vel))

    grid = Coord(101, 103)
    steps = 0
    future_robots = robots
    i = 0
    while True:
        future_robots = move_robots(grid, 1, future_robots)
        if clumped(future_robots, grid):
            print_robots(future_robots, grid)
            return i + 1

        i += 1
    return 0


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
