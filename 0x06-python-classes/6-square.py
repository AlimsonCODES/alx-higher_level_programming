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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.
            Args:
                size (int): The size of the new square.
                position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ get/set for postion tuple"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)) or (len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if ((value[0] not isinstance(value, int) and value[1] not isinstance(value, int)) or (value[0] is <= 0 and value[1] is <= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
