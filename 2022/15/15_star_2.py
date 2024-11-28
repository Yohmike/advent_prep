"""
https://adventofcode.com/2022/day/15

"""
from typing import List
from dataclasses import dataclass
from math import inf
@dataclass
class Point:
    x: int
    y: int

@dataclass
class SensorRadius:
    coord: Point
    radius: int


def manhattan_distance(source: Point, destination: Point) -> int:
    return abs(source.x - destination.x) + abs(source.y - destination.y)


def compute_strip(sensor: SensorRadius, y: int) -> (int,int):
    strip = 0
    top = sensor.coord.y - sensor.radius
    bottom = sensor.coord.y + sensor.radius
    #print(sensor, y, top , bottom)

    if top <= y <= sensor.coord.y:
        strip = sensor.radius - (sensor.coord.y - y)
    if sensor.coord.y <= y <= bottom:
        strip = sensor.radius - (y - sensor.coord.y)
    #print(strip)
    if bottom == y or top == y:
        return sensor.coord.x, sensor.coord.x
    elif strip == 0:
        return None
    return sensor.coord.x - strip, sensor.coord.x + strip


def concat_intervals(intervals: List[int]) -> int:
    length = 0
    gap = (0, 0)
    intervals = sorted(intervals, key=lambda z: z[0])
    max = intervals[0][1]
    min = intervals[0][0]
    for interval in intervals[1:]:
        #print(interval, min, max, length)
        x, y = interval
        if x < min and y < min:
            #print("left")
            continue
        if x <= min <= y <= max:
            #print("intersect left")
            min = x
        if min <= x <= max and min <= y <= max:
            #print("middle")
            continue
        if min <= x <= max <= y:
            #print("intersect_right")
            max = y
        if max < x and min < y:
            #print("right")
            gap = (max, x)
            length += max - min
            min = x
            max = y
    length += max - min
    return length, gap


def get_sensor_and_beacon(line: str) -> (Point, Point):
    sensor_beacon_parts = [x.strip(",:") for x in line.split(" ") if "=" in x]
    sensor = [int(x.split("=")[1]) for x in sensor_beacon_parts[:2]]
    beacon = [int(x.split("=")[1]) for x in sensor_beacon_parts[2:]]
    sensor_point = Point(*sensor)
    beacon_point = Point(*beacon)
    return sensor_point, beacon_point


def parse_input_and_solve(filename):
    file = open(filename)
    sensors = []
    for line in file:
        sensor, beacon = get_sensor_and_beacon(line.strip("\n"))
        sensors.append(SensorRadius(sensor, manhattan_distance(sensor, beacon)))
    # print(sensors)
    for y in range(0, 4000000):
        if y % 1000 == 0:
            print("Step: ", y)
        intervals = [compute_strip(sensor, y) for sensor in sensors]
        intervals = [x for x in intervals if x is not None]
        #print(intervals)
        length, gap = concat_intervals(intervals)
        if gap[1] - gap[0] == 2:
            return 4000000 * (gap[0] + 1) + y


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
