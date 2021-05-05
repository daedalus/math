#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

# absolute value of x
def _abs(x):
    if x >= 0:
        return x
    else:
        return -x


# sign of x returns: [-1,1]
def sign(x):
    if x == 0:
        return 0
    else:
        return x / _abs(x)


def almostEqual(a, b, epsilon):
    return _abs(a - b) <= epsilon


print sign(1)
print sign(0)
print sign(-1)
