#!/usr/bin/python3
"""Contains a function that writes Python Objects to
file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON representation
    Args:
        my_obj: python Object
        filename: file

    Returns:
        nothing.
    """
    import json

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
