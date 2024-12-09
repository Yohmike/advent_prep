"""
https://adventofcode.com/2024/day/9

"""


def expand_blocks(blocks):
    display_blocks = []
    block_size = 0
    for i, block in enumerate(blocks):
        if i % 2 == 0:
            display_blocks.extend([block_size] * int(block))
            block_size += 1
        else:
            display_blocks.extend(["."] * int(block))
    # print(display_blocks)
    return display_blocks


def reorder_blocks(blocks):
    i = 0
    j = len(blocks) - 1
    while i < j:
        if blocks[i] == ".":
            while blocks[j] == ".":
                j -= 1
                if j <= i + 1:
                    break
            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1
        else:
            i += 1
    # print(blocks)
    return blocks


def update_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block == ".":
            break
        checksum += i * int(block)
    return checksum


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    with open(filename) as file:
        disk_blocks = file.readline().strip("\n")
        # print(disk_blocks)
        expanded_blocks = expand_blocks(disk_blocks)
        reordered_blocks = reorder_blocks(expanded_blocks)
        update_count = update_checksum(reordered_blocks)
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
