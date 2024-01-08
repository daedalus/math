# Author Dario Clavijo 2023
# based on https://en.wikipedia.org/wiki/Ramanujan%27s_sum

from gmpy2 import *

ipi2 = (2j) * complex(gmpy2.const_pi())


def c(q, n):
    nipi2 = ipi2 * n
    return sum(exp(nipi2 * (a / q)) for a in range(1, q + 1) if gcd(a, q) == 1)


print([c(1, n).real for n in range(1, 31)])
