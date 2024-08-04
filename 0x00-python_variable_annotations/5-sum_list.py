#!/usr/bin/env python3
'''Task 5's module.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Computes the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_list([1.0, 2.0, 3.0])
        6.0
    '''
    return float(sum(input_list))
