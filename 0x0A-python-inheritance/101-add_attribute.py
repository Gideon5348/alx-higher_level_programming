#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr_name (str): The name of the new attribute.
        attr_value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    # Check if the object supports attribute assignment
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # If the object supports attribute assignment, add the attribute
    setattr(obj, attr_name, attr_value)
