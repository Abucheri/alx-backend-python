#!/usr/bin/env python3
"""
Module: 102-type_checking

Contains a function `zoom_array` with corrected type annotations.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a zoomed-in list by repeating each item in the input list `factor`
    times.

    Args:
        lst (Tuple): The input list to be zoomed-in.
        factor (int, optional): The factor by which each item in the input
        list is repeated. Defaults to 2.

    Returns:
        List: The zoomed-in list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
