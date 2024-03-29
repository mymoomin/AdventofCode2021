from AoC2021.solutions.day2 import main, part1, part2
import pytest


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n")


demo_data = get_input("day2demo")


def test_part1():
    assert part1(demo_data) == 150
    with pytest.raises(ValueError):
        part1(["back 3"])


def test_part2():
    assert part2(demo_data) == 900
    with pytest.raises(ValueError):
        part2(["back 3"])


def test_main():
    assert main() == (2036120, 2015547716)
