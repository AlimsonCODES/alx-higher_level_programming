#!/usr/bin/python3
"""Module for a rectangle.
"""


class Rectangle:
    """Class for rectangle 2d object with 4 sides.
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
        """Get/set for width

        Returns:
            int: width for triangle.
        """
        return self.__width

    @property
    def height(self):
        """Get/set for height.
        
        Returns:
            int: height for triangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value (int): new width of the triangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height
        Args:
           value (int): new height of the triangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Defines the area of a rectangle.
        Returns:
            int: the new area of triangle.
        """
        return self.height * self.height

    def perimeter(self):
        """Function that returns the perimeter of a triangle.
        Returns:
            int: perimeter of triangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
