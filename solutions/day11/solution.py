from collections import defaultdict
from functools import cache
from pathlib import Path

EXAMPLE_P1 = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

EXAMPLE_P2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def load_example_p1():
    return EXAMPLE_P1.splitlines()


def load_example_p2():
    return EXAMPLE_P2.splitlines()


def load_input(path: str = Path(__file__).parent / "input.txt") -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def solve(lines):
    nodes = defaultdict(list[str])
    for line in lines:
        parts = line.split(":")
        node = parts[0]
        outs = parts[1].split()
        nodes[node] = outs

    @cache
    def count_paths(node, dac=True, fft=True):
        if node == "out" and dac and fft:
            return 1

        return sum(
            count_paths(n, dac or (node == "dac"), fft or (node == "fft"))
            for n in nodes[node]
        )

    p1 = count_paths("you")
    p2 = count_paths("svr", dac=False, fft=False)
    return p1, p2
