#!/usr/bin/python3
"""
Module contains class that inherits from <list>
"""


class MyList(list):
    """
    Custom implementation of a list that contains integers.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        """
        print(sorted(self))
