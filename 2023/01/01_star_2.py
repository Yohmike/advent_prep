"""
https://adventofcode.com/2023/day/1

"""


def process_line(line: str) -> int:
    digits = []
    string_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
        if char == "o" and line[i:i+3] == "one":
            digits.append(string_digits["one"])
        if char == "t":
            if line[i:i+3] == "two":
                digits.append(string_digits["two"])
            if line[i:i+5] == "three":
                digits.append(string_digits["three"])
        if char == "f":
            if line[i:i+4] == "four":
                digits.append(string_digits["four"])
            if line[i:i+4] == "five":
                digits.append(string_digits["five"])
        if char == "s":
            if line[i:i+3] == "six":
                digits.append(string_digits["six"])
            if line[i:i+5] == "seven":
                digits.append(string_digits["seven"])
        if char == "e" and line[i:i+5] == "eight":
            digits.append(string_digits["eight"])
        if char == "n" and line[i:i+4] == "nine":
            digits.append(string_digits["nine"])
    return 10 * digits[0] + digits[-1]


def parse_input_and_solve(filename: str) -> int:
    calibration_sum = 0
    file = open(filename)
    for line in file:
        calibration_sum += process_line(line)

    return calibration_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
