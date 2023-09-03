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

        Raises:
            TypeError : If size is not an integer
            VlueError: IF size is < 0

        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Return:
            the area of the square as an integer.
        """
        return (self.__size ** 2)
