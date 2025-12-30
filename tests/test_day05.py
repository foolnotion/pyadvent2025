"""Tests for Day 5."""

import pytest

from solutions.day05.solution import load_example, load_input, solve


@pytest.mark.parametrize(
    "testdata",
    [
        (load_example(), 3, 14),
        (load_input(), 720, 357608232770687),
    ],
)
def test_day05_solution(testdata) -> None:
    data, e1, e2 = testdata
    p1, p2 = solve(data)
    assert p1 == e1
    assert p2 == e2
