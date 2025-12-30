from functools import cache
from pathlib import Path

import numpy as np

EXAMPLE = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def solve(input_data):
    n, m = len(input_data), len(input_data[0])

    a = np.zeros((n, m), dtype=str)

    S = (0, 0)
    for i, line in enumerate(input_data):
        for j, x in enumerate(line):
            a[i, j] = x
            if x == "S":
                S = (i, j)

    graph = {}

    @cache
    def split(point, parent=None):
        i, j = point

        if parent and parent not in graph:
            graph[parent] = set()

        if a[i, j] == "^":
            if parent:
                graph[parent].add(point)

            if j - 1 >= 0:
                split((i, j - 1), point)

            if j + 1 < n:
                split((i, j + 1), point)

            return

        if i + 1 < n:
            split((i + 1, j), parent)

    split(S)

    @cache
    def total(node):
        return 1 + sum(total(c) for c in graph[node] if c in graph)

    p1 = len(graph)
    p2 = total(next(iter(graph))) + 1
    return p1, p2
