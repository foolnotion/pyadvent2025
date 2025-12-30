"""Tests for Day 1."""

import pytest

from solutions.day01.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 3, 6),
        (load_input(), 1074, 6254),
    ],
)
def test_day01_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
