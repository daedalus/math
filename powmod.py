from gmpy2 import next_prime


def powmod(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    e_prime = 0
    while e_prime < exponent:
        c = (c * base) % modulus
        e_prime += 1
    return c


def test(A):
    print(A)
    a = powmod(A[0], A[1], A[2])
    b = pow(A[0], A[1], A[2])
    print(a, b)
    return a == b


print(test((13, 484, 497)))
