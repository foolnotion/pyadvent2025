"""Tests for Day 11."""

import pytest

from solutions.day11.solution import load_example_p1, load_example_p2, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example_p1(), 5, 0),
        (load_example_p2(), 0, 2),
        (load_input(), 683, 533996779677200),
    ],
)
def test_day11_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
