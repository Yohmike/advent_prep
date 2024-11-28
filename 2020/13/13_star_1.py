from collections import namedtuple
import sys


def parse_input_first_star(filename):
    file = open(filename)
    current_time = int(file.readline())
    schedule = file.readline().split(',')
    bus_ids = [int(x) for x in schedule if x != "x"]
    # print(current_time)
    # print(schedule)
    # print(bus_ids)
    BusDeparture = namedtuple("BusDeparture", ["bus_id", "minutes_to_departure"])
    departure_buses = []
    min_bus = BusDeparture(-1, sys.maxsize)
    for bus in bus_ids:
        departure_time = bus - current_time % bus
        bus_departure = BusDeparture(bus, departure_time)
        if departure_time < min_bus.minutes_to_departure:
            min_bus = bus_departure
        departure_buses.append(bus_departure)
        # print(f"Bus {bus} departs in {departure_time} minutes")
    return min_bus.bus_id * min_bus.minutes_to_departure


def main():
    input_file_name = "input"
    test_input_file_name = "small input"
    print("TEST:", parse_input_first_star(test_input_file_name))
    print("INPUT:", parse_input_first_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
