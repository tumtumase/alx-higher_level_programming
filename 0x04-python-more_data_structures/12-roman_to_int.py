#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):  # Check if input is a string
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):  # Process the string from right to left
        value = roman_numerals.get(char, 0)  # Get the integer value of the Roman numeral

        if value < prev_value:
            total -= value  # Subtract if the current value is less than the previous one
        else:
            total += value  # Otherwise, add it to the total

        prev_value = value  # Update prev_value for the next iteration

    return total
