#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the length of each sequence in a list of sequences.

    Args:
        lst (Iterable[Sequence]): A list of sequences (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence from the input list and its length.

    Example:
        >>> element_length(['hello', [1, 2, 3], ('a', 'b', 'c')])
        [('hello', 5), ([1, 2, 3], 3), (('a', 'b', 'c'), 3)]
    '''
    return [(i, len(i)) for i in lst]
