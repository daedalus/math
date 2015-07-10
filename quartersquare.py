#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

def qsqr(a,b):
	return (((a+b)**2)/4) - (((a-b)**2)/4)

def logmult(a,b):
	return math.e ** (math.log(a)+math.log(b))

a = 255
b = 255
print logmult(a,b)
print qsqr(a,b)
print a*b


