"""
https://adventofcode.com/2024/day/20

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


def get_symbol_position(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == symbol:
                return Coord(row, col)


def find_valid_neighbors(maze, pos, symbol="."):
    neighbors = []
    directions = [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]
    for direction in directions:
        new_pos = pos + direction

        if is_inside(maze, new_pos) and maze[new_pos.row][new_pos.col] == symbol:
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
    q = []
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "." or maze[row][col] == "S":
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


def get_path(routes, start, end):
    path = []
    next = end
    while next != start:
        path.append(next)
        next = routes[next]
    path.append(start)
    return path[::-1]


def get_walls(maze, route):
    walls = []
    for node in route:
        neigh_walls = find_valid_neighbors(maze, node, "#")
        for neigh_wall in neigh_walls:
            if neigh_wall not in walls:
                walls.append(neigh_wall)
    return walls


def get_saved_seconds(maze, current, wall, distances, path):
    direction = wall - current
    skip = wall + direction
    if is_inside(maze, skip) and skip in path:
        return distances[skip] - distances[current] - 2
    return 0


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        maze = []
        for line in lines:
            maze.append(list(line.strip("\n")))

        start = get_symbol_position(maze, "S")
        end = get_symbol_position(maze, "E")
        maze[end.row][end.col] = "."
        distances, prev = find_route(maze, start, end)
        route = get_path(prev, start, end)
        maze[start.row][start.col] = "."
        smaller = 0
        # see part 2, if you change the `max_picosends_cheat` to 2 you get part1
        for el in route:
            walls = find_valid_neighbors(maze, el, "#")
            for wall in walls:
                secs = get_saved_seconds(maze, el, wall, distances, route)
                if secs >= 100:
                    smaller += 1

        return smaller


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
