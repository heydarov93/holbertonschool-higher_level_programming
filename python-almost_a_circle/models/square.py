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
