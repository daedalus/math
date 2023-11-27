#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

# absolute value of x
def _abs(x):
    return x if x >= 0 else -x


# sign of x returns: [-1,1]
def sign(x):
    return 0 if x == 0 else x / _abs(x)


def almostEqual(a, b, epsilon):
    return _abs(a - b) <= epsilon


print sign(1)
print sign(0)
print sign(-1)
