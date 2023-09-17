#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class that only allows the 'first_name' attribute to be assigned.
    """
    __slots__ = ("first_name",)
