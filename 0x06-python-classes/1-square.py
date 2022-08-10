#!/usr/bin/python3

"""
this would represent a module for
working with squares
"""


class Square:

    """
    a plane figure with four equal straight sides
    and four right angles.
    """
    def __init__(self, size):
        """
        Initialize a new Square.
            Args:
                size (int): The size of the new square.
        """
        self.__size = size
