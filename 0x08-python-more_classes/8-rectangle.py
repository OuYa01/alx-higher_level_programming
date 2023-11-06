#!/usr/bin/python3
"""
This modul define a class Rectangle
"""


class Rectangle:
    """
    This calss represnt a Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with give it a width and height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Return:
            int: width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width of rectangle

        Args:
        value (int): the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Return:
            int: height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height of rectangle

        Args:
            value (int): the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Area of rectungle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        perimeter of rectungle
        """
        p = 2 * (self.__width + self.__height)

        if self.width == 0 or self.height == 0:
            p = 0
        return (p)

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ("")

        symbol = str(self.print_symbol) if (self.print_symbol) else ("#")
        rectangle_lines = [symbol * self.width for _ in range(self.height)]

        return ("\n".join(rectangle_lines))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        igger_or_equal:
                    returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
