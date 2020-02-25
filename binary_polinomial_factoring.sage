#!/usr/bin/sage
# Factoring integers representing them with polynomials with order=bits
# Ex: 15 = 2^0 + 2^1 + 2^2 + 2^3 -> (2^0 + 2^1) * (2^1 + 2^2) -> 3*5
# It works well with mersenne primes but not with other composites.
# Author Dario Clavijo 2020
# GPlv3

import sys
sys.setrecursionlimit(100000)

import math
import gmpy2
from gmpy2 import mpz

def int_to_poly(n):
  n = mpz(n)
  tmp="" 
  tmp2=[] 
  bits = n.bit_length()
  for j in range(0,bits): 
    b=int((n >> j) & 1) 
    tmp = str(b) + tmp 
    if b == 1: 
      tmp2.append("x^%d " % (j))
  return "+".join(tmp2)

def factor_int(n,verbose=False):
  if verbose:
    print("converting to poly:")
  poly = SR(int_to_poly(n))
  if verbose:
    print(poly)
    print("finding factors:")
  factored = factor(poly)
  if verbose:
    print(factored)
    print("evaluating terms:")
  factors = []
  terms = str(factored).split(")*")
  ls = len(terms)
  if verbose:
    print(ls)
  if ls > 0:
    for term in terms:
      term = term.replace("(","").replace(")","")
      if verbose:
        print(term)
      factors.append(sage_eval(term,{'x':2}))
  return factors

def test():
  n=2
  ff=0
  nf=0
  while True:
    i = (2**n)-1
    if gmpy2.is_prime(i) == False:
      f = factor_int(i)
      if len(f)> 1:
        ff+=1
      else:
        nf+=1
      print(n,i,ff,nf,f)
    n+=1
test()
