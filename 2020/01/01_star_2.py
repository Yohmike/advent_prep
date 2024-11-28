

def parse_input_second_star(filename):
    intended_sum = 2020
    sum_doubles = []
    inputs = []
    file = open(filename)
    for line in file:
        num = int(line)
        if len(inputs) > 1:
            sum_with_previous_inputs_list = [(intended_sum - (num + x), num, x) for x in inputs if num + x < intended_sum]
            sum_doubles.extend(sum_with_previous_inputs_list)
        inputs.append(num)
    for pair in sum_doubles:
        third, first, second = pair
        if third in inputs:
            return first * second * third, first, second , third
    return -1


def main():
    input_file_name = "input"
    print(parse_input_second_star(input_file_name))
    return -1


if __name__ == '__main__':
    main()
