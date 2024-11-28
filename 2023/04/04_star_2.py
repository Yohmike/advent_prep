"""
https://adventofcode.com/2023/day/4

"""
import queue
from typing import Tuple, List
from math import prod
from dataclasses import dataclass
from collections import deque

@dataclass
class Card:
    id: int
    winning_numbers: List[int]
    numbers: List[int]

    def compute_score(self) -> int:
        score = 0
        for card in self.numbers:
            if card in self.winning_numbers:
                score += 1
        #print(score, self)
        return score


def get_card(line:str) -> Card:
    card_index_part, card_values_part = line.split(":")
    card_index = int(card_index_part.split()[-1])
    winning_cards, current_cards = card_values_part.split("|")

    return Card(card_index, [int(x) for x in winning_cards.split()], [int(x) for x in current_cards.split()])

def process_cards(cards: List[Card]) -> int:
    card_copies = [1 for _ in cards]
    for card in cards:
        score = card.compute_score()
        for i in range(0, score):
            card_copies[card.id + i] += card_copies[card.id - 1]
        #print(card_copies)

    counter = sum(card_copies)



    return counter

def parse_input_and_solve(filename):
    file = open(filename)
    cards = []
    for line in file:
        card = get_card(line)
        cards.append(card)
    print(cards)
    tickets = process_cards(cards)
    print(tickets)
    return tickets




def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
