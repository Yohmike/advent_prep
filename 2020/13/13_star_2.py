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
    gen = infinite_sequence()
    current_time = bus_delays[0].bus_id * next(gen)
    while not check_buses(bus_delays, current_time):
        current_time = bus_delays[0].bus_id * next(gen)

    print(current_time)


def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


def check_buses(buses, current_time):
    for bus in buses:
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
