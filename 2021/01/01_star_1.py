"""
https://adventofcode.com/2021/day/1

"""


# The name of parse_input_and_solve suggests that it does two things, but it actually
# does three: it reads the file, parses the input, and solve. A slightly cleaner approach
# would be to let main parse the file, and let parse_input_and_solve operate on the resulting
# string (or stream): it then becomes a "pure" function, without any IO, that's easier to test.
def parse_input_and_solve(filename):
    file = open(filename)
    
    # your solution
    number_of_increases = -1
    previous_depth = 0
    for line in file:
        num = int(line)
        if num > previous_depth:
            number_of_increases += 1
        previous_depth = num
    return number_of_increases

    # There is a danger here: that's assuming that the depth can never be 0. We know this to
    # be true, so this works, but in a slightly-less constrained environment this could be a
    # problem. An easy way out is to use a flag:
    previous_depth = None
    number_of_increases = 0
    for line in file:
        num = int(line)
        if previous_depth is None or num > previous_depth:
            number_of_increases += 1
        previous_depth = num
    return number_of_increases

    # But if you can fit the whole file in memory, then there's a bunch of options now open to you:
    lines = file.readlines()

    # You could for instance validate the input first:
    numbers = list(map(int, lines))
    numbers = list(int(x) for x in lines)
    
    # And now you can choose to instead use indexing (not recommended, but still a
    # possibility: it avoids the flag value):
    number_of_increases = 0
    for i in range(1, len(numbers)):
        if depth[i] > depth[i-1]:
            number_of_increases += 1
    
    # Or you could choose to process the first element separately:
    # (this could also be done on the text stream with 'next', but that's a bit more clunky)
    if not numbers: return 0
    previous_depth = numbers[0]
    number_of_increases = 0
    for depth in numbers[1:]:
        pass # same stuff here
    
    # Or you could go full functional: that's fun, but less idiomatic in Python.
    number_of_increases = sum(int(b > a) for (a,b) in zip(numbers, numbers[1:]))
    
    # Overall I'd recommend your solution, with the explicit loop (that's the most idiomatic),
    # but using the None flag to avoid assuming that 0 is an invalid depth

def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    
    # You probably want to return 0; any non-0 value is interpreted to mean "something went wrong".
    return -1


if __name__ == "__main__":
    main()
