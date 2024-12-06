"""
https://adventofcode.com/2024/day/6

"""

from dataclasses import dataclass


@dataclass
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Coord(self.row - other.row, self.col - other.col)


def is_inside(maze, coord):
    return 0 <= coord.row < len(maze) and 0 <= coord.col < len(maze[0])


def move_until_obstacle(maze, coord, direction):
    steps = 0
    while maze[coord.row][coord.col] != "#":
        maze[coord.row][coord.col] = "X"

        steps += 1
        coord += direction
        if not is_inside(maze, coord):
            return steps, Coord(-1, -1)
    return steps, coord - direction


def get_position(maze, symbol):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == symbol:
                return Coord(i, j)


def change_dir(direction):
    if direction == Coord(-1, 0):
        return Coord(0, 1)
    if direction == Coord(0, 1):
        return Coord(1, 0)
    if direction == Coord(1, 0):
        return Coord(0, -1)
    if direction == Coord(0, -1):
        return Coord(-1, 0)


def traverse(maze, start):
    steps = 0
    direction = Coord(-1, 0)
    dir_steps, new_pos = move_until_obstacle(maze, start, direction)
    print(dir_steps, new_pos)
    while new_pos != Coord(-1, -1):
        steps += dir_steps
        direction = change_dir(direction)
        dir_steps, new_pos = move_until_obstacle(maze, new_pos, direction)
    return steps


def count_symbol(maze, symbol):
    count = 0
    for i in range(len(maze)):
        count += maze[i].count(symbol)
    return count


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    maze = []
    with open(filename) as file:
        for line in file:
            maze.append(list(line.strip("\n")))
    # print(maze)
    start = get_position(maze, "^")
    # print(start)
    steps = traverse(maze, start)
    print(steps)
    update_count = count_symbol(maze, "X")
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
