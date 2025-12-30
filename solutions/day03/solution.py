from pathlib import Path

import numpy as np

EXAMPLE = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def joltage(bank, n_digits):
    indices = np.argsort([-int(x) for x in bank], stable=True)
    bank_size = len(bank)

    def valid_index(current_index, last_index, n_filled):
        digits_needed = n_digits - n_filled
        digits_left = bank_size - current_index
        return current_index > last_index and digits_left >= digits_needed

    value = 0
    last_index = -1  # index of the last filled digit

    for n in range(n_digits):
        current_index = next(x for x in indices if valid_index(x, last_index, n))
        value = 10 * value + int(bank[current_index])
        last_index = current_index

    return value


def solve(input_data):
    p1, p2 = 0, 0

    for line in input_data:
        p1 += joltage(line, 2)
        p2 += joltage(line, 12)

    return p1, p2
