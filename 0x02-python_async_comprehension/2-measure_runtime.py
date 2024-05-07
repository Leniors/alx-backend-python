#!/usr/bin/env python3
"""
2-measure_runtime.py
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    2-measure_runtime.py
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
