#!/usr/bin/env python3
"""asynchronous fn takes in an integer argument max_delay,
waits for a random delay between 0 and max_delay seconds
returns wait_time value
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for some time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
