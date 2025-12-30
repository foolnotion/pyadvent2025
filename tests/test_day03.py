"""Tests for Day 3."""

import pytest

from solutions.day03.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 357, 3121910778619),
        (load_input(), 16927, 167384358365132),
    ],
)
def test_day03_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
