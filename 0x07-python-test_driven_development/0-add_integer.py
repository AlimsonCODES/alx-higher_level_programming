#!/usr/bin/python3

"""A module for addition of 2 integers.
"""


def add_integer(a, b=98):
    """A function that adds 2 integers.
        Args:
            a (int, float): arg 1.
            b (int, float): arg 2.

        Returns:
            int: sum of two integers.
    """
    if not a or (type(a) != int and type(a) != float):
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
