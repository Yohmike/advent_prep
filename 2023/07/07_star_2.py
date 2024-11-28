"""
https://adventofcode.com/2023/day/7

"""
from typing import Tuple, List, Dict
from math import prod, sqrt, ceil, floor
from itertools import combinations
from dataclasses import dataclass
from enum import Enum
import functools


class HandType(Enum):
    NONE = 0
    ONE_KIND = 1
    TWO_KIND = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_KIND = 5
    FIVE_KIND = 6


@functools.total_ordering
class Hand:

    def __init__(self, hand_string: str):
        self.hand_string = hand_string
        self.h_dict = {}
        self.h_type = self.get_type()

    def get_type(self):
        h_type = HandType.NONE
        for char in self.hand_string:
            self.h_dict[char] = self.h_dict.get(char, 0) + 1
        if self.h_dict.get("J", 0) > 0:
            j_counts = self.h_dict["J"]
            if len(self.h_dict.keys()) != 1:
                del self.h_dict["J"]
            max_val = max(self.h_dict.values())
            self.h_dict[list(self.h_dict.keys())[list(self.h_dict.values()).index(max_val)]] += j_counts

        if self.is_five():
            h_type = HandType.FIVE_KIND
        elif self.is_four():
            h_type = HandType.FOUR_KIND
        elif self.is_full():
            h_type = HandType.FULL_HOUSE
        elif self.is_three():
            h_type = HandType.THREE_KIND
        elif self.is_two():
            h_type = HandType.TWO_KIND
        elif self.is_one():
            h_type = HandType.ONE_KIND
        return h_type

    def is_five(self):
        return len(self.h_dict.keys()) == 1

    def is_four(self):
        return len(self.h_dict.keys()) == 2 and \
               min(self.h_dict.values()) == 1 and \
               max(self.h_dict.values()) == 4

    def is_full(self):
        return len(self.h_dict.keys()) == 2 and \
               min(self.h_dict.values()) == 2 and \
               max(self.h_dict.values()) == 3

    def is_three(self):
        return len(self.h_dict.keys()) == 3 and \
               max(self.h_dict.values()) == 3

    def is_two(self):
        return len(self.h_dict.keys()) == 3 and max(self.h_dict.values()) == 2

    def is_one(self):
        return len(self.h_dict.keys()) == 4

    def __eq__(self, other):
        return self.hand_string == other.hand_string

    def __lt__(self, other):
        if self.h_type == other.h_type:
            cards = {
                "A": 14,
                "K": 13,
                "Q": 12,
                #"J": 11,
                "T": 10,
                "9": 9,
                "8": 8,
                "7": 7,
                "6": 6,
                "5": 5,
                "4": 4,
                "3": 3,
                "2": 2,
                "J": 1
            }
            left = [cards[x] for x in self.hand_string]
            right = [cards[x] for x in other.hand_string]
            return left < right
        else:
            return self.h_type.value < other.h_type.value

    def __str__(self):
        return f" hand: {self.hand_string}, type: {self.h_type}"


def parse_input_and_solve(filename):
    file = open(filename)
    hands = []
    bids = []
    for line in file:
        hand, bid = line.split()
        hands.append(Hand(hand))
        bids.append(int(bid))

    ordered_hands = sorted(hands)
    #print(len(set([hand.hand_string for hand in hands])), len(hands))
    winnings = 0

    for i, hand in enumerate(ordered_hands):
        #print(i, hand.hand_string, hand.h_type, bids[hands.index(hand)])
        winnings += (i + 1) * bids[hands.index(hand)]

    print("winning", winnings)


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
