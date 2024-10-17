#!/usr/bin/python3
"""Module that contains the BaseGeometry class"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def area(self):
        """Method to compute the area

        Raises:
            Exception: with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value

        Args:
            name (str): name of the value
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
