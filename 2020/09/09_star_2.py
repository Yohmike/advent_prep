
def parse_input_first_star(filename):
    file = open(filename)
    sequences = []
    preamble = 25
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
                odd_number = current_seq

    # print(f"odd number: {odd_number}")
    # print(f"sequences {sequences}")
    rolling_window = []
    # TODO // stop recomputing sum at every step
    for elem in sequences:
        if elem != odd_number:
            rolling_window.append(elem)
            rolling_sum = sum(rolling_window)
            if rolling_sum == odd_number:
                # print(f"found it! {rolling_sum, rolling_window}")
                return min(rolling_window) + max(rolling_window)
            elif rolling_sum < odd_number:
                # print(f"not found it, smaller! {rolling_sum, rolling_window}")
                continue

            elif rolling_sum > odd_number:
                # print(f"not found it, bigger! {rolling_sum, rolling_window}")
                while rolling_sum > odd_number:
                    rolling_window.pop(0)
                    rolling_sum = sum(rolling_window)
                if rolling_sum == odd_number:
                    # print(f"returning {rolling_window}, {rolling_sum}, {odd_number}")
                    return min(rolling_window) + max(rolling_window)
                # TODO // do i need to pop right too?


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
