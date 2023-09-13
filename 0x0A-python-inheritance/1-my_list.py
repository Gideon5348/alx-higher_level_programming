#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A class that inherits from list and provides additional methods.

    Public methods:
    - print_sorted(): Print the list in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
