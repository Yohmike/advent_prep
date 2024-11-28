"""
https://adventofcode.com/2022/day/16

"""
import re
import itertools
from typing import List, Any
from dataclasses import dataclass


@dataclass
class Valve:
    name: str
    rate: int
    neighbors: List[str]


def get_valve(line: str) -> Valve:
    bits = line.strip("\n").split(" ")
    name = bits[1]
    rate = int(bits[4].strip(";").split("=")[-1])
    neighbors = [bit.strip(",") for bit in bits[9:]]
    return Valve(name=name, rate=rate, neighbors=neighbors)


def parse_input_and_solve(filename):
    valves = []
    with open(filename) as file:
        for line in file:
            valves.append(get_valve(line))
    print(valves)
    return

def read_puzzle(file):
    with open(file) as f:
        return [re.findall('[A-Z]+|\d+', line[1:]) for line in f.readlines()]

def solve(puzzle):
    graph = {valve:leads for valve, _, *leads in puzzle}
    print(graph)
    flows = {valve: int(flow) for valve, flow, *_ in puzzle if flow != '0'}
    print(flows)
    indicies = {valve: 1 << i for i, valve in enumerate(flows)}
    print(indicies)
    distances = {(v,l): 1 if l in graph[v] else 1000 for l in graph for v in graph}
    print(distances)

    # floyd-warshall = Distance for any possible pair of valves
    for k, i, j in itertools.permutations(graph, 3):
        #print(k, i, j)
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])
    print(distances)


    def visit(valve, minutes, bitmask, pressure, answer, iteration = 0):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        print(valve, minutes, iteration)
        iteration += 1
        for valve2, flow in flows.items():
            remaining_minutes = minutes - distances[valve, valve2] - 1
            if indicies[valve2] & bitmask or remaining_minutes <= 0: continue
            visit(valve2, remaining_minutes, bitmask|indicies[valve2], pressure + flow * remaining_minutes, answer, iteration)
        return answer


    part1     = max(visit('AA', 30, 0, 0, {}).values())
    visited2  = visit('AA', 26, 0, 0, {})
    part2     = max(v1+v2 for bitm1, v1 in visited2.items()
                    for bitm2, v2 in visited2.items() if not bitm1 & bitm2)

    return part1, part2

def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    puzzle = read_puzzle(input_file_name)
    print(solve(puzzle))
    return -1


if __name__ == "__main__":
    main()
