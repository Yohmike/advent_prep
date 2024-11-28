from collections import namedtuple


def decode_boarding_pass(boarding_pass):
    binary_boarding_pass = ""
    for letter in boarding_pass:
        if letter == "F" or letter == "L":
            binary_boarding_pass += "0"
        elif letter == "B" or letter == "R":
            binary_boarding_pass += "1"
    return int(binary_boarding_pass, 2)


def parse_input_first_star(filename):
    file = open(filename)

    boarding_passes = []
    for line in file:
        decoded_bp = decode_boarding_pass(line)
        boarding_passes.append(decoded_bp)

    sorted_bp = sorted(boarding_passes)
    print(sorted_bp)
    non_consecutive_numbers = []
    for i, bp in enumerate(sorted_bp[1:-1], 1):
        if sorted_bp[i-1] == bp -1 and sorted_bp[i+1] == bp + 1:
            continue
        else:
            print(sorted_bp[i-1], bp, sorted_bp[i+1])
            non_consecutive_numbers.extend([sorted_bp[i-1], bp, sorted_bp[i+1]])

    return int(sum(non_consecutive_numbers)/len(non_consecutive_numbers))


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
