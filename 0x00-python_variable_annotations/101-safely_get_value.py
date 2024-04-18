#!/usr/bin/env python3
"""
Module: 101-safely_get_value

Contains a function `safely_get_value` with type annotations.
"""

from typing import Mapping, Any, Union, TypeVar


# Define a TypeVar for the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value corresponding to the key in the dictionary `dct`,
    or the default value if the key is not found.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
