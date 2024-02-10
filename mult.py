def mult(x, y):
    z = 0
    while y > 0:
        z += x
        y -= 1
    return z


def russian_peasant(x, y):
    z = 0
    while y > 0:
        z += x * (y & 1) 
        x <<= 1
        y >>= 1
    return z 
