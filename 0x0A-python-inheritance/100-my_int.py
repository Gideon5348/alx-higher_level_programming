#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Represents a rebel integer."""

    def __eq__(self, other):
        """Override the equality operator (==) to invert behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to invert behavior."""
        return super().__eq__(other)
