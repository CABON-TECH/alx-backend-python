#!/usr/bin/env python3
""" Executing multiple coroutines tasks at the same time with async """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that spawns the task `wait_random` `n` times with
        the specified `max_delay` with a task
    """

    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delays.append(task)
        await task
    return sorted(await asyncio.gather(*delays))
