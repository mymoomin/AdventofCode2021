from AoC2021.solutions.day1 import main, part1, part2
from hypothesis import given
from hypothesis.strategies import lists, integers


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n")


demo_data = get_input("day1")


def test_part1():
    assert part1(demo_data) == 7


@given(lists(integers().map(str), min_size=1))
def fuzz_part1(data):
    count = part1(data)
    assert count >= 0
    assert count <= len(data) - 1


@given(lists(integers().map(str), min_size=3))
def fuzz_part2(data):
    count = part2(data)
    assert count >= 0
    assert count <= len(data) - 3


def test_part2():
    assert part2(demo_data) == 5


def test_main():
    assert main() == (1502, 1538)
