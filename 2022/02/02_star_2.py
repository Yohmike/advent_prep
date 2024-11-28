"""
https://adventofcode.com/2022/day/2

"""


def parse_input_and_solve(filename):
    file = open(filename)
    loss = 0
    draw = 3
    win = 6
    rock = 1
    paper = 2
    scissors = 3
    played_score = {
        "AX": scissors,
        "AY": rock,
        "AZ": paper,
        "BX": rock,
        "BY": paper,
        "BZ": scissors,
        "CX": paper,
        "CY": scissors,
        "CZ": rock
    }
    match_results = {
        "X": loss,
        "Y": draw,
        "Z": win
    }
    total_score = 0
    for line in file:
        player1, player2 = line.strip("\n").split(" ")
        total_score += played_score[player1 + player2] + match_results[player2]
    return total_score


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
