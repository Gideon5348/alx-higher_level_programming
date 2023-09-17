#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8).

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
