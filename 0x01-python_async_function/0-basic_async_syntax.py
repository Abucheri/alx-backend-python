#!/usr/bin/env python3
"""
0-basic_async_syntax module

Contains an asynchronous coroutine wait_random that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default 10).

    Returns:
        float: The random delay.
    """
    time_delay = random.uniform(0, max_delay)
    await asyncio.sleep(time_delay)
    return time_delay
