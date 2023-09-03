#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represent a square.

    Attributes:
        __size (int): The size of square
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance with a givine size

        Args:
            size (int): The size of square
        """
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Return:
            the area of the square as an integer.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square and perform validation.

        Args:
            value (int): The new size value to set.

        Raises:
            ValueError: If the value is not an integer.
            TypeError: If the value is  < 0
        """

        if not isinstance(value, int):
            raise ValueError("size must be integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
