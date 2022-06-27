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

    def area(self):
        """Area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Informal representation of an object
        """
        if self.width == 0 or self.height == 0:
            return ("")
        rep = ""
        for sub in range(self.height):
            rep += ("#" * self.width)
            if sub < self.height - 1:
                rep += "\n"
        return (rep)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
