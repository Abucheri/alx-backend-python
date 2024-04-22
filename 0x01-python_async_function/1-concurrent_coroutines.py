#!/usr/bin/env python3
"""
1-concurrent_coroutines module

Contains an asynchronous routine wait_n that spawns multiple instances
of wait_random.
"""

import asyncio
from typing import List
from random import randint
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns n instances of wait_random with
    specified max_delay.

    Args:
        n (int): The number of times wait_random should be spawned.
        max_delay (int): The maximum delay in seconds for each
        wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks: List[Task] = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
