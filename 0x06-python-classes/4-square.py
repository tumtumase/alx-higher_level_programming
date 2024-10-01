#!/usr/bin/python3

class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
