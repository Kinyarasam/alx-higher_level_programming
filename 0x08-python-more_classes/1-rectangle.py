#!/usr/bin/python3
"""Class Rectangle defines a rectangle
"""


class Rectangle:
    """defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """constructor
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
