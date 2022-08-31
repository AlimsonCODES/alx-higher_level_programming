#!/usr/bin/python3
""" module """


class BaseGeometry:
    """ yeah yeah"""
    def area(self):
        """ function for area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ new module"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
