#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string, if not, raise a TypeError
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the result string
    result = ""

    # Iterate through each character in the input text
    for char in text:
        result += char

        # Check if the character is one of the specified punctuation marks
        if char in '.?:':
            result += '\n\n'  # Add 2 new lines after the punctuation mark

    # Print the formatted text
    print(result, end="")
