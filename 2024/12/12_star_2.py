"""
https://adventofcode.com/2024/day/12

"""

from dataclasses import dataclass
from collections import deque, defaultdict


@dataclass
class Region:
    row: int
    col: int
    perimeter: int = 0
    area: int = 0
    letter: str = ""


def look_around_for(matrix, row, col, letter):
    found = []
    dirs = []
    all_dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    if row - 1 >= 0:
        if matrix[row - 1][col] == letter:
            found.append([row - 1, col])
            dirs.append([-1, 0])
    if col - 1 >= 0:
        if matrix[row][col - 1] == letter:
            found.append([row, col - 1])
            dirs.append([0, -1])

    if col + 1 < len(matrix[0]):
        if matrix[row][col + 1] == letter:
            found.append([row, col + 1])
            dirs.append([0, 1])
    if row + 1 < len(matrix):
        if matrix[row + 1][col] == letter:
            found.append([row + 1, col])
            dirs.append([1, 0])
    return found, [d for d in all_dirs if d not in dirs]


def compute_lines(lines):
    lines_count = 0
    for line in lines.values():
        line.sort()
        lines_count += 1
        for i in range(1, len(line)):
            if line[i] - 1 > line[i - 1]:
                lines_count += 1
    return lines_count


def get_area_and_perimeter_for(plots, visited, row, col):
    letter = plots[row][col]

    region = Region(row, col, letter=letter)
    q = deque([[row, col]])
    h_lines = defaultdict(list)
    v_lines = defaultdict(list)
    bottom_h_lines = defaultdict(list)
    bottom_v_lines = defaultdict(list)

    while q:
        next = q.popleft()
        next_row, next_col = next
        if visited[next_row][next_col] == -1:
            visited[next_row][next_col] = 1
            neigh, dirs = look_around_for(plots, next_row, next_col, letter)
            region.area += 1
            if len(neigh) != 4:
                for dir in dirs:
                    r, c = dir
                    if r == 0:
                        if c == 1:
                            bottom_v_lines[next_col + c].append(next_row)
                        else:
                            v_lines[next_col + c].append(next_row)
                    if c == 0:
                        if r == 1:
                            bottom_h_lines[next_row + r].append(next_col)
                        else:
                            h_lines[next_row + r].append(next_col)
            q.extend(neigh)

    h_lines_count = compute_lines(h_lines) + compute_lines(bottom_h_lines)
    v_lines_count = compute_lines(v_lines) + compute_lines(bottom_v_lines)

    region.perimeter = v_lines_count + h_lines_count
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
