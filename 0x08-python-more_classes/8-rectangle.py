#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        s = (str(self.print_symbol) * self.width + '\n') * self.height
        return s[:-1]

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width,
                                   self.height
                                   )

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() >= rect_2.area():
                    return rect_1
                return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
