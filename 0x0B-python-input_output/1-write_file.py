#!/usr/bin/python3
"""Creating a function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""

    with open(filename, "w") as file:

        return file.write(text)
