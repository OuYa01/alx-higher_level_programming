#!/usr/bin/python3
"""Creating a function"""


def append_write(filename="", text=""):

    with open(filename, "a") as file:

        return file.write(text)
