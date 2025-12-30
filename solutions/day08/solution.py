from math import prod, sqrt
from pathlib import Path

EXAMPLE = """\
117,168,530
162,817,812
216,146,977
346,949,466
352,342,300
425,690,689
431,825,988
466,668,158
52,470,668
542,29,236
57,618,57
592,479,940
739,650,466
805,96,715
819,987,18
862,61,35
906,360,560
941,993,340
970,615,88
984,92,344
"""


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return sqrt(x * x + y * y + z * z)


def sort_by_distance(points):
    n = len(points)
    distances = [
        (distance(points[i], points[j]), (i, j))
        for i in range(n - 1)
        for j in range(i + 1, n)
    ]
    return [p for _, p in sorted(distances)]


def solve(lines):
    n = len(lines)
    circuits = [{i} for i in range(n)]

    points = [tuple(int(x) for x in line.split(",")) for line in lines]
    pairs = sort_by_distance(points)

    def connected(i, j):
        return i in circuits[j] and j in circuits[i]

    def top3_product():
        unique_circuits = {len(x) for x in circuits if x}
        top3 = sorted(unique_circuits, key=lambda x: -x)[:3]
        return prod(x for x in top3)

    p1, p2 = 0, 0

    for k, p in enumerate(pairs):
        i, j = p

        if j in circuits[i]:
            continue

        if k == 1000:
            p1 = top3_product()

        p2 = points[i][0] * points[j][0]

        # connect circuits
        s = circuits[i] | circuits[j]
        for k in s:
            circuits[k] = s

    return p1, p2
