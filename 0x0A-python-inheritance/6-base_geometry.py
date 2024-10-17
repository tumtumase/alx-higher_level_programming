#!/usr/bin/python3
"""Module that contains the BaseGeometry class"""


class BaseGeometry:
    """A class with public instance method area()"""

    def area(self):
        """Method to compute the area

        Raises:
            Exception: with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
