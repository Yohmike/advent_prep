"""
https://adventofcode.com/2022/day/4

"""


def parse_input_and_solve(filename):
    file = open(filename)
    overlap_count = 0
    for line in file:
        line.strip("\n")
        char_window = []
        for i, char in enumerate(line, start=1):
            print(char)
            char_window.append(char)
            print(char_window)
            if len(char_window) < 4:
                continue
            elif len(char_window) == 4:
                print(set(char_window))
                if len(set(char_window)) == len(char_window):
                    return i
                char_window.pop(0)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
