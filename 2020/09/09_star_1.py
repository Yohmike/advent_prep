
def parse_input_first_star(filename):
    file = open(filename)
    sequences = []
    preamble = 5
    for i, line in enumerate(file):
        current_seq = int(line)
        if i < preamble:
            sequences.append(int(line))
        else:
            found_sum = False
            # print(f"current list {sequences}")
            for elem in sequences[-preamble:]:
                if current_seq - elem in sequences[-preamble:]:
                    found_sum = True
                    break
            sequences.append(current_seq)
            if not found_sum:
                return current_seq



def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
