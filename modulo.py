import math


def subMod(a, n):
    """Naive modulo implementation with substraction"""
    while a <= n:
        n -= a
    return n


def divMod(d, n):
    """Naive division modulo implementation with substraction"""
    r = 0
    while d <= n:
        n -= d
        r += 1
    return r, n


def test():
    x = 10
    for i in range(1, 11):
        a = subMod(i, x)
        r, m = divMod(i, x)
        b = x % i
        print((x, i, a, b, a == b, r, m, x == (r * i) + m))


if __name__ == "__main__":
    test()
