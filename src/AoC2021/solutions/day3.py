import numpy as np
from AoC2021.utils import get_input


def main():
    data = get_input("day3")
    one = part1(data)
    # two = part2(data)
    print(one)
    return one


def part1(data: list[str]):
    bits = np.array([list(map(int, datum)) for datum in data])
    gamma = "".join(bits.mean(0).round().astype(int).astype(str))
    return int(gamma, 2) * (2 ** len(gamma) - 1 - int(gamma, 2))


def part1_simple(data: list[str]):
    bits = [np.array(list(map(int, datum))) for datum in data]
    avg = sum(bits) / len(bits)
    bin_gamma = list(map(round, avg))  # [round(x) for x in avg]
    bin_epsilon = [1 - x for x in bin_gamma]
    gamma = int("".join(map(str, bin_gamma)), 2)
    epsilon = int("".join(map(str, bin_epsilon)), 2)
    return gamma * epsilon


def part2(data: list[str]):
    pass


if __name__ == "__main__":  # pragma no cover
    one = part1_simple(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )
    print(one)
    main()
