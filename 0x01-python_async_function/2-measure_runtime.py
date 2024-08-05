#!/usr/bin/env python3
'''
# 0x01-python_async_function/2-measure_runtime.py
'''

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Computes the average runtime of wait_n.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average runtime of wait_n.

    Example:
        >>> measure_time(10, 5)
        0.45
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
