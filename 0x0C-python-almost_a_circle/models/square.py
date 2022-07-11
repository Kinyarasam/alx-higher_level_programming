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
