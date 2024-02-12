#!/usr/bin/python3
"""This is a 'rectangle' module"""


from .base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    Private instance attributes, each with its own
    public getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method to initialize a Rectangle instance
        with specified width, height, x, y, and optional id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    def display(self):
        for i in range(self.height):
            """
            Method to print in stdout the Rectangle instance
            with the character #
            """
            print("#" * self.width)

    def area(self):
        """
        Method to calculate and return the area of the rectangle.
        """
        return self.width * self.height

    @staticmethod
    def check_type(field, value):
        """
        Static method to check if the given value is of type int,
        raising a TypeError if not.
        """
        if type(value) is not int:
            raise TypeError(f"{field} must be an integer")

    @staticmethod
    def check_size_value(field, value):
        """
        Static method to check if the given value is lower
        than or equal to 0, raising a ValueError.
        """
        if value <= 0:
            raise ValueError(f"{field} must be > 0")

    @staticmethod
    def check_coordnte_value(field, value):
        """
        Static method to check if the given value is lower than 0,
        raising a ValueError.
        """
        if value < 0:
            raise ValueError(f"{field} must be >= 0")

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter method to retrieve the x-coordinate of the rectangle.
        """
        return self.__x

    @property
    def y(self):
        """
        Getter method to retrieve the y-coordinate of the rectangle.
        """
        return self.__y

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate, performing type and
        coordinate value checks before setting the value.
        """
        self.check_type("x", value)
        self.check_coordnte_value("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate, performing type and
        coordinate value checks before setting the value.
        """
        self.check_type("y", value)
        self.check_coordnte_value("y", value)
        self.__y = value

    @width.setter
    def width(self, value):
        """
        Setter method for the width, performing type and size
        value checks before setting the value.
        """
        self.check_type("width", value)
        self.check_size_value("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height, performing type and size
        value checks before setting the value.
        """
        self.check_type("height", value)
        self.check_size_value("height", value)
        self.__height = value
