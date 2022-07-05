#!/usr/bin/python3
"""Contains a function that creates a python obj from Json file
"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file

    Returns:
        Python Obj created
    """
    import json

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
