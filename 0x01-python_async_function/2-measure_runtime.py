#!/usr/bin/env python3
"""
2-measure_runtime module

Contains a function measure_time to measure the average execution time
for wait_n.
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times wait_n should be called.
        max_delay (int): The maximum delay in seconds for each wait_n call.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
