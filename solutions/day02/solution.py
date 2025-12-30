from pathlib import Path

EXAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"  # noqa: E501


def load_example():
    return EXAMPLE.strip().split(",")


def load_input(path: str = Path(__file__).parent / "input.txt") -> str:
    with open(path) as f:
        return f.read().splitlines()[0].strip().split(",")


def valid_p1(id):
    n = len(id) // 2
    return id[:n] != id[n:]


def valid_p2(id):
    n = len(id)

    def invalid(c):
        return id[:c] * (n // c) == id

    return not any(invalid(c) for c in range(1, n))


def check_range(r, valid):
    a, b = r.split("-")
    s = 0
    for n in range(int(a), int(b) + 1):
        if not valid(str(n)):
            s += n

    return s


def solve(input_data):
    p1 = sum(check_range(r, valid_p1) for r in input_data)
    p2 = sum(check_range(r, valid_p2) for r in input_data)
    return p1, p2
