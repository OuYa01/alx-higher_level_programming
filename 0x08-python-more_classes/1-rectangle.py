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
        self.__height = height
        self.__width = width

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
        else:
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
        else:
            self.__height = value
