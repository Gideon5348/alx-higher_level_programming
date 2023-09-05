#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N queens problem and print all solutions.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    def print_solution(board):
        solution = []
        for row in board:
            queen_col = row.index(1)
            solution.append([board.index(row), queen_col])
        print(solution)

    def solve_util(row):
        if row == n:
            print_solution(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0

    solve_util(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
