"""
https://adventofcode.com/2017/day/1

"""


def parse_input_and_solve(filename):
    calibration_sum = 0
    with open(filename) as file:
        capcha_digits = [int(x) for x in str(file.readlines()[0])]
        print(capcha_digits)
    capcha_sum = 0
    mid = len(capcha_digits) // 2
    for i in range(0, len(capcha_digits)):
        print(i, (i + mid) % (len(capcha_digits)))
        if capcha_digits[i] == capcha_digits[(i + mid) % len(capcha_digits)]:
            capcha_sum += capcha_digits[i]

    return capcha_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
