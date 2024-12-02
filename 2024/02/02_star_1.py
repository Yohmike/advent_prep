"""
https://adventofcode.com/2024/day/2

"""

from typing import List


def sign(number: int) -> int:
    if number >= 0:
        return 1
    else:
        return -1


def is_safe(report: List[int]) -> bool:
    report_sign = sign(report[-1] - report[0])
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3 and sign(diff) == report_sign):
            return False
    return True


def parse_input_and_solve(filename: str) -> int:
    safe_count = 0
    with open(filename) as file:
        for line in file:
            ids = [int(x) for x in line.split(" ")]
            if is_safe(ids):
                safe_count += 1
    return safe_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
