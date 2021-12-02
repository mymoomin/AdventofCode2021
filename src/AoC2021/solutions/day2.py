"""Day 2: Dive! https://adventofcode.com/2021/day/2"""

from AoC2021.utils import get_input, product


def main():
    data = get_input("day2")
    one = part1(data)
    two = part2(data)
    print(one, two)
    return (one, two)


def part1(directions: list[str]):
    position = [0, 0]

    for direction in directions:
        if direction:
            heading, distance = direction.split(" ")
            if heading == "up":
                position[0] -= int(distance)
            elif heading == "down":
                position[0] += int(distance)
            elif heading == "forward":
                position[1] += int(distance)
            else:
                raise ValueError(f"invalid direction {heading}")

    return product(position)


def part2(directions: list[str]):
    position = [0, 0]
    aim = 0

    for direction in directions:
        if direction:
            heading, distance = direction.split(" ")
            if heading == "up":
                aim -= int(distance)
            elif heading == "down":
                aim += int(distance)
            elif heading == "forward":
                position[1] += int(distance)
                position[0] += int(distance) * aim
            else:
                raise ValueError(f"invalid direction {heading}")

    return product(position)


if __name__ == "__main__":  # pragma no cover
    main()
