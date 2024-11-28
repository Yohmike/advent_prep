
def parse_input_first_star(filename):
    file = open(filename)
    answers = []
    vote = ""
    for line in file:
        if line != "\n":
            # print(line)
            vote += line.strip("\n")
        else:
            # print(vote)
            answer = len(set(vote))
            answers.append(answer)
            vote = ""

    answer = len(set(vote))
    answers.append(answer)
    # print(passports)
    return sum(answers)


def main():
    input_file_name = "input"
    print(parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
