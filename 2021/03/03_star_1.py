"""
https://adventofcode.com/2021/day/3

"""


def parse_input_and_solve(filename):
    file = open(filename)
    sum_list = []
    small_number = ""
    big_number = ""
    got_length_sum = False
    last_el = 0
    for i, line in enumerate(file):

        binary_string_list = line
        # WARNING WARNING WARNING
        # THIS DOES NOT CREATE A COPY
        #
        # $ python
        # >>> words1 = ["my", "list", "of", "words"]
        # >>> words2 = words1
        # >>> words2.pop(0)
        # 'my'
        # >>> words1
        # ['list', 'of', 'words']
        #
        # modifying words2 changed words1, because words2 = words1 does not copy the list,
        # it copies the *underlying pointer*. Yes, Python decides whether to copy the value
        # or the pointer depending on the kind of value it is, and hides that from you, and
        # yes that's very annoying.
        #
        # In your case you're fine, since you're dealing with strings, and strings are
        # immutable; so the alias is not dangerous, just useless. :P
                
        if not got_length_sum:
            # here you're basically saying: I want to only do this on the first iteration
            # why not do it outside of the loop, to avoid having to use a flag?
            sum_list = [0 for _ in binary_string_list[:-1]]
            got_length_sum = True

        for j, el in enumerate(binary_string_list):
            if el == "1":
                sum_list[j] += 1
        last_el = i
    for el in sum_list:
        if el >= (last_el + 1) / 2:
            small_number += "0"
            big_number += "1"
        else:
            small_number += "1"
            big_number += "0"

    big = int(big_number.encode("ascii"), 2)
    small = int(small_number.encode("ascii"), 2)
    # not sure why you encode them, since they're already strings?
    # this works just fine
    big = int(big_number, 2)
    small = int(small_number, 2)
    
    return big, small


# So, a lot of your code is used to keep track of things like the number of bits,
# or to create an array on the first loop; there are several ways to do better.
# One way would be to use a dictionary from index to count; that's overkill,
# but it works. (you'd need to use sorted(count) to iterate in index order)
lines = file.readlines()
threshold = len(lines) / 2
count = {}
for line in lines:
    for i, el in enumerate(line[:-1]):
        if el == "1":
            count[i] = count.get(i, 0) + 1
        
# Another solution is to assume that the length of the first line is correct;
# granted, that's making an assumption, but that definitely makes the code easier.
# (we strip the whitespace from each line)
lines = list(line.rstrip() for line in file.readlines())
threshold = len(lines) / 2
count = [0 for _ in lines[0]]
for line in lines:
    for i, el in enumerate(line):
        if el == "1":
            count[i] += 1
        
# You could go even further, and make count ONE OF THE LINES.
# (we strip the whitespace from each line, but with a map ^^)
lines = list(map(str.rstrip, file.readlines()))
threshold = len(lines) / 2
count = list(map(int, lines.pop()))
for line in lines:
    for i, el in enumerate(line):
        if el == "1":
            count[i] += 1

# And, of course, you could define it in a more functional way:
lines = file.readlines()
threshold = len(lines) / 2
count = list(sum(int(line[i]) for line in lines) for i in range(len(line[0])-1))

# As for the computation of the results, your solution of crafting a string works;
# but you could also just use numbers directly:
big = 0
small = 0
for x in count:
    bit = int(x > threshold)
    big = 2 * big + bit
    small = 2 * small + (1 - bit)



def main():
    print()
    input_file_name = "../input"
    big, small = parse_input_and_solve(input_file_name)
    print(f"Final score is: {big*small}")
    return big * small


if __name__ == "__main__":
    main()
