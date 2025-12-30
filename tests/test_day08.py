"""Tests for Day 8."""

import pytest

from solutions.day08.solution import load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_input(), 129564, 42047840),
    ],
)
def test_day08_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
