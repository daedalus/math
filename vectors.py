#
# Author Dario Clavijo 2016
# GPLv3

import math


def multiply(a, b):
    return [a[0] * b[0], a[1] * b[1]]


def multiplyScalar(a, scalar):
    return [a[0] * scalar, a[1] * scalar]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    ax = a[0]
    ay = a[1]
    az = a[2]
    bx = b[0]
    by = b[1]
    bz = b[2]

    rx = ay * bz - az * by
    ry = az * bx - ax * bz
    rz = ax * by - ay * bx
    return [rx, ry, rz]


def length(vec):
    x = vec[0]
    y = vec[1]
    z = vec[2]
    return math.sqrt(x * x + y * y + z * z)


def normalize(vec):
    x = vec[0]
    y = vec[1]
    z = vec[2]
    squaredLength = x * x + y * y + z * z

    if squaredLength > 0:
        length = math.sqrt(squaredLength)
        vec[0] = vec[0] / length
        vec[1] = vec[1] / length
        vec[2] = vec[2] / length

    return vec


def magnitude(vec):
    res = sum(vec[n] * vec[n] for n in range(0, len(vec)))
    return math.sqrt(res)


def tests():
    vec = [0, 4, -3]
    print length(vec)
    print normalize(vec)

    s = 3
    k = [1, 2]
    j = [2, 3]

    tmp = multiply(k, j)
    print tmp
    print multiplyScalar(tmp, s)

    k = [0, 1, 0]
    j = [1, 0, 0]

    print dot(k, j)
    print cross(k, j)

    print magnitude(j)
    print magnitude(k)
