import functools
from typing import Iterable


def get_input(filename: str):
    with open(f"src/AoC2021/data/{filename}.txt", "r") as f:
        data = f.read().split("\n")
    if data[-1] == "":
        data.pop()
    return data


def product(vals: Iterable[float]):
    return functools.reduce(lambda acc, cur: acc * cur, vals)
