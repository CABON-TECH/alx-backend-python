#!/usr/bin/env python3
""" Type Checking with mypy """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Function that takes in a tuple and return a list """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


my_tuple = (12, 72, 91)

zoom_2x = zoom_array(my_tuple)

zoom_3x = zoom_array(my_tuple, 3)
