from functools import reduce
from itertools import groupby
from pathlib import Path

import numpy as np

EXAMPLE = """\
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""


OPS = {
    "+": np.sum,
    "*": np.prod,
}


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(input):
    n, m = len(input), len(input[0].split())
    a = np.zeros((n - 1, m), dtype=np.int32)
    for i, line in enumerate(input[:-1]):
        a[i, :] = [int(x) for x in line.split()]
    return sum(OPS[op](a[:, i]) for i, op in enumerate(input[-1].split()))


def part2(input):
    n = len(input)
    m = max(len(line) for line in input)

    # initialize a string matrix in numpy
    a = np.zeros((n - 1, m), dtype=str)
    for i, line in enumerate(input[:-1]):
        for j in range(len(line)):
            a[i, j] = line[j]

    # concatenate along the columns and strip extra spaces
    nums = reduce(np.char.add, [a[i, :] for i in range(n - 1)])
    nums = [x.strip() for x in nums]

    # group by empty string which is the digit group separator
    return sum(
        OPS[op](batch)
        for op, batch in zip(
            input[-1].split(),
            (list(map(int, g)) for k, g in groupby(nums, key=bool) if k),
            strict=True,
        )
    )


def solve(input_data):
    p1 = part1(input_data)
    p2 = part2(input_data)
    return p1, p2
