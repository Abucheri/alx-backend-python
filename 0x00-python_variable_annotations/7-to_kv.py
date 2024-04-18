#!/usr/bin/env python3
"""
Module: 7-to_kv

Contains a type-annotated function `to_kv` that takes a string `k`
and an int or float `v` as arguments and returns a tuple.
The first element of the tuple is the string `k`, and the second
element is the square of the int/float `v` (annotated as a float).
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string `k` as the first element
    and the square of the int/float `v` as the second element.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float.

    Returns:
        Tuple[str, float]: A tuple containing `k` and the square of `v`.
    """
    return (k, v ** 2)
