#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # Check if the key exists in the dictionary
        del a_dictionary[key]  # Delete the key if it exists
    return a_dictionary  # Return the updated dictionary
