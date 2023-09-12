#!/usr/bin/python3
"""A class"""


class MyInt(int):
    """ MyInt class"""

    def __init__(self, value):
        super().__init__()
        self.value = value

    def ch(self):
        if self.value == value:
            return (False)
        else:
            return (True)

    def __str__(self):
        return f"{self.value}"
