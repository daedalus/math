def gcd1(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def gcd2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd3(a, b):
    return a if b == 0 else gcd(b, a % b)
