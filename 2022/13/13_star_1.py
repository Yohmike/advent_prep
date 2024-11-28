"""
https://adventofcode.com/2022/day/13

"""
from typing import List


def parse_signal(signal: str, index: int) -> [int, List[int]]:
    decoded_signal = []
    number = ""
    i = 0
    #print("called with ", index, signal)
    for i, char in enumerate(signal):
        #print("processing", i, char, decoded_signal)
        if i < index:
            #print("skipping", i, " until", index)
            continue
        else:
            if char == "[":
                index, new_list = parse_signal(signal, i + 1)
                decoded_signal.append(new_list)
            elif char == "]":
                if number != "":
                    decoded_signal.append(int(number))
                return i + 1, decoded_signal
            elif char == ",":
                if number != "":
                    decoded_signal.append(int(number))
                    number = ""
            else:
                number += char
    return i, decoded_signal


def compare(a, b):
    if type(a) == type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif type(a) == type(b) == list:
        n = len(a)
        m = len(b)
        res = 0
        for i in range(min(n, m)):
            res = compare(a[i], b[i])
            if res:
                break
        if res == 0:
            if n < m:
                return -1
            elif n > m:
                return 1
            else: return 0
    elif type(a) == int:
        res = compare([a], b)
    else:
        res = compare(a, [b])
    return res



def parse_input_and_solve(filename):
    file = open(filename)
    correct_signals = 0
    signals = []
    comparisons = 1
    for line in file:
        if line == "\n":
            if compare(signals[0], signals[1]) == -1:
                correct_signals += comparisons
                print("good ones:", signals, comparisons)
            signals = []
            comparisons += 1
        else:
            _, signal = parse_signal(list(line.strip("\n")), 0)
            #print("Decoded", signal)
            signals.append(signal)
    return correct_signals


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
