"""Tests for Day 12."""

import pytest

from solutions.day12.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 2, 0),
        (load_input(), 479, 0),
    ],
)
def test_day12_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
