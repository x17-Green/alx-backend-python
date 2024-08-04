#!/usr/bin/env python3
'''Task 11's module.
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    Retrieves a value from a dictionary using a given key.

    If the key is present in the dictionary, its corresponding value is returned.
    Otherwise, a default value is returned.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Def, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Res: The retrieved value or the default value.

    Examples:
        >>> safely_get_value({'a': 1, 'b': 2}, 'a')
        1
        >>> safely_get_value({'a': 1, 'b': 2}, 'c', default='Not found')
        'Not found'
        >>> safely_get_value({'a': 1, 'b': 2}, 'b', default=None)
        2
    '''
    if key in dct:
        return dct[key]
    else:
        return default
