import numpy as np
import numpy.typing as npt
from AoC2021.utils import get_input
from typing import cast


def main():
    data = get_input("day3")
    one = part1(data)
    two = part2(data)
    print(one, two)
    return (one, two)


def part1(data: list[str]):
    bits = np.array([list(map(int, datum)) for datum in data])
    gamma = "".join(bits.mean(0).round().astype(int).astype(str))
    return int(gamma, 2) * (2 ** len(gamma) - 1 - int(gamma, 2))


def part1_simple(data: list[str]):
    bits = [np.array(list(map(int, datum))) for datum in data]
    avg = cast(npt.NDArray[np.float64], sum(bits) / len(bits))
    bin_gamma = list(map(round, avg))  # [round(x) for x in avg]
    bin_epsilon = [1 - x for x in bin_gamma]
    gamma = int("".join(map(str, bin_gamma)), 2)
    epsilon = int("".join(map(str, bin_epsilon)), 2)
    return gamma * epsilon


def part2(data: list[str]):
    bits = np.array([list(map(int, datum)) for datum in data])
    oxs = bits.copy()

    i = 0
    while len(oxs) > 1:
        most_common = np.round(np.nextafter(oxs.mean(0), np.inf))[i]
        oxs = oxs[oxs[:, i] == most_common]
        i += 1
    bin_ox = "".join(oxs[0].astype(int).astype(str))

    cos = bits.copy()

    i = 0
    while len(cos) > 1:
        most_common = np.round(np.nextafter(cos.mean(0), np.inf))[i]
        cos = cos[cos[:, i] != most_common]
        i += 1
    bin_co = "".join(cos[0].astype(int).astype(str))
    return int(bin_ox, 2) * int(bin_co, 2)


if __name__ == "__main__":  # pragma no cover
    main()
