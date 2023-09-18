#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
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
        pass  # File doesn't exist, do nothing
