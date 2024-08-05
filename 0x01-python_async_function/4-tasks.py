#!/usr/bin/env python3
'''
# 0x01-python_async_function/4-tasks.py
'''

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times concurrently and returns
    a sorted list of wait times.

    Args:
        n (int): The number of times to execute task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A sorted list of wait times.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     wait_times = await task_wait_n(5, 10)
        ...     print(wait_times)
        >>> asyncio.run(main())
        [1.23, 2.56, 3.12, 4.78, 9.01]
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
