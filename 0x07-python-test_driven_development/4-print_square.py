#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0, if yes, raise a ValueError
    if size < 0:
        raise ValueError("size must be >= 0")

    # Loop to print the square
    for _ in range(size):
        print("#" * size)
