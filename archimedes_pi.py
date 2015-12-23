#!/usr/bin/env python
#
# Author Dario Clavijo 2015

from math import *

RAD = 0.0174533

def approximation(sides):
	angle = (360*RAD)/sides
	inside = sin(angle / 2) * sides
	outside = tan(angle / 2) * sides
	pi_guess = (inside + outside) / 2
	accuracy = (1 - (pi_guess - pi) / pi) * 100

	print "sides:",sides	
	print "angle:",angle
	print "inside:",inside
	print "outside:",outside,
	print "pi_guess:",pi_guess
	print "accuracy:",accuracy


for i in xrange(10):
	approximation(10 ** i)
