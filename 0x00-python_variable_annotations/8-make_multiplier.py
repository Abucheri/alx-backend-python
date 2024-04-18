#!/usr/bin/env python3
"""
Module: 8-make_multiplier

Contains a type-annotated function `make_multiplier` that takes a float
`multiplier` as argument and returns a function that multiplies a float
by the given `multiplier`.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given `multiplier`.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the given `multiplier`.
    """
    def mult_func(num: float) -> float:
        """
        Multiplies a float by the given `multiplier`.

        Args:
            num (float): The float value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return num * multiplier
    return mult_func
