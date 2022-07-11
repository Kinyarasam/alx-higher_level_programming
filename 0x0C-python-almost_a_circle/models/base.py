#!/usr/bin/python3
""" Defines a base model class """
import json


class Base:
    """ Represents the base model

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
        # return json.dumps(list_dictionaries, sort_keys=True, indent=4)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file

        Args:
            cls:
            list_objs (list): A list of inherited Base instance
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as json_file:
            if list_objs is None or len(list_objs) < 0:
                json_file.write("[]")
            else:
                list_dictionary = [x.to_dictionary() for x in list_objs]
                json_file.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation

        Args:
            json_string (str): A JSON str representation of a list of dicts.

        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set:

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
