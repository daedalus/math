# Author Dario Clavijo 2023
# based on https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
from gmpy2 import *

pi_i = (-2j) * complex(gmpy2.const_pi())


def fft(X):
    if (N := len(X)) == 1:
        return X
    N2 = N >> 1
    E = fft(X[::2])
    O = fft(X[1::2])
    for k in range(0, N2):
        q = exp((pi_i * k) / N) * O[k]
        X[k] = E[k] + q
        X[k + N2] = E[k] - q
    return X
