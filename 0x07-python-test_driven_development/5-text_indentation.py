#!/usr/bin/python3
"""
Module that defines the text_indentation function.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip leading/trailing spaces from the text and prepare to process it
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip any spaces after punctuation marks
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Remove extra blank lines at the end and print the result
    print(result.strip(), end="")
