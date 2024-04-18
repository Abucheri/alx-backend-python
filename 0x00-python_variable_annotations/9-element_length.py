#!/usr/bin/env python3
"""
Module: 9-element_length

Contains a function `element_length` with annotated parameters and
return value.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements from `lst` and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
