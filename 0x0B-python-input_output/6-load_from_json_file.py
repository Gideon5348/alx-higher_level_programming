#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object created from the JSON data.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
