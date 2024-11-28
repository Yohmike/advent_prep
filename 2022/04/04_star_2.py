"""
https://adventofcode.com/2022/day/4

"""


def parse_input_and_solve(filename):
    file = open(filename)
    non_overlap_count = 0
    for i, line in enumerate(file, start=1):
        elf_1, elf_2 = line.strip("\n").split(',')
        elf_1_range = [int(x) for x in elf_1.split("-")]
        elf_2_range = [int(x) for x in elf_2.split("-")]
        if elf_1_range[1] < elf_2_range[0] or elf_2_range[1] < elf_1_range[0]:
            print(elf_1_range, elf_2_range)
            non_overlap_count += 1
    return i - non_overlap_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
