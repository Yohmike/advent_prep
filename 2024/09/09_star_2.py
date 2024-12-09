"""
https://adventofcode.com/2024/day/9

"""

from math import inf


def expand_blocks(blocks):
    display_blocks = []
    block_size = 0
    block_sizes = {}
    for i, block in enumerate(blocks):
        if i % 2 == 0:
            display_blocks.extend([block_size] * int(block))
            block_sizes[block_size] = int(block)
            block_size += 1

        else:
            display_blocks.extend(["."] * int(block))
    print(display_blocks, block_sizes)
    return display_blocks, block_sizes


def reorder_blocks(blocks, block_sizes):
    i = 0
    descending_key = max(block_sizes.keys())
    for key in range(descending_key, -1, -1):
        key_size = block_sizes[key]
        print(key)
        for i in range(0, len(blocks) - key_size):
            if blocks[i : i + key_size] == ["."] * key_size:
                key_index = blocks.index(key)
                if i > key_index:
                    break
                blocks[i : i + key_size], blocks[key_index : key_index + key_size] = (
                    blocks[key_index : key_index + key_size],
                    blocks[i : i + key_size],
                )
                break
    return blocks


def update_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block == ".":
            continue
        checksum += i * int(block)
    return checksum


def parse_input_and_solve(filename: str) -> int:
    update_count = 0
    with open(filename) as file:
        disk_blocks = file.readline().strip("\n")
        # print(disk_blocks)
        expanded_blocks, sizes = expand_blocks(disk_blocks)
        reordered_blocks = reorder_blocks(expanded_blocks, sizes)
        update_count = update_checksum(reordered_blocks)
    return update_count


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
