#!/usr/bin/env python3
"""
Module: 1-concat

Contains a type-annotated function `concat` that takes two string arguments
and returns their concatenation as a string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
