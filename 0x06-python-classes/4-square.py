#!/usr/bin/python3
"""DEfine a class Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """CalculTE the areaa of the current square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
