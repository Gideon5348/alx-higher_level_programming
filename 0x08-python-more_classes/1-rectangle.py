#!/usr/bin/python3
"""Defines a Rectangle Class."""


class Rectangle:
    """This class defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter method for the width attribute."""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter method for the width attribute."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """Getter method for the height attribute."""
                return self.__height

            @height.setter
            def height(self, value):
                """Setter method for the height attribute."""
                if not isinstance(value, int):
                    raise TypeErrror("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
