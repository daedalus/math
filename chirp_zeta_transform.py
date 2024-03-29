# Given the following paper: https://www.nature.com/articles/s41598-019-50234-9

# TODO: Implimentand test functions
# Found function implementation: ToeplitzMultiplyE
# Suplemental paper (at bottom of previous link):
# https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-019-50234-9/MediaObjects/41598_2019_50234_MOESM1_ESM.pdf
#
# Contains functions:
#   ToeplitzMultiplyE
#   ToeplitzMultiplyP
#   CirculantMultiply
#   SkewCirculantMultiply
#
# Depends on FFT and IFFT (import fftw)


def CZT(x, M, W, A):
    N = len(x)
    X, r, c = [] * N, [] * N, [] * M
    for k in range(0, N - 1):
        k2 = k * k
        X[k] = W[((k2) >> 1)] * A[-k] * x[k]
        r[k] = W[-((k2) >> 1)]
    for k in range(0, M - 1):
        c[k] = W[-((k * k) >> 1)]
    X = ToeplitzMultiplyE(r, c, X)
    for k in range(0, M - 1):
        X[k] = W[((k * k) >> 1)] * X[k]
    return X


def ICZT(X, N, W, A):
    M = len(X)
    if M != N:
        raise ("M must == to N")
    n = N
    x, p, u, z = [] * n, [] * n, [] * n, [] * n
    for k in range(0, n - 1):
        x[k] = W[((k * k) >> 1)] * X[k]
    p[0] = 1
    for k in range(0, n - 1):
        p[k] = (p[k - 1]) * (W[k] - 1)
    for k in range(0, n - 1, 2):
        u[k] = (W[((k * k) << 1) - ((n << 1) - 1) + n * (n - 1)]) / (
            p[n - k - 1] * p[k]
        )
    for k in range(1, n - 1, 2):
        u[k] = (
            (W[((k * k) << 1) - ((n << 1) - 1) + n * (n - 1)]) / (p[n - k - 1] * p[k])
        ) * -1
    for j in range(n - 1, 0, -1):
        u1[k] = u[k - j]
    u2 = u[0] + [0] * (n - 1)
    x1 = ToeplitzMultiplyE(u1, z, x)
    x1 = ToeplitzMultiplyE(z, u1, x1)
    x2 = ToeplitzMultiplyE(u, u2, x)
    x2 = ToeplitzMultiplyE(u2, u, x2)
    for k in range(0, n - 1):
        x[k] = (x2[k] - x1[k]) / u[0]
    for k in range(0, n - 1):
        x[k] = A[k] * W[-((k * k) >> 1)] * x[k]
    return x
