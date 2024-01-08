#!/usr/bin/env python
# Author Dario Clavijo 2016
# GPLv3

# AM => GM => HM
# arithmetric mean
def AM(data):
    accum = sum(data[i] for i in range(0, len(data) - 1))
    return accum / len(data)


# geometric mean
def GM(data):
    accum = 1
    for i in range(0, len(data) - 1):
        accum *= data[i]
    return accum ** (1 / len(data))


# harmonic mean
def HM(data):
    accum = sum(1 / data[i] for i in range(0, len(data) - 1))
    return len(data) * (accum**-1)
