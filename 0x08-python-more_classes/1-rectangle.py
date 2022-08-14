#!/usr/bin/python3
"""A Module for a rectangle"""


class Rectangle:
    """Class for rectangle 2d object with 4 sides
    """
    def __init__(self, width=0, height=0):
        """Initialises the rectangle

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
