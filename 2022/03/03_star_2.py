"""
https://adventofcode.com/2022/day/3

"""


def priority(char):
    if char == char.lower():
        return ord(char) - ord('a') + 1
    if char == char.upper():
        return ord(char) - ord("A") + 27


def parse_input_and_solve(filename):
    file = open(filename)
    total_score = 0
    compartments = []
    for i, line in enumerate(file,start=1):
        rucksack = line.strip("\n")
        compartments.append(set(rucksack))
        if i % 3 == 0:
            total_score += priority(list(compartments[0].intersection(*compartments[1:]))[0])
            compartments = []
    return total_score


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
