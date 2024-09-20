#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Create a set to filter out duplicates
    total_sum = sum(unique_numbers)  # Calculate the sum of unique integers
    return total_sum  # Return the result
