from AoC2021.solutions.day3 import part1, part1_simple, part2, main
import pytest
from hypothesis import given
from hypothesis.strategies import lists, text, integers


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n")


demo_data = get_input("day3demo")


@pytest.mark.parametrize(
    "testinput,expected",
    [(demo_data, 198), (["1"], 0), (["10"], 2), (["100", "011", "011"], 12)],
)
def test_part1(testinput, expected):
    assert part1(testinput) == expected


@pytest.mark.parametrize(
    "testinput,expected",
    [(demo_data, 198), (["1"], 0), (["10"], 2), (["100", "011", "011"], 12)],
)
def test_part1_simple(testinput, expected):
    assert part1_simple(testinput) == expected


@given(
    integers(min_value=1, max_value=10).flatmap(
        lambda n: lists(text(alphabet="10", min_size=n, max_size=n), min_size=1)
    )
)
def test_part1_eq_part1_simple(data):
    assert part1(data) == part1_simple(data)


@pytest.mark.parametrize(
    "testinput,expected",
    [(demo_data, 230), (["1"], 1), (["10"], 4), (["100", "011", "010"], 12)],
)
def test_part2(testinput, expected):
    assert part2(testinput) == expected


def test_main():
    assert main() == (2724524, 2775870)
