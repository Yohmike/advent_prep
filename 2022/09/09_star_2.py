"""
https://adventofcode.com/2022/day/9

"""
from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int


def update_tail_position(head, tail):
    #print(head, tail)
    x = 0
    y = 0
    if abs(head.x - tail.x) < 2 and abs(head.y - tail.y) < 2:
        #print("Nothing to do")
        return None
    elif abs(head.x - tail.x) >= 3 or abs(head.y - tail.y) >= 3:
        #print("ERROR")
        return "Error"
    elif abs(head.x - tail.x) == 2 and head.y == tail.y:
        x = tail.x - 1 if head.x < tail.x else tail.x + 1
        y = tail.y
    elif abs(head.y - tail.y) == 2 and head.x == tail.x:
        y = tail.y - 1 if head.y < tail.y else tail.y + 1
        x = tail.x
    elif head.x > tail.x and head.y > tail.y:
        x = tail.x + 1
        y = tail.y + 1
    elif head.x < tail.x and head.y < tail.y:
        x = tail.x - 1
        y = tail.y - 1
    elif head.x > tail.x and head.y < tail.y:
        x = tail.x + 1
        y = tail.y - 1
    elif head.x < tail.x and head.y > tail.y:
        x = tail.x - 1
        y = tail.y + 1
    tail.x = x
    tail.y = y
    coords = f"{x}_{y}"
    #print(coords)
    return coords


def parse_instruction(instruction, step, knots):
    pos = []
    #print(instruction, step, head, tail)
    if instruction == "U":
        while step > 0:
            step -=1
            knots[0].x += 1

            for i, knot in enumerate(knots[:-1], 1):
                new_pos = update_tail_position(knot, knots[i])
                if i == 9 and new_pos is not None:
                    pos.append(new_pos)
    if instruction == "D":
        while step > 0:
            step -= 1
            knots[0].x -= 1
            for i, knot in enumerate(knots[:-1], 1):

                new_pos = update_tail_position(knot, knots[i])
                if i == 9 and new_pos is not None:
                    pos.append(new_pos)
    if instruction == "L":
        while step > 0:
            step -=1
            knots[0].y -= 1
            for i, knot in enumerate(knots[:-1], 1):

                new_pos = update_tail_position(knot, knots[i])
                if i == 9 and new_pos is not None:
                    pos.append(new_pos)
    if instruction == "R":
        while step > 0:
            step -=1
            knots[0].y += 1
            for i, knot in enumerate(knots[:-1], 1):
                #print(i, knot, knots[i])
                new_pos = update_tail_position(knot, knots[i])
                if i == 9 and new_pos is not None:
                    pos.append(new_pos)
    #print(pos)
    return pos


def parse_input_and_solve(filename):
    file = open(filename)
    positions = {}
    head = Position(0, 0)
    tail = Position(0, 0)
    knots = [Position(0, 0) for _ in range(0,10)]
    #print(knots)
    for line in file:
        instruction, steps = line.strip("\n").split(" ")
        #print(instruction, steps)
        steps = int(steps)
        new_positions = parse_instruction(instruction, steps, knots)
        for position in new_positions:
            positions[position] = 1
    #print(positions)
    return len(positions.keys()) + 1


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
