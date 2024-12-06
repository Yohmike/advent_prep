"""
https://adventofcode.com/2024/day/5

"""

from collections import defaultdict


def check_rules(rules, update):
    for i in range(0, len(update)):
        for j in range(0, len(update)):
            if j < i:
                if update[i] not in rules[update[j]]:
                    return False
            if j > i:
                if update[j] not in rules[update[i]]:
                    return False
    return True


def reorder_update(rules, update):
    left = defaultdict(list)
    right = defaultdict(list)
    for el in update:
        for el2 in update:
            if el != el2:
                if el in rules[el2]:
                    # of elements before this element
                    left[el].append(el2)

    ordering = [0 for _ in range(len(update))]
    for el in update:
        ordering[len(left[el])] = el
    return ordering


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    rules = defaultdict(list)
    updates = []
    with open(filename) as file:

        switch_to_updates = False
        for line in file:
            if line == "\n":
                switch_to_updates = True
                continue
            if not switch_to_updates:
                left, right = line.strip("\n").split("|")
                rules[int(left)].append(int(right))
            else:
                updates.append([int(x) for x in line.strip("\n").split(",")])

    for update in updates:
        if not check_rules(rules, update):
            ordered = reorder_update(rules, update)
            update_count += ordered[len(ordered) // 2]

    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
