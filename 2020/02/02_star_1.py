import re


def parse_input_first_star(filename):
    pattern = re.compile("([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)")
    file = open(filename)
    valid_passwords_count = 0
    for line in file:
        # print(line)
        tokens = re.match(pattern, line).groups()
        min_aparitions, max_aparitions, letter, password = tokens
        aparitions = password.count(letter)
        # print(aparitions)
        if int(min_aparitions) <= aparitions <= int(max_aparitions):
            valid_passwords_count += 1
    print(f"Valid password count is: {valid_passwords_count}")
    return valid_passwords_count


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()