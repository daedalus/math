#!/usr/bin/env python3
# Author Dario Clavijo 2021
# GPLv3 

def gcd(a, b):
    """ subGCD: Replace divisions with substactions """
    if a == b:
        return b
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def test():
    print(gcd(115,5))
    print(gcd(5,7))
    print(gcd(10,4))


    a = 37975227936943673922808872755445627854565536638199 * 40094690950920881030683735292761468389214899724061
    b = 40094690950920881030683735292761468389214899724061 * 5846418214406154678836553182979162384198610505601062333
    print(gcd(a,b))

if __name__ == "__main__":
    test()


