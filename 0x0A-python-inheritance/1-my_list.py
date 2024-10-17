#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list and adds a method to print sorted elements."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)  # Create a sorted version of the list
        print(sorted_list)          # Print the sorted list
