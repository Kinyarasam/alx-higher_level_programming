#!/usr/bin/python3
""" Contains a function that returns python DSA from JSON string
"""


def from_json_string(my_str):
    """Returns python DSA from JSON string
    Args:
        my_str: json string representation

    Returns:
        Python object
    """
    import json
    return (json.loads(my_str))
