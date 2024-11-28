"""
https://adventofcode.com/2022/day/12

"""
from collections import deque

def djikstra(adj, vertices, source):
    to_visit = deque()
    inf = 100000
    used = [False for _ in range(0, vertices)]
    distance = [inf for _ in range(0, vertices)]
    parents = [-1 for _ in range(0, vertices)]
    to_visit.append(source)
    distance[source] = 0
    for i in range(0, vertices):
        v = -1
        for j in range(0, vertices):
            if not used[j] and (v == -1 or distance[j] < distance[v]):
                v = j
        if distance[v] == inf:
            break
        used[v] = True
        for edge in adj[v]:
            if distance[v] + 1 < distance[edge]:
                distance[edge] = distance[v] + 1
                parents[edge] = v
    return distance, parents


def get_neighbor(position, matrix):
    row, col = position
    if row < 0 or row > len(matrix) - 1:
        return None
    if col < 0 or col > len(matrix[0]) - 1:
        return None
    if matrix[row][col] in ["E", "S"]:
        return None
    return matrix[row][col]


def to_adj_list(matrix):
    source = -1
    destination = -1
    len_columns = len(matrix[0])
    adj_list = [[] for _ in range(0, len(matrix)*len_columns)]
    chars = ["" for _ in range(0, len(matrix)*len_columns)]
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            adj_index = i * len_columns + j
            left = (i, j - 1)
            right = (i, j + 1)
            up = (i - 1, j)
            down = (i + 1, j)
            neighbors = [up, down, left, right]
            chars[adj_index] = el
            if el == "S":
                source = adj_index
                for neighbor in neighbors:
                    value = get_neighbor(neighbor, matrix)
                    if value is not None and value == "a":
                        adj_list[adj_index].append(neighbor[0] * len_columns + neighbor[1])
                        adj_list[neighbor[0] * len_columns + neighbor[1]].append(adj_index)

            elif el == "E":
                destination = adj_index
                for neighbor in neighbors:
                    value = get_neighbor(neighbor, matrix)
                    if value is not None and value == "z":
                        #adj_list[adj_index].append(neighbor[0] * len_columns + neighbor[1])
                        adj_list[neighbor[0] * len_columns + neighbor[1]].append(adj_index)

            else:
                for neighbor in neighbors:
                    value = get_neighbor(neighbor, matrix)
                    if value is not None:
                        # if value == chr(ord(el) + 1) or value == chr(ord(el) - 1) or value == el:
                        #     adj_list[adj_index].append(neighbor[0] * len_columns + neighbor[1])
                        #     adj_list[neighbor[0] * len_columns + neighbor[1]].append(adj_index)
                        if value <= chr(ord(el) + 1):
                            adj_list[adj_index].append(neighbor[0] * len_columns + neighbor[1])

    print(chars)
    for i, l in enumerate(adj_list):
        adj_list[i] = list(set(l))
    return source, destination, adj_list, chars


def print_path(parents, start, chars):

    pred = parents[start]
    path = []
    while pred > -1:
        path.append(pred)
        pred = parents[pred]
    print([chars[step] for step in path])

    path.reverse()
    print(path)
    print([chars[step] for step in path])



def parse_input_and_solve(filename):
    file = open(filename)
    height_map = []
    for line in file:
        height_map.append(line.strip("\n"))
    source, destination, adj, chars = to_adj_list(height_map)
    #print(source, destination, adj)
    distances, parents = djikstra(adj, len(adj), source)
    #print(distances)
    #print(parents)
    print_path(parents, destination, chars)
    print("Result:", distances[destination] - 2)
    return


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
