#!/usr/bin/env python3
'''
# 0x02-python_async_comprehension/0-async_generator.py
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Generates a sequence of 10 random numbers between 0 and 10.

    This asynchronous generator uses asyncio.sleep
    to pause execution for 1 second
    between each generated number.

    Yields:
        float: A random number between 0 and 10.

    Example:
        >>> async def main():
        ...     async for num in async_generator():
        ...         print(num)
        >>> asyncio.run(main())
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
