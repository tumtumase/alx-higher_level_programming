#!/usr/bin/python3
from add_0 import add  # Import the add function from add_0

a = 1  # Assign 1 to a
b = 2  # Assign 2 to b

# Print the result in the format: a + b = result
print("{} + {} = {}".format(a, b, add(a, b)))
