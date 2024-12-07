"""
https://adventofcode.com/2024/day/7

"""

from copy import deepcopy
from itertools import combinations


def eval_op(op, left, right):
    if op == "+":
        return left + right
    if op == "*":
        return left * right
    if op == "||":
        return int(str(left) + str(right))


def generate_posib_for_operator(starting_op, op):
    posibilities = [starting_op]
    mul_pos = [i for i in range(0, len(starting_op))]
    mul_comb = []

    for i in range(len(mul_pos)):
        mul_comb.extend(combinations(mul_pos, i + 1))

    for mul in mul_comb:
        new_posib = deepcopy(starting_op)
        for pos in mul:
            new_posib[pos] = op
        posibilities.append(new_posib)
    return posibilities


def generate_operator_posibilities(starting_op):
    add_mul_posibitlities = generate_posib_for_operator(starting_op, "*")
    add_mul_cocncat_posib = []
    for ad_mul in add_mul_posibitlities:
        add_mul_cocncat_posib.extend(generate_posib_for_operator(ad_mul, "||"))
    return add_mul_cocncat_posib


def can_generate_result(res, operands):
    operator_len = len(operands) - 1
    starting_operators = list("+" * operator_len)
    resulting_operators = generate_operator_posibilities(starting_operators)
    # print(resulting_operators)
    for operators in resulting_operators:
        partial_res = operands[0]
        # print(operators, partial_res)
        for i, operator in enumerate(operators):
            # print(i, operator, partial_res, operands[i + 1])
            partial_res = eval_op(operator, partial_res, operands[i + 1])
        if partial_res == res:
            return True
    return False


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    results = []
    operands = []
    with open(filename) as file:
        for line in file:
            result, ops = line.strip("\n").split(":")
            results.append(int(result))
            operands.append([int(x) for x in ops.split(" ") if x != ""])
    print(results)
    print(operands)

    for res, op in zip(results, operands):
        if can_generate_result(res, op):
            # print(res, op)
            update_count += res
        else:
            print(res, op)

    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
