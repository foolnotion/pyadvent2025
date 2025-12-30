from itertools import takewhile
from pathlib import Path

EXAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, x):
        return x >= self.a and x <= self.b

    def __repr__(self):
        return f"[{self.a}-{self.b}]"

    def __lt__(self, other):
        return self.a < other.a

    def __len__(self):
        return self.b - self.a + 1

    def overlaps_with(self, other):
        return other.a in self or other.b in self

    def merge_with(self, other):
        # assert self.overlaps_with(other)
        a, b = self.a, self.b
        c, d = other.a, other.b
        self.a = min(a, c)
        self.b = max(b, d)


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def solve(input_data):
    def make_range(line):
        return Interval(*(int(x) for x in line.split("-")))

    ranges = [make_range(x) for x in takewhile(lambda x: x, input_data)]
    ranges.sort()

    ingredients = [
        int(x) for x in takewhile(lambda x: x, input_data[len(ranges) + 1 :])
    ]

    def fresh(x):
        return any(x in range for range in ranges)

    p1 = sum(fresh(x) for x in ingredients)

    s = set(ranges)
    for i, u in enumerate(ranges):
        if u not in s:
            continue

        for v in ranges[i + 1 :]:
            if v in s and u.overlaps_with(v):
                u.merge_with(v)
                s.remove(v)

    p2 = sum(len(x) for x in s)
    return p1, p2
