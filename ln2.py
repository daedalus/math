#!/usr/bin/env python


def taylor_ln2():
    h = 100000
    sum = 0
    for n in range(1, h):
        sum += ((-1) ** (n + 1)) / float(n)
    return sum


print taylor_ln2()
