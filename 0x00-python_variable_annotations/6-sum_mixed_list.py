#!/usr/bin/env python3
'''Task 6's module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Computes the sum of a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.

    Example:
        >>> sum_mixed_list([1, 2, 3.5, 4.2])
        10.7
    '''
    return float(sum(mxd_lst))
