import pytest
from AoC2021.solutions.day4 import main, part1


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


def test_main():
    assert main() == 51776
