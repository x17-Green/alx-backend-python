#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Retrieves the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists, otherwise None.

    Examples:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element([])
        None
        >>> safe_first_element("hello")
        'h'
        >>> safe_first_element(())
        None
    '''
    if lst:
        return lst[0]
    else:
        return None
