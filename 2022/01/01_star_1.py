"""
https://adventofcode.com/2022/day/1

"""


def parse_input_and_solve(filename):
    max_calories = 0
    file = open(filename)
    calories = 0
    for line in file:
        if line == "\n":
            max_calories = max(max_calories, calories)
            calories = 0
        else:
            calories += int(line)

    return max_calories


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
