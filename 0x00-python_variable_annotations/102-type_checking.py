#!/usr/bin/env python3
'''Task 12's module.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Creates multiple copies of items in a tuple.

    Args:
        lst (Tuple): The input tuple to be zoomed.
        factor (int, optional): The number of times to replicate each item. Defaults to 2.

    Returns:
        List: A list with each item from the input tuple replicated 'factor' times.

    Example:
        >>> array = (12, 72, 91)
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]
        >>> zoom_3x = zoom_array(array, 3)
        >>> print(zoom_3x)
        [12, 12, 12, 72, 72, 72, 91, 91, 91]
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
