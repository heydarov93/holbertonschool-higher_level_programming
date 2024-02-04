#!/usr/bin/python3
"""Document for Module"""


class Square:
    """Defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square object"""
        self.size = size
        self.position = position

    def area(self):
        """calculates are of square object

        Return:
        - area of square object
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of private size field"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks and assigns value to private instance size field"""
        Square.checksize(value)
        self.__size = value

    @property
    def position(self):
        """Retrieves the value of private position field"""
        return self.__position

    @position.setter
    def position(self, value):
        """Checks value and assigns it to __position

        Raises:
        - TypeError if value not a tuple of 2 positive int
        """
        if (
                isinstance(value, tuple) and (len(value) == 2)
                and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            self.__position = value
            return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0], "#" * self.size, sep="")

    @classmethod
    def checksize(cls, size):
        """Checks size and raises exception
        if size doesn't fit expectations
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
