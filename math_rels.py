import math

def sgn(x):
  if x == 0:
    return 0
  if x > 0:
    return 1
  if x < 0: 
    return -1

def max(a,b):
  if b > a:
     return b
  else: 
     return a

def min(a,b):
  if b < a:
     return b
  else:
     return a

def close(a,b,e):
  return abs(a-b) < e

a = 2

t = -min(-a,a)
x = max(-a,a) 
y = abs(a)
z = math.sqrt(a**2) 
w = a*sgn(a)

print t == x == y == z == w
