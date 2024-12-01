"""
https://adventofcode.com/2024/day/1

"""


def parse_input_and_solve(filename: str) -> int:
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            ids = line.split(" ")
            left.append(int(ids[0]))
            right.append(int(ids[-1]))
    left.sort()
    right.sort()
    return sum([abs(l - r) for l, r in zip(left, right)])


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
