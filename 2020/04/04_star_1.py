from collections import namedtuple


def process_passport(passport):
    passport_components = passport.strip(" ").split(" ")
    # print(passport_components)
    identifiers = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_identifiers = ["cid"]

    for identifier in identifiers:
        if identifier not in passport:
            # print("False::::", identifier, passport)
            return False
    return True


def parse_input_first_star(filename):
    file = open(filename)

    passports = []
    passport = ""
    for line in file:
        if line != "\n":
            # print(line)
            passport += line.strip("\n") + " "
        else:
            # print(line)
            # passport complete, strip last whitespace
            processed_passport = process_passport(passport)
            passports.append(processed_passport)
            passport = ""
    processed_passport = process_passport(passport)
    passports.append(processed_passport)
    # print(passports)
    return passports.count(True)


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
