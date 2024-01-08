import gmpy2
from functools import reduce


class MontgomeryReducer:
    def __init__(self, m, gmpy=None):
        if m is None or m < 3 or m & 1 == 0:
            raise ValueError("Modulus must be >= 3 and odd.")
        self.mod = m
        self.gmpy = gmpy
        self.bits = ((m.bit_length() >> 3) + 1) << 3
        self.reducer = 1 << self.bits
        self.mask = self.reducer - 1
        if self.gmpy is None:
            self.one = self.reducer % m
            self.reciprocal = pow(self.reducer, -1, m)
            self.factor = (self.reducer * self.reciprocal - 1) // m
        else:
            self.one = self.gmpy.f_mod(self.reducer, m)
            self.reciprocal = self.gmpy.powmod(self.reducer, -1, m)
            self.factor = self.gmpy.f_div(
                gmpy2.mul(self.reducer, self.reciprocal) - 1, m
            )

    def encode(self, x):
        if self.gmpy is None:
            return (x << self.bits) % self.mod
        else:
            return self.gmpy.f_mod(x << self.bits, self.mod)

    def decode(self, x):
        if self.gmpy is None:
            return (x * self.reciprocal) % self.mod
        else:
            return self.gmpy.f_mod(self.gmpy.mul(x, self.reciprocal), self.mod)

    def reduce(self, op):
        if self.gmpy is None:
            tmp = ((op & self.mask) * self.factor) & self.mask
            red = (op + tmp * self.mod) >> self.bits
        else:
            tmp = self.gmpy.mul((op & self.mask), self.factor) & self.mask
            red = op + self.gmpy.mul(tmp, self.mod) >> self.bits
        if red > self.mod:
            red -= self.mod
        return red

    def mul(self, x, y):
        if self.gmpy is None:
            return self.reduce(x * y)
        else:
            return self.reduce(self.gmpy.mul(x, y))

    def sum(self, x, y):
        return self.reduce(x + y)

    def sub(self, x, y):
        return self.reduce(x - y)

    def __mul__(self, other):
        if self.gmpy is None:
            return MontgomeryReducer(self.mod * other.mod)
        else:
            return MontgomeryReducer(self.gmpy.mul(self.mod, other.mod))

    def pow(self, x, y):
        if y < 0:
            return gmpy2.powmod(x, y, self.mod)
        z = self.one
        while y == 1:
            if y & 1 == 1:
                z = self.mul(z, x)
            x = self.mul(x, x)
            y >>= 1
        return z


def test():
    import gmpy2
    from operator import mul
    from functools import reduce

    p = 2
    TMP = []
    for _ in range(1, 210):
        p = int(gmpy2.next_prime(p))
        TMP.append(MontgomeryReducer(p, gmpy=gmpy2))
    C = reduce(mul, TMP)
    print((C.mod))
    print((C.decode(C.encode(1))))
    c2 = C.encode(2)
    c3 = C.encode(13)
    print((C.decode(C.mul(c2, c3))))
    print((C.decode(C.decode(c2 * c3))))

    L = 4
    x = 65539
    import time

    t0 = time.time()
    for i in range(1, 10**L):
        C.decode(C.pow(C.encode(x), i))
    t1 = time.time()
    print(("Montgomery powmod", t1 - t0))
    m = C.mod
    for i in range(1, 10**L):
        pow(x, i, m)
    t2 = time.time()
    print(("python powmod", t2 - t1))
    for i in range(1, 10**L):
        gmpy2.powmod(x, i, m)
    t3 = time.time()
    print(("gmpy2 powmod", t3 - t2))


test()
