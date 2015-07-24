#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

# direct aproximation of e
# the x magic number is between 6444429920 and 6444429921

def direct_e():
        x = 6444429920 + 0.22 # or int(0x1801e3260,16) + 0.22
        ret = (1+(1.0/x))**x
        return ret

# taylor aproximation of e

def taylor_e():
	accum = 0
	for n in xrange(0,15):
		accum += 1.0/(math.factorial(n))
	return accum

# by limits definition:
# d/dx e^x = lim ((e^x . e^h) - e^x)/h as h->0 
# = e^x . lim((e^h - 1)/h) as h->0
# = e^x . 1 = e^x as h -> 0

def lim_ddx_e(x):
	h = 1.0/(534645555)
	return ((math.e**x * math.e **h) -math.e**x)/h # = math.e * ((math.e ** h - 1.0)/h)

print math.e
print direct_e()
print taylor_e()
print lim_ddx_e(1)
