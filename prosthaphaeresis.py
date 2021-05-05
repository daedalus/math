#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math


def pmultcos(a, b):

    a = math.acos(a)
    b = math.acos(b)

    return (math.cos(a + b) + math.cos(a - b)) / 2


def pmultsin(a, b):

    a = math.asin(a)
    b = math.asin(b)

    return (math.cos(a - b) - math.cos(a + b)) / 2


def pmultsincos(a, b):

    a = math.asin(a)
    b = math.acos(b)

    return (math.sin(a + b) + math.sin(a - b)) / 2


def pmultcossin(a, b):

    a = math.acos(a)
    b = math.asin(b)

    return (math.sin(a + b) - math.sin(a - b)) / 2


a = 0.17
b = 0.37

print a * b
print pmultcos(a, b)
print pmultsin(a, b)
print pmultsincos(a, b)
print pmultcossin(a, b)
