from AoC2021.solutions.day4 import part1
import pytest


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n\n")


demo_data = get_input("day4demo")


@pytest.mark.parametrize(
    "testinput,expected",
    [(demo_data, 4512)],
)
def test_part1(testinput, expected):
    assert part1(testinput) == expected
