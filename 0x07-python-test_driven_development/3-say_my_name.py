#!/usr/bin/python3
"""
Module that defines the say_my_name function.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): The first name
        last_name (str): The last name (optional)

    Raises:
        TypeError: If either first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
