"""Tests for Day 2."""

import pytest

from solutions.day02.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 1227775554, 4174379265),
        (load_input(), 35367539282, 45814076230),
    ],
)
def test_day02_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
