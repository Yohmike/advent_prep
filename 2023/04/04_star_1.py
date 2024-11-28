"""
https://adventofcode.com/2023/day/4

"""
from typing import Tuple, List
from math import prod
from dataclasses import dataclass

@dataclass
class Card:
    id: int
    winning_numbers: List[int]
    numbers: List[int]

    def compute_score(self) -> int:
        score = 0
        for card in self.numbers:
            if card in self.winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        #print(score, self)
        return score


def get_card(line:str) -> Card:
    card_index_part, card_values_part = line.split(":")
    card_index = int(card_index_part.split()[-1])
    winning_cards, current_cards = card_values_part.split("|")

    return Card(card_index, [int(x) for x in winning_cards.split()], [int(x) for x in current_cards.split()])



def parse_input_and_solve(filename):
    file = open(filename)
    cards = []
    score = 0
    for line in file:
        card = get_card(line)
        cards.append(card)
        score += card.compute_score()
    print(cards)
    print(score)



def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
