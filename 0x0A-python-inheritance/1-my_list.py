#!/usr/bin/python3
""" Creating Mylist class """

class List:
    """
    List class
    """

    def __init__(self):
        self.list1 = []
    def append(self, item):
        self.list1.append(item)
    def print_stored(self):
        print(self.list1)

class MyList(List):
    """
    MyList class that inherits from list
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        self.list1.sort()
        print(self.list1)
    def __str__(self):
        return (str(self.list1))
