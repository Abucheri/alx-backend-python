#!/usr/bin/env python3
"""
Async Generator Module
----------------------

This module defines a coroutine called async_generator that yields random
numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that generates random numbers asynchronously.

    This coroutine loops 10 times, each time asynchronously waiting for
    1 second, then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
