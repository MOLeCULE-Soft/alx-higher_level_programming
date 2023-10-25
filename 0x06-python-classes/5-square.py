#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Property to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property to set size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """Print square using # symbols"""
        if (not self.size):
            print()
        for i in range(self.size):
            print("#" * self.size)
