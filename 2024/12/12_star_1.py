"""
https://adventofcode.com/2024/day/12

"""

from dataclasses import dataclass
from collections import deque


@dataclass
class Region:
    row: int
    col: int
    perimeter: int = 0
    area: int = 0


def look_around_for(matrix, row, col, letter):
    found = []
    if row - 1 >= 0:
        if matrix[row - 1][col] == letter:
            found.append([row - 1, col])
    if col - 1 >= 0:
        if matrix[row][col - 1] == letter:
            found.append([row, col - 1])

    if col + 1 < len(matrix[0]):
        if matrix[row][col + 1] == letter:
            found.append([row, col + 1])
    if row + 1 < len(matrix):
        if matrix[row + 1][col] == letter:
            found.append([row + 1, col])
    return found


def get_area_and_perimeter_for(plots, visited, row, col):
    region = Region(row, col)
    q = deque([[row, col]])
    letter = plots[row][col]
    while q:
        next = q.popleft()
        next_row, next_col = next
        if visited[next_row][next_col] == -1:
            visited[next_row][next_col] = 1
            neigh = look_around_for(plots, next_row, next_col, letter)
            region.area += 1
            region.perimeter += 4 - len(neigh)
            q.extend(neigh)
    return region


def visit_plots(plots):
    visited = [[-1] * len(plots[0]) for _ in range(len(plots))]
    regions = []
    for row in range(len(plots)):
        for col in range(len(plots[0])):
            if visited[row][col] == -1:
                region = get_area_and_perimeter_for(plots, visited, row, col)
                regions.append(region)
    return regions


def add_perimeter_area_for_region(regions):
    total = 0
    for region in regions:
        total += region.perimeter * region.area
    return total


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    plot_matrix = []
    with open(filename) as file:
        for line in file:
            plot_matrix.append(list(line.strip("\n")))
    regions = visit_plots(plot_matrix)

    update_count = add_perimeter_area_for_region(regions)
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
