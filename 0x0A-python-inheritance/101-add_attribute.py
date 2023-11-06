#!/usr/bin/python3
"""creating a function"""


def add_attribute(obj, name, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
