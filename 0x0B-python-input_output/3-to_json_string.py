#!/usr/bin/python3
""" Contains a function that returns JSON
representation of object string """


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)
    Args:
        my_obj: python object

    Returns:
        json string representation
    """
    import json
    return (json.dumps(my_obj))
