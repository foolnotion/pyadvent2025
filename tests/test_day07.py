"""Tests for Day 7."""

import pytest

from solutions.day07.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 21, 40),
        (load_input(), 1602, 135656430050438),
    ],
)
def test_day07_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
