"""
https://adventofcode.com/2022/day/4

"""


def parse_input_and_solve(filename):
    file = open(filename)
    overlap_count = 0
    for i, line in enumerate(file,start=1):
        elf_1, elf_2 = line.strip("\n").split(',')
        elf_1_range = [int(x) for x in elf_1.split("-")]
        elf_2_range = [int(x) for x in elf_2.split("-")]
        if elf_1_range[0] >= elf_2_range[0] and elf_1_range[1] <= elf_2_range[1]:
            print(elf_1_range, elf_2_range)
            overlap_count += 1
        if elf_2_range[0] >= elf_1_range[0] and elf_2_range[1] <= elf_1_range[1]:
            print("2", elf_1_range, elf_2_range)
            overlap_count += 1
        if elf_2_range[0] == elf_1_range[0] and elf_2_range[1] == elf_1_range[1]:
            overlap_count -= 1
    return overlap_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
