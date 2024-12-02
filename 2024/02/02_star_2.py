"""
https://adventofcode.com/2024/day/2

"""

from typing import List


def sign(number: int) -> int:
    if number == 0:
        return 0
    if number > 0:
        return 1
    else:
        return -1


def is_safe_strict(report: List[int]) -> bool:
    signs = [sign(report[i] - report[i - 1]) for i in range(1, len(report))]
    report_sign = -1 if signs.count(-1) > signs.count(1) else 1

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3 and sign(diff) == report_sign):
            return False
    return True


def is_safe(report: List[int]) -> bool:
    signs = [sign(report[i] - report[i - 1]) for i in range(1, len(report))]
    report_sign = -1 if signs.count(-1) > signs.count(1) else 1
    one_bad = False
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3 and sign(diff) == report_sign):
            if not one_bad:
                one_bad = True

                return is_safe_strict(
                    report[: max(0, i - 1)] + report[i:]
                ) or is_safe_strict(report[:i] + report[i + 1 :])
            else:
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
