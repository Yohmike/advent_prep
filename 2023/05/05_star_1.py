"""
https://adventofcode.com/2023/day/5

"""
from typing import Tuple, List, Dict
from math import prod
from dataclasses import dataclass

@dataclass
class Range:
    destination_start: int
    source_start: int
    range_length: int


@dataclass
class Map:
    name: str
    ranges: List[Range]

    def find_destination(self, source: int):
        for r in self.ranges:
            if r.source_start < source < r.source_start + r.range_length:
                return r.destination_start + source - r.source_start
        return source


def go_through_maps(seed: int, maps: Dict[str,Map])-> int:
    order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
             "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    for el in order:
        seed = maps[el].find_destination(seed)

    return seed

def parse_input_and_solve(filename):
    file = open(filename)
    seeds_line = file.readline()
    seeds = [int(x) for x in seeds_line.split(":")[-1].split()]
    maps = {}
    file.readline()
    for line in file:
        if "map" in line:
            map_name = line.split()[0]
            map = Map(map_name, [])
        elif line != "\n":
            line_range = Range(*[int(x) for x in line.split()])
            map.ranges.append(line_range)
        else:
            maps[map.name] = map
    maps[map.name] = map
    print(maps)
    locations = []
    for seed in seeds:
        locations.append(go_through_maps(seed, maps))

    print(min(locations))



def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
