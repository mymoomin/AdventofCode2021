import numpy as np


def part1(data: list[str]):
    bits = np.array([list(map(int, datum)) for datum in data])
    print(bits.mean(0).round().astype(int))
    gamma = "".join(bits.mean(0).round().astype(int).astype(str))
    return int(gamma, 2) * (2 ** len(gamma) - 1 - int(gamma, 2))


if __name__ == "__main__":  # pragma no cover
    one = part1(
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
