from AoC2021.solutions.day1 import main, part1, part2


def get_input(filename: str):
    with open(f"tests/data/{filename}.txt", "r") as f:
        return f.read().split("\n")


demo_data = get_input("day1")


def test_part1():
    assert part1(demo_data) == 7


def test_part2():
    assert part2(demo_data) == 5


def test_main():
    assert main() == (1502, 1538)
