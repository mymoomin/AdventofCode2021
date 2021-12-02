from math import isnan, isclose
from AoC2021.utils import product, get_input
from hypothesis import given
from hypothesis.strategies import lists, floats
import pytest


def test_product():
    assert product([1, 2, 3, 4]) == 24


@given(lists(floats(), min_size=1))
def test_fuzz_product(vals):
    total = 1
    for val in vals:
        total *= val
    if isnan(total):
        assert isnan(product(vals))
    else:
        assert isclose(total, product(vals))


def test_get_input():
    prefix = "src/AoC2021/data/"
    with pytest.raises(FileNotFoundError):
        get_input("")

    with open(f"{prefix}/day1.txt", "r") as f:
        assert f.read().split("\n") == get_input("day1")

    assert get_input("newline") == ["150"]
