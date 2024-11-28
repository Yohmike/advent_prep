"""
https://adventofcode.com/2022/day/8

"""
from copy import deepcopy


def look_up(matrix, vis_matrix):
    visibility_height = deepcopy(matrix[0])
    vis_matrix[0] = [1 for _ in matrix[0]]
    for i, row in enumerate(matrix[1:], 1):
        for j, tree in enumerate(row):
            #print(i, j, tree, visibility_height[j])
            if tree > visibility_height[j]:
                visibility_height[j] = max(tree, visibility_height[j])
                vis_matrix[i][j] = 1


def rotate_90(matrix):
    new_matrix = [[] for _ in matrix[0]]
    for row in matrix:
        for i, el in enumerate(row[::-1]):
            new_matrix[i].append(el)
    return new_matrix



def parse_input_and_solve(filename):
    file = open(filename)
    matrix = []
    visibility_map = []
    for line in file:
        matrix.append([int(x) for x in line.strip("\n")])
        visibility_map.append([0 for x in line.strip("\n")])
    # print(matrix)
    # print(visibility_map)
    for i in range(0, 4):
        # print(i, matrix, visibility_map)
        look_up(matrix, visibility_map)
        matrix = rotate_90(matrix)
        visibility_map = rotate_90(visibility_map)

    res = sum([sum(x) for x in visibility_map])
    return res



def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
