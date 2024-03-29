#!/usr/bin/python3
"""class Square - A class that defines a square
"""


class Square:
    """class representing a square object
    """
    def __init__(self, size=0):
        """class constructor
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
