#!/usr/bin/env python3
"""
Measure Runtime Module
----------------------

This module defines a coroutine called measure_runtime that measures the
total runtime for executing async_comprehension four times in parallel.
"""

import asyncio
from time import perf_counter
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime for executing
    async_comprehension four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end_time = perf_counter()
    return end_time - start_time
