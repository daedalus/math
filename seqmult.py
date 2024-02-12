#!/usr/bin/env python
# Author Dario Clavijo 2020
from functools import reduce

def SeqMult(lst):
    return reduce(lambda x, y: x * y, lst)


print((SeqMult([1, 2, 3, 4, 5]) == (1 * 2 * 3 * 4 * 5)))
