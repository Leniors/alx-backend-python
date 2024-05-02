#!/usr/bin/env python3
from typing import Union, Tuple

"""
to_kv
"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv """
    return (k, v ** 2)
