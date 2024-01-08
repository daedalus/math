class BarretReduccer:
    """
    https://en.wikipedia.org/wiki/Barrett_reduction
    """

    def __init__(self, m):
        if m <= 0:
            raise ValueError("Modulus must be positive")
        if m & (m - 1) == 0:
            raise ValueError("Modulus must not be a power of 2")
        self.m = m
        self.shift = m.bit_length() << 1
        self.q = (1 << self.shift) // m

    def reduce(self, a):
        # if 0 <= a <= self.m**2: raise ValueError("a must be >0 and < n^2")
        a -= ((a * self.q) >> self.shift) * self.m
        if a >= self.m:
            a -= self.m
        return a


def test():
    br = BarretReduccer(12)
    print((br.reduce(6)))
    print((br.reduce(13)))
    print((br.reduce(18)))
