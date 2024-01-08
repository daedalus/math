def int_to_limbs(n, base):
    """
    Converts an integer to its limbs (digits in a given base).

    Args:
    - n: the integer to convert
    - base: the base in which to represent the integer

    Returns:
    A list of limbs (digits) representing the integer in the given base.
    """
    limbs = []
    while n > 0:
        n, remainder = divmod(n, base)
        limbs.append(remainder)
    return limbs[::-1]


def limbs_to_int(limbs, base):
    """
    Converts a list of limbs (digits in a given base) to an integer.

    Args:
    - limbs: a list of digits representing the integer in the given base
    - base: the base in which the integer is represented

    Returns:
    An integer representing the value of the given limbs in the given base.
    """
    n = 0
    for digit in limbs:
        n = base * n + digit
    return n
