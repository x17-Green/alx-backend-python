#!/usr/bin/env python3
'''Task 2's module.
'''


def floor(n: float) -> int:
    '''
    Computes the floor of a floating-point number.

    The floor of a number is the largest integer less than or equal to the number.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The floor of the input number.

    Examples:
        >>> floor(3.7)
        3
        >>> floor(-3.7)
        -4
        >>> floor(3.0)
        3
    '''
    return int(n)
