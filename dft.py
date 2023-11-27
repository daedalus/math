#!/usr/bin/env python
# Author Dario Clavijo 2017
import math

# Example slow DFT
# 1HZ signal over 8HZ sampling

signal = [0, 0.707, 1, 0.707, 0, -0.707, -1, -0.707]


def dft_slow(signal):

    N = len(signal)

    def Fk(signal, k):
        Freq = 0.0
        for n in xrange(0, N):
            coef = math.exp((-2 * math.pi * k * n) / N)
            Freq += signal[n] * coef
        return Freq

    histogram = []
    for k in xrange(0, N):
        histogram.append(Fk(signal, k))
    return histogram


def nyquist_norm(histogram):
    N = len(histogram)
    return [histogram[n] * 2 for n in range(0, N / 2)]


print nyquist_norm(dft_slow(signal))
