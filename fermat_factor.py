#!/usr/bin/env python
# Author Dario Clavijo 2020
# Example taken from https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
# GPLv3

import gmpy2

def fermat(n):
  a = gmpy2.isqrt(n)
  b2 = (a**2) -n
  step=0
  while not gmpy2.is_square(b2):
    a += 1
    b2 = (a**2) -n
    step+=1
    print(n,step,a,b2)
  return a-gmpy2.isqrt(b2),a + gmpy2.isqrt(b2)

def test():
  n=5959
  print ("-"*40)
  a,b= fermat(n)
  print ("-"*40)
  print (n,a,b,n==a*b)

test()
