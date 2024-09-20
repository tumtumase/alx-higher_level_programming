#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # Check if the dictionary is None or empty
        return None
    
    best_key = max(a_dictionary, key=a_dictionary.get)  # Find the key with the maximum value
    return best_key  # Return the key with the highest score
