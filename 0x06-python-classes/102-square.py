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

    def __eq__(self, value):
        if isinstance(value, Square):
            return self.area() == value.area()
        else:
            return False
        
    def __ne__(self, value):
        if isinstance(value, Square):
            return self.area() != value.area()
        else:
            return True

    def __gt__(self, value):
        if isinstance(value, Square):
            return self.area() > value.area()
        else:
            err_msg = "'>' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
        return False 

    def __ge__(self, value):
        if isinstance(value, Square):
            return self.area() >= value.area()
        else:
            err_msg = "'>=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
        return False

    def __lt__(self, value):
        if isinstance(value, Square):
            return self.area() < value.area()
        else:
            err_msg = "'<' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
        return False
    
    def __le__(self, value):
        if isinstance(value, Square):
            return self.area() <= value.area()
        else:
            err_msg = "'<=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
        return False
