"""
https://adventofcode.com/2022/day/11

"""
from dataclasses import dataclass, field


@dataclass
class Monkey:
    id: int = 0
    items: list = field(default_factory=list)
    operation: list = field(default_factory=list)
    test: int = -1
    test_true: int = 0
    test_false: int = 0
    items_inspected: int = 0


def decode_line(words, monkey):
    #print(words)
    decoded_monkey = False
    if words[0] == "Monkey":
        monkey.id = int(words[-1].split(":")[0])
    if len(words) > 2 and words[2] == "Starting":
        monkey.items = [int(x.strip(",")) for x in words[4:]]
    elif len(words) > 2 and words[2] == "Operation:":
        monkey.operation = words[-3:]
    elif len(words) > 2 and words[2] == "Test:":
        monkey.test = int(words[-1])
    elif len(words) > 4 and words[5] == "true:":
        monkey.test_true = int(words[-1])
    elif len(words) > 4 and words[5] == "false:":
        monkey.test_false = int(words[-1])
    return decoded_monkey


def worry_operation(item, operation):
    _, op, quantity = operation
    amount = 0
    if quantity == "old":
        amount = item
    else:
        amount = int(quantity)

    if op == "*":
        return item * amount
    if op == "+":
        return item + amount


def throw_items(monkeys, monkey_id, divider):
    monkey = monkeys[monkey_id]
    for item in monkey.items:
        monkey.items_inspected += 1
        worry_level = worry_operation(item, monkey.operation) % divider
        if worry_level % monkey.test == 0:
            monkeys[monkey.test_true].items.append(worry_level)
        else:
            monkeys[monkey.test_false].items.append(worry_level)
    monkey.items = []


def simulate_rounds(monkeys, divider, rounds=20):
    for round in range(0, rounds):
        if round % 1000 == 0:
            print("Round", round)
        for monkey in monkeys:
            throw_items(monkeys, monkey.id, divider)


def parse_input_and_solve(filename):
    file = open(filename)
    monkeys = []
    monkey = Monkey()
    for line in file:
        if line == "\n":
            monkeys.append(monkey)
            monkey = Monkey()
        else:
            decode_line(line.strip("\n").split(" "), monkey)
    monkeys.append(monkey)
    #print(monkeys)
    divider = 1
    for monkey in monkeys:
        divider *= monkey.test
    simulate_rounds(monkeys, divider, 10000)
    print(monkeys)
    inspections = [monkey.items_inspected for monkey in monkeys]
    max_inspections = max(inspections)
    inspections.pop(inspections.index(max(inspections)))
    return max(inspections) * max_inspections


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
