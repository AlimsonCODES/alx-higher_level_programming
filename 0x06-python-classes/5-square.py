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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """
        calculates area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        print '#' for area of square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.size):
                for num in range(self.size):
                    print("#", end='')
                print("")
