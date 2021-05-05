#!/usr/bin/env python
# Author Dario Clavijo 2020
# nth root of x

import math


def nth_root(n, x):
    return math.e ** ((1.0 / n) * math.log(x))


print nth_root(2, 2)
print nth_root(3, 8)
