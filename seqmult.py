#!/usr/bin/env python
# Author Dario Clavijo 2020


def SeqMult(s):
    mul = lambda a, b: a * b
    l = len(s)
    while l > 1:
        if l % 2 != 0:
            s += [1]
            l += 1
        s = list(map(mul, s[:l // 2], s[l // 2 :]))
        l = len(s)
    return s[0]


print(SeqMult([1, 2, 3, 4, 5]) == (1 * 2 * 3 * 4 * 5))
