#!/usr/bin/env python3
from typing import Sequence, Any, Union

"""
100-safe_first_element.py
"""

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """ Returns the first element of a sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
