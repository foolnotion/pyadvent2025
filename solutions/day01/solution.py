from pathlib import Path

EXAMPLE = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

N = 100


def load_example():
    return EXAMPLE.split("\n")


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def apply_rotation(n, rot):
    """Returns current dial position and
    how many times it crossed zero
    """
    s = -1 if rot[0] == "L" else 1
    a = int(rot[1:])

    if a > N:
        x, z1, z2 = apply_rotation(n, str(rot[0] + str(a % N)))
        return x, z1, z2 + a // N

    # calculate new dial position
    m = (n + s * a) % N

    # part 1: figure out if I'm at zero
    p1 = int(m == 0)

    # part 2: calculate zero crossing
    # (only if I'm not already at zero)
    p2 = int(n != 0 and (m == 0 or m * s < n * s))

    return m, p1, p2


def solve(input_data):
    n, p1, p2 = 50, 0, 0

    for rot in input_data:
        n, z1, z2 = apply_rotation(n, rot)
        p1 += z1
        p2 += z2

    return p1, p2
