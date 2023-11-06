#!/usr/bin/python3
"""Creating a class"""


class BaseGeometry:
    """ BaseGeometry Class"""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
