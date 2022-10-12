#!/usr/bin/python3
"""classes for a singly linked list"""


class Node:
    """Node in a singly linked list"""

    def __init__(self, data=0, next_node=None):
        """Initialize a new node

        Args:
            data (int): the date at node
            next_node (node): the next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set data for the node"""
        return(self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set node fot the next node"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that represents a singly linked list"""
    def __init__(self):
        """initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node to the singly linked list which is
        sorted by its value.

        Args:
            value (node) node to be inserted"""

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """print() reperesentation for SinglyLinkedList"""

        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
