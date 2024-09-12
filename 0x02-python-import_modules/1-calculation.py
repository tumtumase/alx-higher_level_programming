#!/usr/bin/python3
from calculator_1 import add, sub, mul, div  # Import only the required functions

a = 10  # Define variable a
b = 5   # Define variable b

# Perform calculations and print the results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
