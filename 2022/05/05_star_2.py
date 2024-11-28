"""
https://adventofcode.com/2022/day/5

"""

def process_crates(crates):
    """
    each crate line has 4 chars for each crate except the last "[_] "
    :param crates:
    :return:
    """
    crate_count = len(crates[0])//4 + 1
    new_crates = []
    for i in range(0, crate_count):
        new_crates.append([])
    # print(new_crates)
    for crate in crates:
        # print("line", crate)
        crate_index = 0
        for i in range(1, len(crate), 4):
            # print(i, crate[i])
            if crate[i] != " ":
                new_crates[crate_index].append(crate[i])
            crate_index += 1
        # print(new_crates)
    return new_crates


def move_instruction(crates, instruction):
    print(instruction)
    crate_number, source_crate, destination_crate = instruction
    source_crate -= 1
    destination_crate -= 1
    crates_to_be_moved = []
    source_crate_len = len(crates[source_crate])
    if crate_number >= source_crate_len:
        crates_to_be_moved.extend(crates[source_crate][1:])
        crates[source_crate] = crates[source_crate][:1]
    else:
        crates_to_be_moved.extend(crates[source_crate][source_crate_len - crate_number:])
        crates[source_crate] = crates[source_crate][:source_crate_len - crate_number]
    print(crates_to_be_moved)
    crates[destination_crate].extend(crates_to_be_moved)
    print(crates)


def parse_input_and_solve(filename):
    file = open(filename)
    crates = []
    movements = []
    switch = False
    for i, line in enumerate(file, start=1):
        if line == "\n":
            switch = True
        if not switch:
            # build crates
            crates.append(line.strip("\n"))
        else:
            # movements
            if line == "\n":
                continue
            instruction = line.strip("\n").split(" ")
            movements.append([int(x) for x in [instruction[1], instruction[3], instruction[5]]])

    crates.reverse()
    crates = process_crates(crates)
    print(crates)
    print(movements)
    for instruction in movements:
        move_instruction(crates, instruction)
    print(crates)
    solution = ""
    for crate in crates:
        solution += crate[-1]
    return solution


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
