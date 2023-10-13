#!/usr/bin/env python3
""" Type annotation of Complex types - functions / callable """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    """
    def callable(x: float) -> float:
        return x * multiplier

    return callable
