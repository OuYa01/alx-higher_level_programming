#!/usr/bin/python3
"""Creating a class"""


class Student:
    """
    class Student that defines a student
    by first name and last name and age
    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                    }
        else:
            return {

                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
            }

    def reload_from_json(self, json):
        """update all the attributtes of student"""
        for i in json:
            self.__dict__.update({i: json[i]})
