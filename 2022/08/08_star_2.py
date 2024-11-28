"""
https://adventofcode.com/2022/day/8

"""


def look_right(matrix, vis_matrix):
    for i, row in enumerate(matrix):
        for j, tree in enumerate(row):
            #print(i, j, tree, vis_matrix)
            if j == 0:
                vis_matrix[i][j] = 0
            else:
                h = j
                view = 0
                while h > 0 and row[h] <= tree:
                    view += 1
                    h -= 1
                    if row[h] == tree:
                        break
                vis_matrix[i][j] *= view


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
        visibility_map.append([1 for x in line.strip("\n")])
    # print(matrix)
    # print(visibility_map)
    for i in range(0, 4):
        #print(i, matrix, visibility_map)
        look_right(matrix, visibility_map)
        matrix = rotate_90(matrix)
        visibility_map = rotate_90(visibility_map)

    res = max([max(x) for x in visibility_map])
    #print(visibility_map)
    return res


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
