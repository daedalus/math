#!/usr/bin/env python3
# Author Dario Clavijo 2021

def legendre_symbol(a,p)
  """ legendre symbol computation"""
  
  ls = pow(a,(p-1)//2,p)
  
  if ls == p - 1:
     return -1
  else:
     return ls

def test():
  for a in range(1,10):
    for p in range(1,10):
      print(a,p,legendre_symbol(a,p))

if __name__ == "__main__":
  test()
  
