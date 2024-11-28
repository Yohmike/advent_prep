"""
https://adventofcode.com/2022/day/14

"""
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Direction:
    start: Point
    stop: Point


def sign(x):
    return x//abs(x)


def get_boundaries(wall: List[List[int]]) -> (Point,Point):
    min_x = 1000
    max_x = 0
    min_y = 1000
    max_y = 0
    for i, row in enumerate(wall):
        for j, el in enumerate(row):
            if el != 0:
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)
    top_left = Point(min_x, min_y)
    bottom_right = Point(max_x, max_y)
    return top_left, bottom_right


def print_wall(wall):
    top_left, bottom_right = get_boundaries(wall)
    for i in range(top_left.x - 1, bottom_right.x + 1):
        print(wall[i][top_left.y - 1:bottom_right.y + 1])
    print(top_left.x - 1, bottom_right.x)
    print(top_left.y - 1, bottom_right.y)


def process_path(wall: List[List[int]], directions: List[Direction]):
    for direction in directions:
        if direction.start.x == direction.stop.x:
            x = direction.start.x
            direction_sign = sign(direction.stop.y - direction.start.y)
            for i in range(direction.start.y, direction.stop.y + direction_sign, direction_sign):
                wall[i][x] = 1
        if direction.start.y == direction.stop.y:
            y = direction.start.y
            direction_sign = sign(direction.stop.x - direction.start.x)
            for i in range(direction.start.x, direction.stop.x + direction_sign, direction_sign):
                wall[y][i] = 1


def get_direction_from_string(directions_str: str) -> List[Direction]:
    directions = []
    directions_set = directions_str.split(" -> ")
    prev_direction = directions_set[0]
    for direction in directions_set[1:]:
        new_start_direction = Point(*[int(x) for x in prev_direction.split(",")])
        new_end_direction = Point(*[int(x) for x in direction.split(",")])
        new_direction = Direction(new_start_direction, new_end_direction)
        directions.append(new_direction)
        prev_direction = direction
    return directions


def update_move(sand: Point, wall: List[List[int]]) -> Point:
    if wall[sand.x + 1][sand.y] == 0:
        return Point(sand.x + 1, sand.y)
    elif wall[sand.x + 1][sand.y - 1] == 0:
        return Point(sand.x + 1, sand.y - 1)
    elif wall[sand.x + 1][sand.y + 1] == 0:
        return Point(sand.x + 1, sand.y + 1)
    else:
        return sand


def simulate_sand_grain(wall: List[List[int]]):
    sand_spawn = Point(0, 500)

    _, bottom_right = get_boundaries(wall)
    abyss = bottom_right.x + 2
    wall[abyss] = [0] + [1 for _ in range(0, 988)] + [0]
    sand_grains = 1
    while True:
        #print("Simulating sand #", sand_grains)
        sand = sand_spawn
        moved_sand = update_move(sand, wall)
        while moved_sand != sand:
            #print(sand)
            sand = moved_sand
            moved_sand = update_move(sand, wall)
            if sand.x >= abyss:
                break
        if sand == sand_spawn:
            break
        else:
            sand_grains += 1
            wall[sand.x][sand.y] = 1
            continue
    return sand_grains


def parse_input_and_solve(filename):
    wall = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    with open(filename) as file:
        for line in file:
            directions = get_direction_from_string(line.strip("\n"))
            #print(directions)
            process_path(wall, directions)

    #print_wall(wall)
    grains = simulate_sand_grain(wall)

    return grains


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
