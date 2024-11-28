from collections import namedtuple


def byr_valid(input_str):
    number = int(input_str)
    return 1920 <= number <= 2002


def iyr_valid(input_str):
    number = int(input_str)
    return 2010 <= number <= 2020


def eyr_valid(input_str):
    number = int(input_str)
    return 2020 <= number <= 2030


def hgt_valid(input_str):
    number = int(input_str[:-2])
    unit = input_str[-2:]
    return (unit == "cm" and (150 <= number < 193)) or (unit == "in" and (59 <= number <= 76))


def hcl_valid(input_str):
    return input_str[0] == "#" and input_str[1:].isalnum()


def ecl_valid(input_str):
    return input_str in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_valid(input_str):
    return input_str.isdigit()


def process_passport(passport):
    passport_components = passport.strip(" ").split(" ")
    passport_dict = {x.split(":")[0]: x.split(":")[1] for x in passport_components}
    # print(passport_components)
    identifiers = {
        "byr": byr_valid,
        "iyr": iyr_valid,
        "eyr": eyr_valid,
        "hgt": hgt_valid,
        "hcl": hcl_valid,
        "ecl": ecl_valid,
        "pid": pid_valid
    }
    optional_identifiers = ["cid"]

    for identifier in identifiers:
        if identifier not in passport_dict.keys():
            return False
        if not identifiers[identifier](passport_dict[identifier]):
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
