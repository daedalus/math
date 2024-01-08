# taken from https://maths.dk/teaching/courses/math357-spring2016/projects/factorization.pdf

import math
import gmpy2


def euler(n):
    a = 0
    end = n
    firstb = -1
    sol = []

    while a < end and len(sol) < 2:
        b2 = n - a**2
        b = gmpy2.isqrt(b2)
        b3 = b2 - b**2
        # print(b2,b,b3)
        if b3 == 0 and a != firstb and b != firstb:
            firstb = b
            sol.append([b, a])
            print((b, a))
        a += 1

    if len(sol) < 2:
        print("sol found is in the form 4k+3")

    a = sol[0][0]
    b = sol[0][1]
    c = sol[1][0]
    d = sol[1][1]

    # a2+b2 = c2+d2
    # a2-c2 = d2-b2 (a-c)(a+c) =(d-b)(+b)
    k = gmpy2.gcd(a - c, d - b)
    h = gmpy2.gcd(a + c, d + b)
    m = gmpy2.gcd(a + c, d - b)
    l = gmpy2.gcd(a - c, d + b)

    # n = (k**2 + h**2)*(m**2 + l**2)

    return (k**2 + h**2) // 4, (l**2 + m**2) // 4


import sys

r = euler(int(sys.argv[1]))
print(r)
print((r[0] * r[1]))
