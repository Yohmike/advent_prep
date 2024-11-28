"""
https://adventofcode.com/2022/day/10

"""


def update_signal_strength(clock, x_reg):
    print("-"*20, clock, x_reg)
    signal_strength = x_reg * clock
    return signal_strength


def is_sprite_drawable(x_reg, clock):
    return x_reg <= clock <= x_reg +2


def parse_input_and_solve(filename):
    file = open(filename)
    x_register = 1
    interesting_cycles = [40, 80, 120, 160, 200, 240]
    instructions = []
    instruction_counter = -1
    update_register = None
    for line in file:
        instruction = line.strip("\n").split(" ")
        instructions.append(instruction)
    new_instruction = instructions.pop(0)
    crt_line = ""
    for cycle in range(1, 241):
        # print(cycle, x_register, processed_instruction, new_instruction, instruction_counter, crt_line)
        if is_sprite_drawable(x_register, cycle % 40):
            crt_line += "#"
        else:
            crt_line += "."
        if cycle == interesting_cycles[0]:
            print(crt_line)
            crt_line = ""
            interesting_cycles.pop(0)

        if new_instruction is None:
            instruction_counter -= 1
        elif new_instruction[0] == "noop":
            instruction_counter = 0
            new_instruction = None
        elif new_instruction[0] == "addx":
            instruction_counter = 1
            update_register = int(new_instruction[1])
            new_instruction = None

        if instruction_counter == 0:
            if update_register is not None:
                x_register += update_register
                update_register = None
            if instructions:
                new_instruction = instructions.pop(0)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
