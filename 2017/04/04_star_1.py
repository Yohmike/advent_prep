"""
https://adventofcode.com/2017/day/4

"""

from collections import defaultdict


def parse_input_and_solve(filename):

    with open(filename) as file:
        valid_count = 0
        for line in file:
            passphrase = line[:-1].split(" ")
            passphrase_dict = defaultdict(int)
            for word in passphrase:
                passphrase_dict[word] += 1
            if max(passphrase_dict.values()) <= 1:
                valid_count += 1
    return valid_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
