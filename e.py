#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

# the x magic number is between 6444429920 and 6444429921
def direct_e():
        x = 6444429920 + 0.22 # or int(0x1801e3260,16) + 0.22
        ret = (1+(1.0/x))**x
        return ret


def taylor_e():
	accum = 0
	for n in xrange(0,15):
		accum += 1.0/(math.factorial(n))
	return accum

print math.e
print direct_e()
print taylor_e()
