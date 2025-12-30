from pathlib import Path

from shapely import LineString, Point, Polygon

EXAMPLE = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

DIM = 2


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def area(a, b):
    dx = abs(a.x - b.x) + 1
    dy = abs(a.y - b.y) + 1
    return abs(dx) * abs(dy)


def solve(input_data):
    p1, p2 = 0, 0

    n = len(input_data)

    points = [Point(int(x) for x in line.split(",")) for line in input_data]
    p1, p2 = 0, 0

    poly = Polygon(points)

    for i in range(n - 1):
        a = points[i]

        for j in range(i + 1, n):
            b = points[j]
            r = area(a, b)

            p1 = max(p1, r)

            if r < p2:
                continue

            c = Point(a.x, b.y)
            d = Point(b.x, a.y)

            if poly.covers(LineString([a, b])) and poly.covers(LineString([c, d])):
                p2 = max(p2, r)

    return p1, p2
