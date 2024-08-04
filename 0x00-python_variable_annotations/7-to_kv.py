#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Converts a key and its value to a tuple of the key and the square of its value.

    Args:
        k (str): The key to be converted.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of its value.

    Example:
        >>> to_kv('x', 3)
        ('x', 9.0)
        >>> to_kv('y', 4.5)
        ('y', 20.25)
    '''
    return (k, float(v**2))
