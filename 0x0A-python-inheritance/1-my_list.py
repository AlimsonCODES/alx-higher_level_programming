#!/usr/bin/python3
""" my module """


class Mylist(list):
    """ class module that recieves a list"""
    def print_sorted(self):
        """ must document func"""
        sorted_list = sorted(self)
        print(sorted_list)
        del sorted_list
