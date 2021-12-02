"""Day 1: Sonar Sweep https://adventofcode.com/2021/day/1"""

from AoC2021.utils import get_input


def main():
    data = get_input("day1")
    one = part1(data)
    two = part2(data)
    print(one, two)
    return (one, two)


def part1(data: list[str]):
    """Counts the number of times a depth measurement
    increases from the previous measurement

    :param data: list of depths as strings
    :return: number of increases
    """
    depths = list(map(int, data))
    last = depths[0]
    counter = 0

    for depth in depths:
        if depth > last:
            counter += 1
        last = depth

    return counter


def part2(data: list[str]):
    """Counts the number of times the sum of the last
    3 depth measurements increases

    :param data: list of depths as strings
    :return: number of increases"""
    depths = list(map(int, data))
    counter = 0
    last = sum(depths[0:3])

    for i in range(2, len(depths)):
        window_depth = sum(depths[i - 2 : i + 1])
        if window_depth > last:
            counter += 1
        last = window_depth

    return counter


if __name__ == "__main__":  # pragma: no cover
    main()
