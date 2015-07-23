#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

def pmult(a,b):

	a = math.acos(a)
	b = math.acos(b)
	
	return (math.cos(a+b) + math.cos(a-b))/2

a = 0.17
b = 0.37
print pmult(a,b)
print a*b


