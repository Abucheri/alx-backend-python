#!/usr/bin/env python3
"""
Measure Runtime Module
----------------------

This module defines a coroutine called measure_runtime that measures the
total runtime for executing async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime for executing
    async_comprehension four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
