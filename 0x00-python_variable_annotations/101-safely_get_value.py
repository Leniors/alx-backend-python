#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union
"""
101-safely_get_value.py
"""

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """ Safely retrieves a value from a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
