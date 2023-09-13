#!/usr/bin/python3
"""Creating a function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename) as file:
        print(file.read(), end="")
