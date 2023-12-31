#!/usr/bin/python3
"""Creating a class"""


class BaseGeometry:
    """ BaseGeometry Class"""

    def __init__(self):

        pass

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):

        if type(value) is not int:

            raise TypeError(f"{name} must be an integer")

        elif value <= 0:

            raise ValueError(f"{name} must be greater than 0")
