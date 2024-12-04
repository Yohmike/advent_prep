def parse_input_and_solve(filename):
    number_of_increases = 0
    sliding_window = []
    file = open(filename)
    for line in file:
        num = int(line)
        if len(sliding_window) < 3:
            sliding_window.append(num)
            continue
        else:
            sliding_window.append(num)
            # print(sliding_window)
            # print(sliding_window[:3])
            # print(sliding_window[1:])
            if sum(sliding_window[:3]) < sum(sliding_window[1:]):
                number_of_increases += 1

        if len(sliding_window) >= 3:
            sliding_window.pop(0)
    return number_of_increases



# (Same comments as for part 1 re. opening the file in main.)
#
# There's a trick you can use here:
#
# previous window: [a, b, c]
# current window:     [b, c, d]
#
# current window > previous window <=> d > a
#
# So you don't need to keep the sliding window!
depths = map(int, file.readlines())
number_of_increases = 0
for i in range(3, len(depths)):
    if depths[i] > depths[i-3]:
        number_of_increases += 1 
        
# if you want to keep it, then, a few suggestions:
#   - you don't need to append in both branches of the if;
#   - you don't need to re-test for length before popping
sliding_window = []
for line in file:
    num = int(line)
    old_sum = sum(sliding_window)
    sliding_window.append(num)
    if len(sliding_window) < 3:
        continue
    sliding_window.pop(0)
    new_sum = sum(sliding_window)
    if new_sum > old_sum:
        number_of_increases += 1
        
# if you want to keep it but only perform the minimal test:
sliding_window = []
for line in file:
    num = int(line)
    sliding_window.append(num)
    if len(sliding_window) < 3:
        continue
    old = sliding_window.pop(0)
    if num > old:
        number_of_increases += 1



def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1

if __name__ == "__main__":
    main()
