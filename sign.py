#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

# sign of x returns: [-1,1]
def sign(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)
