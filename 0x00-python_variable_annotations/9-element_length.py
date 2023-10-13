#!/usr/bin/env python3
""" Duck typing an iterable object """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Duck typing an iterable object """
    return [(i, len(i)) for i in lst]
