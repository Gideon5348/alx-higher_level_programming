#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Read the contents of a text file (UTF-8) and print it to stdout.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
