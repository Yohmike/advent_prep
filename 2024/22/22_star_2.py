"""
https://adventofcode.com/2024/day/21

"""

from collections import defaultdict


def mix_prune(secret, value):
    return (secret ^ value) % 16777216


def compute_secret(original):
    mul_secret = original * 64
    prune = mix_prune(mul_secret, original)
    div_secret = prune // 32
    prune = mix_prune(div_secret, prune)
    mul_secret = prune * 2048
    prune = mix_prune(mul_secret, prune)

    return prune


def generate_secret_sequences(start, times=2000):
    next = start

    secrets = [start % 10]
    price_sequences = {}

    for i in range(times):
        prev = secrets.pop()
        next = compute_secret(next)
        last_digit = next % 10
        secrets.append(last_digit - prev)
        if i >= 3:
            str_seq = ",".join([str(x) for x in secrets[i - 3 : i + 1]])
            if price_sequences.get(str_seq) is None:
                price_sequences[str_seq] = last_digit
        secrets.append(last_digit)

    return price_sequences


def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        secret_sum = 0
        secrets = defaultdict(int)
        for line in lines:
            new_secrets = generate_secret_sequences(int(line.strip("\n")))
            for k, v in new_secrets.items():
                secrets[k] += v

        max_index = max(secrets, key=secrets.get)
        secret_sum = secrets[max_index]

        return secret_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
