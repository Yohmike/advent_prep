"""
https://adventofcode.com/2022/day/2

"""

def rps_compare(player1, player2):
    """
    Rock: A, X
    Paper: B, Y
    Scissors: C, Z
    :return: scores - 6 for win,  3 for tie, 0 for loss for the second player
    """
    win = 6
    loss = 0
    draw = 3
    match_results = {
        "AX": draw,
        "AY": win,
        "AZ": loss,
        "BX": loss,
        "BY": draw,
        "BZ": win,
        "CX": win,
        "CY": loss,
        "CZ": draw
    }
    return match_results[player1 + player2]

def parse_input_and_solve(filename):
    file = open(filename)
    played_score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    total_score = 0
    for line in file:
        player1, player2 = line.strip("\n").split(" ")
        total_score += played_score[player2] + rps_compare(player1, player2)
    return total_score


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
