#!/usr/bin/python3
"""Base Class"""
import json
import csv
import turtle
import random

class Base:
    """Base Class"""
    __nb__objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = self.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ls = []
        if list_objs:
            for obj in list_objs:
                ls.append(obj.to_dictionary())
        with open(cls.__name__ + ".json",
                  "w", encoding="utf8") as file:
            file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ls = []
        try:
            with open(cls.__name__ + ".json",
                      "r", encoding="utf8") as file:
                list_dicts = Base.from_json_string(file.read())
                ls = [cls.create(**obj) for obj in list_dicts]
        finally:
            return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs:
            try:
                with open(cls.__name__ + ".csv",
                        "w", encoding="utf8") as file:
                    if len(list_objs) > 0:
                        column_order = [['id', 'width', 'height', 'x', 'y']]
                        column_order.append(['id', 'size', 'x', 'y'])
                        use = column_order[0 if cls.__name__ == "Rectangle" else 1]
                        writer = csv.DictWriter(file, fieldnames=use)
                        for obj in list_objs:
                            writer.writerow(obj.to_dictionary())
            finally:
                pass

    @classmethod
    def load_from_file_csv(cls):
        ls = []
        try:
            with open(cls.__name__ + ".csv",
                      "r", encoding="utf8") as file:
                column_order = [['id', 'width', 'height', 'x', 'y']]
                column_order.append(['id', 'size', 'x', 'y'])
                use = column_order[0 if cls.__name__ == "Rectangle" else 1]
                reader = csv.DictReader(file, fieldnames=use)
                reader = [dict([k, int(v)] for k, v in d.items())
                          for d in reader]
                ls = [cls.create(**obj) for obj in reader]
        finally:
            return ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        mole = turtle.Turtle()
        mole.shape("turtle")

        polygons = list_rectangles
        polygons.extend(list_squares)

        for polygon in polygons:
            mole.showturtle()
            mole.up()
            mole.goto(polygon.x, polygon.y)
            mole.down()
            mole.color("#" + format(random.randint(0, 0xFFFFFF), '06X'))
            mole.screen.bgcolor("#" + format(random.randint(0, 0xFFFFFF), '06X'))
            mole.pensize(random.randint(1, 10))
            for i in range(2):
                mole.forward(polygon.width)
                mole.left(90)
                mole.forward(polygon.height)
                mole.left(90)
            mole.hideturtle()

        turtle.exitonclick()
