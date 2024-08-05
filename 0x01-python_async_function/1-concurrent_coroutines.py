#!/usr/bin/env python3
'''
# 0x01-python_async_function/1-concurrent_coroutines.py
'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes wait_random n times concurrently and returns
    a sorted list of wait times.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A sorted list of wait times.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     wait_times = await wait_n(5, 10)
        ...     print(wait_times)
        >>> asyncio.run(main())
        [1.234, 2.345, 3.456, 4.567, 5.678]
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
