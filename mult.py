def mult(x, y):
    z = 0
    while y > 0:
        z = z + x
        y = y - 1
    return z


def russian_peasant(x, y):
    z = 0
    while y > 0:
        if y % 2 == 1: z = z + x
        x = x << 1
        y = y >> 1
    return z 