import math

def subMod(a,n):
    """ Naive modulo implementation with substraction """
    while a <= n:
        n -= a
    return n

def test():
    x = 10
    for i in range(1,11):
        a = subMod(i,x)
        b = x % i
        print(x,i,a,b,a==b)


if __name__ == "__main__":
    test()
