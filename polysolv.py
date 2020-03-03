#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPlv3
# Polynomial synthetic division

def poly_synthetic_div(poly,Q):
  lP = len(P)
  R = [0,0,0,0,0]

  for i in range(0,lP):
    if i == 0:
      R[i] = P[i]
    else:
      R[i] = P[i] + Q * R[i-1]
  return R


   
def poly_to_text(poly,d=0):
  lP = len(poly)
  tmp=[]
  for i in range(0,lP):
    if lP-i-1-d > -1:
      if lP-i-1-d == 0:
        tmp.append('%d' %  poly[i])
      else:
        tmp.append('%d^%d' %  (poly[i],lP-i-1-d))
    
  return " + ".join(tmp)

P = [1,1,-11,-5,30]
Q = 2

print "P = ",poly_to_text(P,0)
print "Coefs: P =",P
print "Q =",Q

R = poly_synthetic_div(P,Q)
print "Coefs: R =",R

if R[-1] == 0:
  print("%d is divisor" % Q)
else:
  print("%d is not divisor" % Q)

print "R = ",poly_to_text(R,1)

