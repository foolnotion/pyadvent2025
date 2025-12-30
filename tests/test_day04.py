"""Tests for Day 4."""

import pytest

from solutions.day04.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 13, 43),
        (load_input(), 1602, 9518),
    ],
)
def test_day04_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
