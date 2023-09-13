#!/usr/bin/python3
"""Creating a function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, "a") as file:

        return file.write(text)
