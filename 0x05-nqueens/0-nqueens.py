#!/usr/bin/python3
""" Solution of N-Queens Problem. """

import sys


def is_safe(board: int, row: int, col: int, N: int) -> bool:
    """ Determaines if it safe to add queen in position.

    Args:
        board (int): Square of the chess board.
        row (int): Number of the cells in Row.
        col (int): Number of the cells in Col.
    Returns: (bool) safe or not.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(N: int) -> list[list]:
    """ Solving the problem.

    Args:
        N (int): Number of Length or Breathe of the Chess Board square.
    Returns: list[list] all the possible solutions.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row: int) -> None:
        if row == N:
            solutions.append([[i, row] for i, row in enumerate(board)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

