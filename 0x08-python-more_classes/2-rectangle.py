#!/usr/bin/python3
""" module for a rectangle"""


class Rectangle:
    """ class for rectangle
    2d object with 4 sides
    """
    def __init__(self, width=0, height=0):
        """
        initialises the rectangle

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set for width"""
        return self.__width

    @property
    def height(self):
        """get/set for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

   @height.setter
   def height(self, value):
       """ setter for height """
       if not isinstance(value, int):
           raise TypeError('height must be an integer')
       elif value < 0:
           raise ValueError('height must be >= 0')
       self.__height = value

       def area(self):
           """
           defines the area of a rectangle
           """
           return self.height * self.height

       def perimeter(self):
           """ function that returns the perimeter of a triangle """
           if self.width == 0 or self.height == 0:
               return 0
           else:
               return 2 * (self.width + self.height)
