#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def is_safe(board, row, col, n):
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
    for i, j in zip(range(row, -1, -1), range(col, n)):
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

    def solve_util(row):
        if row == n:
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        print("[{}, {}]".format(i, j), end=' ')
            print()
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0

    solve_util(0)
