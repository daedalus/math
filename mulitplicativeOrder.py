#!/usr/bin/env python3
# Author Dario Clavijo 2021
from gmpy2 import gcd

def multiplicative_order(a,n):
   if gcd(a,n) > 1:
     return -1
   k = 2
   while k < n:
     if pow(a,k,n) == 1:
       return k
     k += 1
   return -1

if __name__ == "__main__":
  for i in range(2,10):
    for j in range(i,10):
      if gcd(i,j) == 1:
        print(i,j,multiplicative_order(i,j))
