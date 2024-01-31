#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    def validate(value, name):
        """Validator function"""
        if type(value) is int:
            if value >= 0:
                return value
            else:
                raise ValueError('{} must be >= 0'.format(name))
        else:
            raise TypeError('{} must be an integer'.format(name))

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = Rectangle.validate(width, "width")
        self.__height = Rectangle.validate(height, "height")

    @property
    def width(self):
        """Property to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set width"""
        self.__width = Rectangle.validate(value, "width")

    @property
    def height(self):
        """Property to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to set height"""
        self.__height = Rectangle.validate(value, "height")
