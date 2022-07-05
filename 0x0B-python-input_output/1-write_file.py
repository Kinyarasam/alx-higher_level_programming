#!/usr/bin/python3
""" Module 1-write_file
Contains function that creates file and returns num chars written
"""


def write_file(filename="", text=""):
    """ writes to text file and returns the number of characters written """
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
