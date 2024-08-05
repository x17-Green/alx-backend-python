#!/usr/bin/env python3
# 0x01-python_async_function/0-basic_async_syntax.py

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random number of seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual number of seconds waited.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     wait_time = await wait_random(max_delay=5)
        ...     print(f"Waited for {wait_time:.2f} seconds")
        >>> asyncio.run(main())
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
