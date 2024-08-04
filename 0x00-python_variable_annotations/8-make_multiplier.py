#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function that multiplies its input by a given factor.

    Args:
        multiplier (float): The factor by which the input will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the product of the input and the multiplier.

    Example:
        >>> double = make_multiplier(2.0)
        >>> double(5.0)
        10.0
        >>> triple = make_multiplier(3.0)
        >>> triple(5.0)
        15.0
    '''
    return lambda x: x * multiplier
