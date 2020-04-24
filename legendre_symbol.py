#!/usr/bin/env python
# Legendre symbol calculator
# https://en.wikipedia.org/wiki/Legendre_symbol
# https://www.youtube.com/watch?v=X63MWZIN3gM
# Author Dario Clavijo 2020
# GPLv3 

import gmpy2
import math

def factor(n0):
  n = n0
  factors = []
  if gmpy2.is_prime(n) != True:
    for i in range(2,n):
      while n % i == 0:
        n = n // i
        factors.append(i)
  if len(factors) == 0:
    factors = [n]
  print ("factor(%d)=%s" % (n0,str(factors)))
  return factors

def legendre_naive(p,q):
  if p % q == 0:
    r = 0
  else:
    r = -1
    for x in range(0,q):
      y = (x**2) % q
      z = p % q
      #print x,y,z
      if y == z:
        r = 1
        break
  print ("legendre_naive(%d|%d)=%d" % (p,q,r))
  return r

def legendre_prop0(p,q):
   print ("legendre_prop0(%d|%d)" % (p,q))
   phi = (p-1)*(q-1)
   _pow = pow(int(-1),int(phi//4))
   return _pow * legendre_naive(q,p) 
  
def legendre_prop1(p,q):
  print ("legendre_prop1 (2| %d)" % q)
  if p == 2:
    return pow((-1),(((q**2)-1)//8))
  else:
    raise Exception ("p != 2")

def legendre_prop2(ab,q):
   print ("legendre_prop2(%d,%d)"  % (ab,q))
   tmp = 1
   for f in factor(ab):
     if f == 2:
       tmp *= legendre_prop1(2,q)
     else:
       tmp *= legendre_naive(f,q)
   return tmp

def _legendre(p,q):
  r = p % q
  print (">legendre(%d|%d) r=%d" % (p,q,r))
  if r == 0:
    ret = 0
  else:
    p1 = r
    if p1 == 1:
      #if p>q:
      #  ret = legendre_naive(p,q)
      #else:  
      ret = legendre_naive(q,p)
    if p1 == 2:
      ret = legendre_prop1(p1,q)
    else:
       if p1 >2:
          fp1 = factor(p1)[::-1]
          tmp = 1
          for f in fp1:
            #while tmp2 > 1:    
            if f == 2:
              tmp *= legendre_prop1(f,q)
            else:
              tmp *= _legendre(q,f)
          #tmp = legendre_prop2(p1,q) 
          ret = tmp
  print ("<legendre(%d|%d) r=%d -> %d" % (p,q,r,ret))
  return ret

legendre = _legendre

def test():
  pairs = []
  pairs.append((5,331))
  pairs.append((713,1009))
  pairs.append((1009,713))
  pairs.append((12345,331))
  pairs.append((65537,3331))

  def check_pair(pair):  
    p,q = pair
    print("-----")
    a = legendre(p,q)
    b = gmpy2.legendre(p,q)
    txt = "%d %s %d" % (a,(a==b),b)
    txt = txt.replace("True","=").replace("False","!=")
    print (txt)
    print ("------")
    c = legendre(q,p)
    d = gmpy2.legendre(q,p)
    txt = "%d %s %d" % (c,c==d,d)
    txt = txt.replace("True","=").replace("False","!=")
    print (txt)
 
  for pair in pairs:
    check_pair(pair)  

if __name__ == "__main__":
  test()
