"""
https://adventofcode.com/2024/day/18

"""

from dataclasses import dataclass
from math import inf


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

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, value):
        return self.row == value.row and self.col == value.col


def is_inside(maze, coord):
    return 0 <= coord.row < len(maze) and 0 <= coord.col < len(maze[0])


def find_valid_neighbors(maze, pos):
    neighbors = []
    directions = [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]
    for direction in directions:
        new_pos = pos + direction

        if is_inside(maze, new_pos) and maze[new_pos.row][new_pos.col] == ".":
            neighbors.append(new_pos)
    return neighbors


def get_min(q, dist):
    min_dist = inf
    index = -1
    for i, el in enumerate(q):
        if dist[el] < min_dist:
            index = i
            min_dist = dist[el]

    return index


def find_route(maze, start, end):
    dist = {}
    prev = {}
    from_dir = {}
    q = []
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == ".":
                node = Coord(row, col)
                dist[node] = inf
                prev[node] = None
                q.append(node)

    dist[start] = 0
    while q:
        min_index = get_min(q, dist)
        next = q.pop(min_index)
        if next == end:
            break
        valid_neighbors = find_valid_neighbors(maze, next)
        for pos in valid_neighbors:
            if pos in q:
                new_dist = 1 + dist[next]
                if new_dist < dist[pos]:
                    dist[pos] = new_dist
                    prev[pos] = next
    return dist, prev


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        maze = [["."] * 71 for _ in range(71)]
        for i, line in enumerate(lines):
            if i == 1024:
                break
            row, col = line.strip("\n").split(",")
            maze[int(row)][int(col)] = "#"

        start = Coord(0, 0)
        end = Coord(70, 70)
        distances, _ = find_route(maze, start, end)

        return distances[end]


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
