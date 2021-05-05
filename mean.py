#!/usr/bin/env python
# Author Dario Clavijo 2016
# GPLv3

# AM => GM => HM
# arithmetric mean
def AM(data):
    accum = 0
    for i in range(0, len(data) - 1):
        accum += data[i]
    return accum / len(data)


# geometric mean
def GM(data):
    accum = 1
    for i in range(0, len(data) - 1):
        accum *= data[i]
    return accum ** (1 / len(data))


# harmonic mean
def HM(data):
    accum = 0
    for i in range(0, len(data) - 1):
        accum += 1 / data[i]
    return len(data) * (accum ** -1)
