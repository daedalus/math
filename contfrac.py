#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Continued_fraction
# Author Dario Clavijo 2020
# GPLv3


def cont_frac(a, b):
    coef = []
    i = a // b
    while b != 0:
        r = a // b
        i = r
        coef.append(i)
        f = a - i * b
        a = b
        b = f
    return coef


print(cont_frac(649, 200))
print(cont_frac(17993, 90581))
