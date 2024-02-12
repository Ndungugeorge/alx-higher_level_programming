#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square Class"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = self.height = self.validateWH("width", size)

    def update(self, *args, **kwargs):
        """Square Class"""
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y

        if kwargs:
            keys = set(kwargs.keys())
            self.id = kwargs["id"] if "id" in keys else self.id
            self.size = kwargs["size"] if "size" in keys else self.size
            self.x = kwargs["x"] if "x" in keys else self.x
            self.y = kwargs["y"] if "y" in keys else self.y

    def __str__(self):
        """Square Class"""
        return "[{}] ({}) {}/{} - {}".format(
                                                self.__class__.__name__,
                                                self.id,
                                                self.x, self.y, self.size
                                            )

    def to_dictionary(self):
        """Polygon to dictionary"""
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
