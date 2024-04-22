#!/usr/bin/env python3
"""
4-tasks module

Contains a function task_wait_n that spawns multiple instances of
task_wait_random.
"""

import asyncio
from asyncio import Task
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns n instances of task_wait_random
    with specified max_delay.

    Args:
        n (int): The number of times task_wait_random should be spawned.
        max_delay (int): The maximum delay in seconds for each
        task_wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks: List[Task] = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    time_delay = await asyncio.gather(*tasks)
    return sorted(time_delay)
