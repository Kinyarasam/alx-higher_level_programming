#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Rectangle.

        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
            x (int): x co-ordinates of the new Rectangle.
            y (int): y co-ordinates of the new Rectangle.
            id (int): identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Print the Rectangle using the `#` character """
        if self.width == 0 or self.height == 0:
            print('')
            return

        [print('') for y in range(self.y)]
        for h in range(self.height):
            [print(' ', end='') for x in range(self.x)]
            [print('#', end='') for w in range(self.width)]
            print('')

    def __str__(self):
        """ Return the print() and str() representation of
        the Rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ Update the Rectangle

        Args:
            *args (int): New attribute values.
                - 1st argument represents the id attribute
                - 2st argument represents the width attribute
                - 3rd argument represents the height attribute
                - 4th argument represents the x attribute
                - 5th argument represents the y attribute
        """
        if args and len(args) != 0:
            __val = 0
            for init in args:
                if __val == 0:
                    if init is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = init
                elif __val == 1:
                    self.width = init
                elif __val == 2:
                    self.height = init
                elif __val == 3:
                    self.x = init
                elif __val == 4:
                    self.y = init
                __val += 1

        elif kwargs and len(kwargs) != 0:
            for init, __val in kwargs.items():
                if init == "id":
                    if __val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = __val
                elif init == "width":
                    self.width = __val
                elif init == "height":
                    self.height = __val
                elif init == "x":
                    self.x = __val
                elif init == "y":
                    self.y = __val

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
