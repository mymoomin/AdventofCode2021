import numpy as np


def main():
    data = get_input("day4")
    one = part1(data)
    print(one)
    return one


def get_input(filename: str):
    with open(f"src/AoC2021/data/{filename}.txt", "r") as f:
        return f.read().split("\n\n")


def part1(data: list[str]):
    bingo_draws = [int(num) for num in data[0].split(",")]
    boards = data[1:]
    board_arrays = [
        np.genfromtxt(board.split("\n"), dtype=np.int64) for board in boards
    ]
    for draw in bingo_draws:
        for board in board_arrays:
            board[...] = np.where(board == draw, -1, board)
            col_totals = np.sum(board, axis=0)
            row_totals = np.sum(board, axis=1)
            if -5 in col_totals or -5 in row_totals:
                board = np.where(board == -1, 0, board)
                print(draw * np.sum(board))
                return draw * np.sum(board)


if __name__ == "__main__":  # pragma no cover
    main()
