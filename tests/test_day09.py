"""Tests for Day 9."""

import pytest

from solutions.day09.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 50, 24),
        (load_input(), 4755064176, 1613305596),
    ],
)
def test_day09_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
