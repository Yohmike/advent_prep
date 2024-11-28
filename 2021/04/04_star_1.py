import numpy as np


class Board:
    def __init__(self, row_size=5, col_size=5):
        self.row = row_size
        self.col = col_size
        self.board, self.marked_board = self._build_empty_board()

        self.board_won = False
        self.winner_number_and_position = None

    def _build_empty_board(self):
        board = []
        for i in range(0, self.col):
            board.append([0 for j in range(0, self.row)])
        return np.array(board), np.ma.masked_array(board, mask=False)

    def __repr__(self):
        print(f"Board size is {self.row} x {self.col}")
        print(f"Board size is {self.row} x {self.col}")
        for line in self.board:
            print(*line, " ")
        for line in self.marked_board:
            print(*line, " ")
        return ""

    def build(self, input: str):
        #print(input.split("\n"))
        board = []
        for i, line in enumerate(input.strip("\n").split("\n")):
            elements = line.split()
            #print(len(elements))
            #print(elements)
            board.append([int(x) for x in elements])
            self.board = np.array(board)

    def mark_bingo_number(self, number: int):
        #print(number)
        #print(self.board)
        #print(self.marked_board)
        indices = np.where(self.board == number)
        #print(indices)
        if len(indices) > 0 and len(indices[0]) > 0:
            row = indices[0][0]
            col = indices[1][0]
            self.marked_board[row][col] = True
            #print("marking ", self.marked_board)
            #print("row sum", sum(self.marked_board[row]))
            if sum(self.marked_board[row]) == 5 or sum(self.marked_board[:, col]) == 5:
                self.board_won = True
                self.winner_number_and_position = (number, row, col)

    def compute_winning_score(self):
        if self.board_won == True:
            #print("compute score")
            masked = np.ma.masked_array(self.board, mask=self.marked_board)
            #print(np.ma.compressed(masked))
            score = sum(np.ma.compressed(masked))
            return score
        else:
            return 0


def parse_input_and_solve(filename):
    with open(filename) as f:
        bingo_numbers = [int(x) for x in f.readline().split(",")]
        #print(bingo_numbers)
        boards = []
        index = -1
        board_string = ""
        for line in f:
            #print(line, index)
            index += 1
            if index == 5:
                index = -1
                board_string += line
                board = Board()
                #print(board_string)
                board.build(board_string)
                #print(board)
                board_string = ""
                boards.append(board)

            elif index == 0:
                continue
            else:
                board_string += line
        print("play bingo")
        #print(boards)
        for bingo_number in bingo_numbers:
            for board in boards:
                #print(bingo_number, board)
                board.mark_bingo_number(bingo_number)
                if board.board_won == True:
                    score = board.compute_winning_score()
                    return score * bingo_number

def main():
    input_file_name = "../input"
    score = parse_input_and_solve(input_file_name)
    print(f"Final score is: {score}")



if __name__ == "__main__":
    main()