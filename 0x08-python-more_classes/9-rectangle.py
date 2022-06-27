#!/usr/bin/python3
"""Class Rectangle defines a rectangle
"""


class Rectangle:
    """defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ("")
        rep = ""
        for sub in range(self.__height):
            rep += (str(self.print_symbol) * self.__width)
            if sub < self.__height - 1:
                rep += "\n"
        return (rep)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Destructor
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare area and return the biggest area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle with equal size

        Args:
            cls: class Rectangle
            size: Rectangle width and Rectangle height

        Returns:
            A new instance of Rectangle class
        """
        return cls(size, size)
