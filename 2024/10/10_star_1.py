"""
https://adventofcode.com/2024/day/10

"""


def find_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def find_next_trail_steps(map, position, hike_index):
    next_trail_step = []
    row, col = position
    if 0 <= row - 1 and map[row - 1][col] == hike_index:
        next_trail_step.append((row - 1, col))
    if row + 1 < len(map) and map[row + 1][col] == hike_index:
        next_trail_step.append((row + 1, col))
    if 0 <= col - 1 and map[row][col - 1] == hike_index:
        next_trail_step.append((row, col - 1))
    if col + 1 < len(map[0]) and map[row][col + 1] == hike_index:
        next_trail_step.append((row, col + 1))

    return next_trail_step


def find_trail(map, position):
    trail = [position]
    for i in range(1, 10):
        new_trails = []
        for t in trail:
            new_trail = find_next_trail_steps(map, t, i)
            for nt in new_trail:
                if nt not in new_trails:
                    new_trails.append(nt)
        if new_trails == []:
            return []
        trail = new_trails
    return trail


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    map = []
    with open(filename) as file:
        for line in file:
            map.append([int(x) for x in line.strip("\n")])
    trailheads = find_trailheads(map)
    for trailhead in trailheads:
        trails = find_trail(map, trailhead)
        update_count += len(trails)
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
