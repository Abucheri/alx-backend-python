#!/usr/bin/env python3
"""
3-tasks module

Contains a regular function task_wait_random that returns an asyncio.Task.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random
        coroutine.

    Returns:
        Task: An asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
