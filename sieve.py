import math


def sieve_Erathostenes(n):
    sieves = [True for _ in range(0, n)]
    # sieving
    for i in range(2, int(math.sqrt(n))):
        if sieves[i] == True:
            for j in range(0, n):
                h = (i**2) + (j * i)
                if h < n:
                    sieves[h] = False
    return [k for k in range(2, n) if sieves[k] == True]


print((sieve_Erathostenes(121)))
