#!/usr/bin/env python3
# Author Dario Clavijo 2021
# GPLv3


def gcd(a, b):
    """Binary GCD implementation: it replaces division by one-bit shifts"""
    if a == b:
        return b
    if a == 0:
        return b
    if b == 0:
        return a
    if a & 1 == 1:
        if b & 1 == 0:
            return gcd(a, b >> 1)
        else:
            return gcd(abs(a - b), min(a, b))
    else:
        if b & 1 == 1:
            return gcd(a >> 1, b)
        else:
            return 2 * gcd(a >> 1, b >> 1)


def test():
    print(gcd(115, 5))
    print(gcd(5, 7))
    print(gcd(10, 4))

    a = (
        37975227936943673922808872755445627854565536638199
        * 40094690950920881030683735292761468389214899724061
    )
    b = (
        40094690950920881030683735292761468389214899724061
        * 5846418214406154678836553182979162384198610505601062333
    )
    print(gcd(a, b))


if __name__ == "__main__":
    test()
