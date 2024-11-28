"""
https://adventofcode.com/2023/day/5

"""
from typing import Tuple, List, Dict
from math import prod
from dataclasses import dataclass

@dataclass
class Range:
    s_start: int
    length: int

    def intersect(self, other):
        overlap = Range(0,0)
        intact = [self]
        if other.s_start + other.length < self.s_start or other.s_start > self.s_start + self.length:
            return overlap, intact
        elif other.s_start < self.s_start:
            if other.s_start + other.length <= self.s_start + self.length:
                common_size = other.s_start + other.length - self.s_start
                overlap = Range(self.s_start, common_size)
                intact = [Range(other.s_start + other.length, self.length - common_size)]
            else:
                overlap = self
                intact = []
        elif other.s_start >= self.s_start:
            if other.s_start + other.length < self.s_start + self.length:
                overlap = other
                intact = [
                    Range(self.s_start, other.s_start - self.s_start),
                    Range(other.s_start + other.length, self.s_start + self.length - other.s_start - other.length)
                ]
            else:
                common_size = self.s_start + self.length - other.s_start
                overlap = Range(other.s_start, common_size)
                intact = Range(self.s_start, self.length - common_size)
        return overlap, intact

@dataclass
class Map:
    name: str
    ranges: Dict[int, Range]


def get_overlapping_ranges(maps):
    ranges = {}
    for k in list(maps.keys())[::-1]:
        current_map = maps[k]
        if not ranges:
            for el, r in current_map.ranges.items():
                if r.s_start < el:
                    ranges[el] = Range(el, r.length)
        else:
            for r in ranges:
                #TODO: update the overlapping intervals.
                pass


def parse_input_and_solve(filename):
    file = open(filename)
    seeds_line = file.readline()
    seeds = [int(x) for x in seeds_line.split(":")[-1].split()]
    maps = {}
    file.readline()
    for line in file:
        if "map" in line:
            map_name = line.split()[0]
            map = Map(map_name, {})
        elif line != "\n":
            dest, source, length = [int(x) for x in line.split()]
            line_range = Range(source, length)
            map.ranges[dest] = line_range
        else:
            maps[map.name] = map
    maps[map.name] = map
    overlapping = get_overlapping_ranges(maps)
    print(maps)
    print()


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
