#!/usr/bin/env python3
"""
Correction of "3. Tasks"
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Regular function that creates and returns an asyncio.Task for the wait_random coroutine.
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
