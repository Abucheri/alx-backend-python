#!/usr/bin/env python3
"""
Module: 100-safe_first_element

Contains a function `safe_first_element` with duck-typed annotations.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence, if it exists.

    Args:
        lst (Sequence[Any]): A sequence of elements with unspecified types.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
