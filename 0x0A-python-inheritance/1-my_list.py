#!/usr/bin/python3
""" Defines an inherited list Class MyList. """

class MyList(list):
    """ Implements sorted printing for the built-in list class. """

    def print_sorted(self):
        """ __ """
        print(sorted(self))
