#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

from math import *

# tells if a n is prime or not
def isPrime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


# finds the prime factors of n
def factors(n):
    factor = []
    limit = int(round(sqrt(n), 2)) + 1
    check = 2
    num = n
    if isPrime(n):
        return [n]
    for check in range(2, limit):
        if isPrime(check) and (num % check) == 0:
            factor.append(check)
            num /= check
            if isPrime(num):
                factor.append(num)
                break
    return sorted(factor)


# add the negative factors to try
def addnegatives(D):
    nD = []
    for i in D:
        nD.extend((-abs(i), abs(i)))
    return nD


# one step ruffini
def ruffini_step(P, D):

    for i in range(len(D)):
        tmpPoli = []
        for j in range(len(P)):
            if j == 0:
                tmpPoli.append(P[j])
            else:
                tmpPoli.append(P[j] + (D[i] * tmpPoli[j - 1]))
        if tmpPoli[-1] == 0:
            return [D[i], tmpPoli]


def ruffini_test(P):
    print(("P=", P))
    TI = P[len(P) - 1]
    D = [1] + factors(abs(TI)) + [abs(TI)]
    D = addnegatives(D)
    D.sort()
    print(("D=", D))

    tmp = P
    for k in range(len(P) - 3):
        ret = ruffini_step(tmp, D)
        tmp = ret[1]
        print(("Grade=", len(P) - k, "root=", ret[0], "coefs=", ret[1]))


# P = [1,-7,13,23,-78]
P = [6, -29, 27, 27, -29, 6]
ruffini_test(P)
