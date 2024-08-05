#!/usr/bin/env python3
# 0x01-python_async_function/0-basic_async_syntax.py

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
