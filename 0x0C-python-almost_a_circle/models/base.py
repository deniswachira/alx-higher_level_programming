#!/usr/bin/python3
"""
File: base.py

Author: Samson Tedla <samitedla23@gmail.com>

Defines a class called Base
"""
import json
import csv
import turtle


class Base:
    """
    Represent the base model

    Represents the base for all other classes

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base

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
        """Returns JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of objects to a file"""
        if list_objs is None:
            list_dict = []
        else:
            list_dict = []
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        else:
            json_list = (json.loads(json_string))
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance by processing a dictionary

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        draw = turtle.Turtle()

        for rect in list_rectangles:
            draw.showturtle()
            draw.up()
            draw.goto(rect.x, rect.y)
            draw.down()
            for i in range(2):
                draw.forward(rect.width)
                draw.left(90)
                draw.forward(rect.height)
                draw.left(90)
            draw.hideturtle()

        for sq in list_squares:
            draw.showturtle()
            draw.up()
            draw.goto(sq.x, sq.y)
            draw.down()
            for i in range(2):
                draw.forward(sq.width)
                draw.left(90)
                draw.forward(sq.height)
                draw.left(90)
            draw.hideturtle()

