#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
