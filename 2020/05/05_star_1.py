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

    max_boarding_pass = 0
    for line in file:
        decoded_bp = decode_boarding_pass(line)
        print(decoded_bp)
        max_boarding_pass = max(max_boarding_pass,decoded_bp)
    # print(passports)
    return max_boarding_pass


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
