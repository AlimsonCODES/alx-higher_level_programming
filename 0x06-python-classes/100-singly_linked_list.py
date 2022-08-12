#!/usr/bin/python3
""" module for node structure """


class Node:
    """
    this is the class for node structure
    """
    def __init__(self, data, next_node=None):
        """
        init for structure
        Args:
            data (int): integer var
            next_node (None): nxt node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set for data in sll"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """get/set for next node in sequence"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise Typeerror('next_node must be a Node object')

class SinglyLinkedList:
    """
    class for a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Define the print() representation of a SinglyLinkedList."""
        if not isinstance(value, int) or value is None:
            raise TypeError('value must be an integer')
        else:
            if self.__head is None or self.__head.data >= value:
                new_node = Node(value, self.__head)
                self.__head = new_node
            else:
                node_ptr = self.__head
                prev_ptr = None
                while node_ptr is not None and value > node_ptr.data:
                    prev_ptr = node_ptr
                    node_ptr = node_ptr.next_node
                new_node = Node(value, node_ptr)
                prev_ptr.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
