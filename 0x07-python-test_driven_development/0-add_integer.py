#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """Returns the addition of two integers
    
    Args:
    a: first number
    b: second number

    Returns:
    The addition of the two given numbers

    Raises:
         TypeError: If a or b aren't integer and/or float numbers

    """

   if type(a) == float or type(b) == float:
       a = int(a)
       b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
