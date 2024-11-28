"""
https://adventofcode.com/2023/day/1

"""


def parse_input_and_solve(filename):
    calibration_sum = 0
    file = open(filename)
    for line in file:
        calibration_digits = [int(x) for x in line if x.isdigit()]
        calibration_sum += 10 * calibration_digits[0] + calibration_digits[-1]

    return calibration_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
