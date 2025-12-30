from pathlib import Path

import numpy as np

EXAMPLE = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def solve(input_data):
    n = len(input_data[0])
    a = np.zeros(shape=(n, n), dtype=np.int8)
    for i, line in enumerate(input_data):
        a[i, :] = [1 if c == "@" else 0 for c in line]

    def can_remove(i, j):
        c = 0
        for x in (i - 1, i, i + 1):
            if x < 0 or x >= n:
                continue

            for y in (j - 1, j, j + 1):
                if y < 0 or y >= n:
                    continue

                if x == i and y == j:
                    continue

                c += a[x, y] != 0
                if c >= 4:
                    return False

        return True

    def remove_rolls(p2: bool) -> int:
        removed = 0
        for i in range(n):
            for j in range(n):
                if a[i, j] == 0:
                    continue

                if can_remove(i, j):
                    removed += 1
                    if p2:
                        a[i, j] = 0

        return removed

    p1 = remove_rolls(False)
    p2 = sum(iter(lambda: remove_rolls(True), 0))

    return p1, p2
