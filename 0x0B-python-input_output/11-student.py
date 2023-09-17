#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.

        Args:
            attrs (list): A list of attribute names to include in the dictionary.

        Returns:
            dict: dictionary containing selected attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
        for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student with the provided JSON data.
        """
        for key, value in json.items():
            setattr(self, key, value)
