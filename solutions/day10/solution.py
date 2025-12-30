import sys
from pathlib import Path

from z3 import Int, Optimize, Sum, sat

EXAMPLE = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def load_example():
    return EXAMPLE.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def search_p1(config):
    goal = config[0]
    buttons = config[1]

    def toggle(c):
        return "." if c == "#" else "#"

    state = ["."] * len(goal)
    pressed = [False] * len(buttons)

    stack = []
    stack.append((0, state, pressed))

    seen = {}

    min_steps = sys.maxsize

    while stack:
        steps, state, pressed = stack.pop()

        if state == goal:
            min_steps = min(min_steps, steps)
            continue

        if steps >= min_steps:
            continue

        t = tuple(state)
        if t in seen and seen[t] <= steps:
            continue
        seen[t] = steps

        for i in range(len(buttons)):
            if pressed[i]:
                continue

            s = state.copy()
            p = pressed.copy()

            p[i] = True
            for j in buttons[i]:
                s[j] = toggle(s[j])

            stack.append((steps + 1, s, p))

    return min_steps


def search_p2(config):
    button = config[1]
    joltage = config[2]
    opt = Optimize()

    counts = [Int(f"c_{i}") for i in range(len(button))]
    for c in counts:
        opt.add(c >= 0)

    for i, v in enumerate(joltage):
        contributions = [counts[j] for j, b in enumerate(button) if i in b]
        opt.add(Sum(contributions) == v)

    opt.minimize(Sum(counts))
    if opt.check() == sat:
        model = opt.model()
        return sum(model[c].as_long() for c in counts)
    else:
        raise ValueError("solver failed")


def solve(lines):
    p1, p2 = 0, 0

    # lines = load_example()
    data = []
    for line in lines:
        parts = line.split()
        lights = [*parts[0][1:-1]]
        buttons = [[int(x) for x in part[1:-1].split(",")] for part in parts[1:-1]]
        counters = [int(x) for x in parts[-1][1:-1].split(",")]
        data.append((lights, buttons, counters))

    p1 = sum(search_p1(d) for d in data)
    p2 = sum(search_p2(d) for d in data)

    return p1, p2
