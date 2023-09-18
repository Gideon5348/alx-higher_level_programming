#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert.
    """
    try:
        with open(filename, mode="r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

            file.truncate()

    except FileNotFoundError:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(new_string)
