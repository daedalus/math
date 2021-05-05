# Author Dario Clavijo 2020
# GPLv3
import math


def _min(a, b):
    return 0.5 * (a + b - math.sqrt((a - b) ** 2))


def _max(a, b):
    return 0.5 * (a + b + math.sqrt((a - b) ** 2))


print _min(5, 7)
print _max(5, 7)
