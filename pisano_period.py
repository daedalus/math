#!/usr/bin/env python3
# Author Dario Clavijo 2021
import sys


def pisano_period(m):
    """
    A001175
    """
    if m == 1:
        return 1
    a = b = 1
    n = i = 0
    while i <= (m**2):
        b, a = a, (a + b) % m
        if a == 1 and b == 0:
            return n + 2
        n += 1


if __name__ == "__main__":
    for i in range(1, 100):
        print((pisano_period(i)))
