#!/usr/bin/env python3
'''
# 0x02-python_async_comprehension/2-measure_runtime.py
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the total execution time.

    Returns:
        float: The total execution time.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     runtime = await measure_runtime()
        ...     print(f"Total execution time: {runtime:.2f} seconds")
        >>> asyncio.run(main())
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
