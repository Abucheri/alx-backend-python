#!/usr/bin/env python3
"""
Module: 5-sum_list

Contains a type-annotated function `sum_list` that takes a list of floats
as input and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
