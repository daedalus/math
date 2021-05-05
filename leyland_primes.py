#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPLv3
# https://en.wikipedia.org/wiki/Leyland_number
# https://oeis.org/A094133

import gmpy2


def leyland_primes_naive(m):
    tmp = []
    for i in range(2, m):
        for j in range(2, m):
            x = i ** j + j ** i
            if gmpy2.is_prime(x):
                if x not in tmp:
                    tmp.append(x)
    return tmp


def leyland_primes_oeis(N):
    tmp = [3]
    n = 2
    n = 1
    n1 = 1
    while n < N:
        n = 2 * n1 ** n1
        k = n1 + 1
        while k < N:
            if gmpy2.gcd(n, k) == 1:
                a = n ** k + k ** n
                if a > N:
                    break
                if gmpy2.is_prime(a):
                    if a not in tmp:
                        tmp.append(a)
                        print(a)
            k += 1
        n1 += 1
    return tmp


if __name__ == "__main__":
    print(leyland_primes_oeis(10 ** 10))
