#!/usr/bin/python3
"""This is a 'square' module"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method to initialize a Square instance
        with specified size, x, y, and optional id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method that returns:
        [Square] (<id>) <x>/<y> - <width>/<height>
        """
        classname = self.__class__.__name__
        return f"[{classname}] ({self.id})"\
               f" {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size, performing type and size
        value checks before setting the value.
        """
        self.check_type("width", value)
        self.check_size_value("width", value)
        self.width = value
        self.height = value
