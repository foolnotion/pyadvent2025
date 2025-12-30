"""Tests for Day 6."""

import pytest

from solutions.day06.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 4277556, 3263827),
        (load_input(), 4648618073226, 7329921182115),
    ],
)
def test_day06_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
