#!/usr/bin/python3
""" module """


class BaseGeometry:
    """ yeah yeah"""
    def __init__(self, width, height):
        """ init module"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """ function for area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        return value
