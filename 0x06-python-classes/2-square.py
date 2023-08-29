#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
