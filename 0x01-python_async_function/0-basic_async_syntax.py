#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ An asynchronous coroutine that takes in an integer argument
        `max_delay', waits for a random delay between 0 and
        `max_delay` seconds and eventually returns it.
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
