import re


def parse_input_first_star(filename):
    pattern = re.compile("([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)")
    file = open(filename)
    valid_passwords_count = 0
    for line in file:
        # print(line)
        tokens = re.match(pattern, line).groups()
        first_aparitions, second_aparitions, letter, password = tokens
        # Make it zero indexed
        first_aparitions = int(first_aparitions) - 1
        second_aparitions = int(second_aparitions) - 1
        if password[first_aparitions] == letter or password[second_aparitions] == letter:
            if not (password[first_aparitions] == letter and password[second_aparitions] == letter):
                valid_passwords_count += 1
    print(f"Valid password count is: {valid_passwords_count}")
    return valid_passwords_count


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()