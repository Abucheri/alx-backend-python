#!/usr/bin/env python3
"""
Async Comprehension Module
---------------------------

This module defines a coroutine called async_comprehension that collects
10 random numbers using an async comprehension over async_generator.
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [num async for num in async_generator()]
