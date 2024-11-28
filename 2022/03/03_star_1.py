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
    for line in file:
        rucksack = line.strip("\n")
        size = len(rucksack)
        compartment1 = set(rucksack[:size//2])
        compartment2 = set(rucksack[size//2:])
        total_score += priority(list(compartment1.intersection(compartment2))[0])
    return total_score


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
