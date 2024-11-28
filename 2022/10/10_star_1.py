"""
https://adventofcode.com/2022/day/10

"""


def update_signal_strength(clock, x_reg):
    print("-"*20, clock, x_reg)
    signal_strength = x_reg * clock
    return signal_strength


def parse_input_and_solve(filename):
    file = open(filename)
    clock = 0
    x_register = 1
    signal_strength = 0
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    for line in file:
        if not interesting_cycles:
            break
        # print(clock, x_register)
        instruction = line.strip("\n").split(" ")
        #print(instruction)
        if instruction[0] == "noop":
            # print("noop")
            clock += 1
            if clock == interesting_cycles[0]:
                signal_strength += update_signal_strength(interesting_cycles.pop(0), x_register)
        if instruction[0] == "addx":
            # print("addx", instruction)
            if clock + 1 == interesting_cycles[0] or clock + 2 == interesting_cycles[0]:
                signal_strength += update_signal_strength(interesting_cycles.pop(0), x_register)
            x_register += int(instruction[1])
            clock += 2

    return signal_strength


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
