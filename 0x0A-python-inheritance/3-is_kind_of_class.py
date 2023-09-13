#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class."""
    return isinstance(obj, a_class)
