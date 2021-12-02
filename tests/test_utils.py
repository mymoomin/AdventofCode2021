from AoC2021.utils import prod, get_input
from hypothesis import given
from hypothesis.strategies import lists, floats
import pytest


def test_prod():
    assert prod([1, 2, 3, 4]) == 24


@given(lists(floats(), min_size=1))
def fuzz_prod(vals):
    total = 1
    for val in vals:
        total *= val
    assert total == prod(vals)


def test_get_input():
    prefix = "src/AoC2021/data/"
    with pytest.raises(FileNotFoundError):
        get_input("")

    with open(f"{prefix}/day1.txt", "r") as f:
        assert f.read().split("\n") == get_input("day1")

    assert get_input("newline") == ["150"]
