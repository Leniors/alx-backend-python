#!/usr/bin/env python3
from typing import List

"""
sum list
"""

def sum_list(input_list: List[float]) -> float:
    """ sum_list function """
    sum = 0
    for x in input_list:
        sum += x
    return sum
