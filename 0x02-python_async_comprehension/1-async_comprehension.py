#!/usr/bin/env python3
"""
1-async_comprehension.py
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> [float]:
    """
    async def async_comprehension() -> List[float]:
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
