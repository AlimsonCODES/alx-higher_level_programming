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
    def __init__(self, size=0):
        """
        Initialize a new Square.
            Args:
                size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get/set the object size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """
        calculates area
        """
        return (self.__size ** 2)
