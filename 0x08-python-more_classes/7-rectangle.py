#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """This class defines a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    number_of_instances = 0  # Public class attribute
    print_symbol = '#'      # Public class attribute

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Getter method for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_line = str(self.print_symbol) * self.__width
        return '\n'.join([symbol_line for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method to print a message when an instance is deleted."""
        print("Bye rectangle...")
