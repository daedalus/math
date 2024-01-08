#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

# direct aproximation of e
# the x magic number is between 6444429920 and 6444429921


def direct_e():
    x = 6444429920 + 0.22  # or int(0x1801e3260,16) + 0.22
    return (1 + (1.0 / x)) ** x


# taylor aproximation of e


def taylor_e():
    return sum(1.0 / (math.factorial(n)) for n in range(0, 15))


# by limits definition:
# d/dx e^x = lim ((e^x . e^h) - e^x)/h as h->0
# = e^x . lim((e^h - 1)/h) as h->0
# = e^x . 1 = e^x as h -> 0


def lim_ddx_e(x):
    h = 1.0 / (534645555)
    return (
        (math.e**x * math.e**h) - math.e**x
    ) / h  # = math.e * ((math.e ** h - 1.0)/h)


def test():
    print((math.e))
    print((direct_e()))
    print((taylor_e()))
    print((lim_ddx_e(1)))


i = complex(0, 1)
pi = math.pi


def exp(n, precision=100):
    return sum((n**x) / math.factorial(x) for x in range(0, precision))


def test_exp():
    print((exp(0)))
    print((exp(0.5)))
    print((exp(1)))
    print((exp(pi)))
    print((exp(i * pi)))


test_exp()
