#!/usr/bin/env python3
"""
Module: 2-floor

Contains a type-annotated function `floor` that takes a float argument
and returns its floor as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of `n`.
    """
    return math.floor(n)
