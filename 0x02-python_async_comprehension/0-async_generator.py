#!/usr/bin/env python3
"""async_generator loops 10 times, asynchronously waits 1 second,
then yield a random number between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
