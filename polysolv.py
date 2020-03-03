#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPlv3
# Polynomial synthetic division

import gmpy2
from gmpy2 import mpz

def sanitize(s):
  return s.replace(" 0x^1 "," ").replace("+ -","- ").replace("1x","x").replace(" + - "," - ")

def factors(n):
  result = []
  n = mpz(n)
  for i in range(1, gmpy2.isqrt(n) + 1):
    div, mod = divmod(n, i)
    if not mod:
      result.append(i)
  return result

def poly_synthetic_div(P,Q):
  lP = len(P)
  R = [0] * lP

  for i in range(0,lP):
    if i == 0:
      R[i] = P[i]
    else:
      R[i] = P[i] + Q * R[i-1]
  return R

def get_rationals(poly,grade):
   tmp = []
   lP = len(poly)
   d = factors(abs(poly[-1]))
   if d==[]: 
     d=[abs(poly[-1])]
   n = factors(abs(grade-poly[0]))
   if n==[]: 
     n=[abs(poly[0])]
   #print d
   #print n
   for d_ in d:
     for n_ in n:
       div = float(d_)/n_
       if div > 0:
         tmp.append(div)
   tmp2=[]
   for r in set(sorted(tmp)):
     tmp2.append(r)
     tmp2.append(-r)
   return tmp2

def poly_to_text(poly,grade=0):
  lP = len(poly)
  tmp=[]
  for i in range(0,lP):
    if grade-i > -1:
      if grade-i == 0:
        tmp.append('%d' %  poly[i])
      else:
        tmp.append('%dx^%d' %  (poly[i],grade-i))
    
  return sanitize(" + ".join(tmp))

def poly_synthetic_div_complete_step(poly,grade):
  print "-"*60
  print "Grade:",grade
  print "P = ",poly_to_text(poly,grade)
  print "Coefs: P =",poly
  rationals = get_rationals(poly,grade)
  print "rationals:",rationals
  term = []
  if len(rationals) > 0:
    for Q in rationals:
      R = poly_synthetic_div(poly,Q)
      if R[-1] == 0:
        print "Q =",Q
        print("%d is divisor" % Q)
        print "Coefs: R =",R
        print "R = ",poly_to_text(R,grade-1)
      if R[-1] == 0:
        term = ["(x + %d)" % -Q]
        #break 
        return R[:-1],term
    print "No divisor found"
    return None 
  else:
    print "No rationals"  
  return None    

def factor_poly(Poly,Grade):
  P = Poly
  terms = []
  for grade in range(Grade,1,-1):
    result = poly_synthetic_div_complete_step(P,grade)
    if result != None:
      P,term = result
      if term == []:
        break
      else:
        terms += term
    else:
        break
  terms += ["(%s)" % poly_to_text(P,grade)]
  print "="*60
  s = sanitize("".join(terms))
  print "Result:",s

P = [1,1,-11,-5,30]

factor_poly(P,4)
