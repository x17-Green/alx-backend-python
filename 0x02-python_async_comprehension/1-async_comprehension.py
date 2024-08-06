#!/usr/bin/env python3
'''
# 0x02-python_async_comprehension/1-async_comprehension.py
'''

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Creates a list of 10 numbers from a 10-number generator.

    This function utilizes asynchronous comprehension to generate
    a list of numbers from an asynchronous generator.
    The generator produces 10 random numbers.

    Args:
        None

    Returns:
        List[float]: A list of 10 floating point numbers.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     numbers = await async_comprehension()
        ...     print(numbers)
        >>> asyncio.run(main())
        [1.23, 4.56, 7.89, 0.12, 3.45, 6.78, 9.01, 2.34, 5.67, 8.90]
    '''
    return [num async for num in async_generator()]
