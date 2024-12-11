"""
https://adventofcode.com/2024/day/11

"""


def apply_rules(stone):
    if stone == 0:
        return [1]

    stone_s = str(stone)
    if len(stone_s) % 2 == 0:
        return [int(stone_s[: len(stone_s) // 2]), int(stone_s[len(stone_s) // 2 :])]

    return [stone * 2024]


def blink(arrangement):
    for _ in range(25):
        new_arrangement = []
        for stone in arrangement:
            new_arrangement.extend(apply_rules(stone))
        arrangement = new_arrangement
    return len(arrangement)


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    with open(filename) as file:
        initial_arangement = [int(x) for x in file.readline().strip("\n").split(" ")]
    update_count = blink(initial_arangement)
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
