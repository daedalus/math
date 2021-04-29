#!/usr/bin/env python3
# Author Dario Clavijo 2021
from gmpy2 import gcd

def multiplicativeOrder(a,n):
   if gcd(a,n) > 1:
     return -1
   k = 2
   while k < n:
     if pow(a,k,n) == 1:
       return k
     k += 1
   return -1

def ZnMultGroup(n):
  i=1
  tmp = []
  while i<n:
    if gcd(i,n) == 1:
      tmp.append(i)
    i+=1
  return tmp

if __name__ == "__main__":
  print("ZnMultGroup(10)",ZnMultGroup(10))
  print("ZnMultGroup(11)",ZnMultGroup(11))
  for i in range(2,10):
    for j in range(i,10):
      if gcd(i,j) == 1:
        print("multiplicativeOrder",i,j,multiplicativeOrder(i,j))
