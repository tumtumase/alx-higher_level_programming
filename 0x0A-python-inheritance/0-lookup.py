#!/usr/bin/python3
"""
Module to return a list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
        
    Returns:
        A list of attributes and methods.
    """
    return dir(obj)
