"""
https://adventofcode.com/2024/day/21

"""

from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


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


def generate_secret(start, times=2000):
    next = start
    for _ in range(times):
        next = compute_secret(next)
    return next


@timing
def parse_input_and_solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        secret_sum = 0
        for line in lines:
            secret = generate_secret(int(line.strip("\n")))
            secret_sum += secret

        return secret_sum


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
