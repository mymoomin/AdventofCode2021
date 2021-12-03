from AoC2021.solutions.day3 import part1
import pytest


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n")


demo_data = get_input("day3demo")


@pytest.mark.parametrize("testinput,expected", [(demo_data, 198)])
def test_part1(testinput, expected):
    assert part1(testinput) == expected
