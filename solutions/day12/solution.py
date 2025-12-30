from pathlib import Path

import numpy as np
import numpy.ma as ma

EXAMPLE = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

PRESENT_SHAPE = (3, 3)
NUM_PRESENTS = 6


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def parse_input(lines):
    it = iter(lines)

    presents = {}
    regions = []

    while it:
        if len(presents) < NUM_PRESENTS:
            i = int(next(it)[:1])
            a = [[x == "#" for x in next(it)] for j in range(3)]
            m = ma.make_mask(a)
            presents[i] = [m, np.rot90(m, 1), np.rot90(m, 2), np.rot90(m, 3)]
            next(it)  # skip empty line

        else:
            try:
                line = next(it)
                parts = line.split(":")
                regions.append(
                    (
                        tuple(int(x) for x in parts[0].split("x")),
                        [int(x) for x in parts[1].split()],
                    )
                )
            except StopIteration:
                break

    return presents, regions


def can_fit_presents(presents, target):
    shape, counts = target
    rows, cols = shape
    pw, ph = PRESENT_SHAPE

    # first check if prefectly compacted presents still don't have enough area
    required_area = sum(
        count * np.sum(presents[index][0]) for index, count in enumerate(counts)
    )
    available_area = rows * cols
    if required_area > available_area:
        return 0

    # check if presents placed as loosely as possible will fit anyway
    total_presents = sum(counts)
    if total_presents * pw * ph <= rows * cols:
        return 1

    region = np.zeros(shape, dtype=np.uint8)

    def can_fit_present(present, region, i, j) -> int:
        rw, rh = region.shape

        # check if the present would fit at the coordinates
        if not (i + pw <= rw and j + ph <= rh):
            return 0

        r = region[i : i + pw, j : j + ph]

        # check if the present can be placed in that region
        if not (np.sum(r[present]) == 0):
            return 0

        r[present] = 1
        return 1

    # iterate over the counts and try to fit presents
    for index in range(len(counts)):
        if counts[index] == 0:
            continue

        # get an iterator to the target region
        it = np.nditer(region, flags=["multi_index"])
        for _ in (x for x in it if not x):
            i, j = it.multi_index
            counts[index] -= any(
                can_fit_present(rot, region, i, j) for rot in presents[index]
            )

            if counts[index] == 0:
                break

    return np.sum(counts) == 0


def solve(lines):
    presents, regions = parse_input(lines)
    return sum(can_fit_presents(presents, target) for target in regions), 0
