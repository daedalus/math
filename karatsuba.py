import math
digits = lambda n: int(math.log10(n))+1
from functools import cache

@cache
def karatsuba(x, y):
    if (x < 10 or y < 10): return x * y 
    m = max(digits(x), digits(y)) 
    m2 = m // 2
    m3 = 10 ** m2
    a, b = divmod(x, m3)
    c, d = divmod(y, m3)
    z0 = karatsuba(b, d)
    z1 = karatsuba(a + b, c + d)
    z2 = karatsuba(a, c)
    return (z2 * (10 ** (m2 << 1))) + ((z1 - z2 - z0) * m3) + z0

a,b = 132621000145968689486197181919225338865594781061448283090178076569, 6476706838600125160840627922710127689
print(karatsuba(a,b))
print(a*b)
