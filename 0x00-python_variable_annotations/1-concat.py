#!/usr/bin/env python3
'''Task 1's module.
'''


def concat(str1: str, str2: str) -> str:
    '''
    Concatenates two strings.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat('Hello, ', 'world!')
        'Hello, world!'
    '''
    return str1 + str2
