#!/usr/bin/env python3
from typing import Tuple, List, Any

"""
Zooms in on the elements of a tuple by repeating each element based on the given factor.
"""

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple:
    """
    Zooms in on the elements of a tuple by repeating each element based on the given factor.
    """
    zoomed_in: List = [
            item for item in lst
            for _ in range(factor)
            ]
    return tuple(zoomed_in)

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
