#!/usr/bin/python3
""" new module """


def inherits_from(obj, a_class):
    """ checks if issubclass"""
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
