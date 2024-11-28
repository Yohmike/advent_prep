from collections import namedtuple
import sys


def parse_input_first_star(filename):
    file = open(filename)
    current_time = int(file.readline())
    schedule = file.readline().split(',')
    bus_ids = [int(x) for x in schedule if x != "x"]
    BusDelay = namedtuple("BusDelay", ["bus_id", "delay_min"])
    bus_delays = [BusDelay(int(bus), i) for i, bus in enumerate(schedule) if bus != "x"]
    print(bus_delays)
    first_bus = max([x.bus_id for x in bus_delays])
    gen = infinite_sequence(first_bus)
    multiplier = bus_delays[0].bus_id
    current_time = multiplier * next(gen)
    how_far = 2

    while how_far < len(bus_delays) + 1:
        while not check_buses(bus_delays, current_time, how_far):
            current_time = bus_delays[0].bus_id * next(gen)
        multiplier = current_time - (bus_delays[how_far - 1].bus_id - bus_delays[how_far - 1].delay_min)
        print(current_time, multiplier)
        how_far += 1
        gen = infinite_sequence(first_bus)

    return current_time


def infinite_sequence(first_bus=None):
    if first_bus is not None:
        num = first_bus
    while True:
        yield num
        num += 1


def check_buses(buses, current_time, how_far):
    for bus in buses[:how_far]:
        if (current_time + bus.delay_min) % bus.bus_id != 0:
            return False
    return True


def main():
    input_file_name = "input"
    test_input_file_name = "small input"
    print("TEST:", parse_input_first_star(test_input_file_name))
    print("INPUT:", parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
