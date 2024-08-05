#!/usr/bin/env python3
'''
# 0x01-python_async_function/3-tasks.py
'''

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay for the wait_random task.

    Returns:
        asyncio.Task: An asynchronous task that waits for a random delay.

    Example:
        >>> import asyncio
        >>> task = task_wait_random(5)
        >>> asyncio.run(task)
    '''
    return asyncio.create_task(wait_random(max_delay))
