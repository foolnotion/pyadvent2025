"""Tests for Day 10."""

import pytest

from solutions.day10.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 7, 33),
        (load_input(), 444, 16513),
    ],
)
def test_day10_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
