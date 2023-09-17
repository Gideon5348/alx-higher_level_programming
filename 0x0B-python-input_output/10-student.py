#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_attrs[attr] = getattr(self, attr)
            return filtered_attrs
