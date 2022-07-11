#!/usr/bin/python3
""" Defines a square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a Square. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square.

        Args:
            size (int): The size of the new square
            x (int): The x co-ordinates of the new square
            y (int): The y co-ordinates of the new square
            id (int): The identity of the new new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            __val = 0
            for __arg in args:
                if __val == 0:
                    if __arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = __arg
                elif __val == 1:
                    self.size = __arg
                elif __val == 2:
                    self.x = __arg
                elif __val == 3:
                    self.y = __arg
                __val += 1

        elif kwargs and len(kwargs) != 0:
            for __val, __kwarg in kwargs.items():
                if __val == "id":
                    if __kwarg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = __kwarg
                elif __val == "size":
                    self.size = __kwarg
                elif __val == "x":
                    self.x = __kwarg
                elif __val == "y":
                    self.y = __kwarg

    def to_dictionary(self):
        """ Return the dictionary representation of the Square. """

        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
