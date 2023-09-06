#!/usr/bin/python3
"""
This modul define a class Rectangle
"""


class Rectangle:
    """
    This calss represnt a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with give it a width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Return:
            int: width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width of rectangle

        Args:
        value (int): the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Return:
            int: height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height of rectangle

        Args:
            value (int): the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Area of rectungle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        perimeter of rectungle
        """
        p = 2 * (self.__width + self.__height)

        if self.width == 0 or self.height == 0:
            p = 0
        return (p)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        rec_str = ""
        
        for _ in range(self.height):
            rec_str += "#" * self.__width + '\n'
        return (rec_str)
