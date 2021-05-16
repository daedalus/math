# /usr/bin/env python3
# Author Darío Clavijo 2021

from gmpy2 import fib
from sympy import *

"""
General formula for fibonacci numbers
Fn   = Fn-1 + Fn-2
Fn-1 = Fn-1 + 0

Matrix from the system:
A = |1 1|
    |1 0|

Identity matrix:
I = |1 0|
    |0 1|

Definition of eigenvectors:
(A-λI)v = 0

Aplying definition we get:
A-λI = |1-λ 1|
       |1  -λ|

Solving the determinant:
(1-λ)(-λ)-1 = 0
λ^2 - λ -1 = 0

By bhaskara:

λ1 = (1 + sqrt(5)) / 2
λ2 = (1 - sqrt(5)) / 2
"""

def find_fibonacci_eigenvalues():
  "It computes lambda(λ) from: (A-λI)v = 0 " 
  _lambda = symbols('λ') # Lambda escalar placeholder
  A = Matrix(([1, 1], [1, 0])) # Fibonacci general equation matrix
  I = Matrix(([1, 0], [0, 1])) # Identity matrix
  L = _lambda * I # Lambda diagonal 
  E = A-L # Resulting matrix = A-λI
  print("A:",A,"\nI:",I,"\nL:",L,"\nE:",E)
  D = E.det() # compute the matrix determinant
  print("D:",D)
  lambdas = solve(D) # Get roots, solve equation by bhaskara
  la0 = lambdas[0] # root 0
  la1 = lambdas[1] # root 1
  print("λ0:",la0,"\nλ1:",la1)
  return (la0,la1)

def binet_fib_eig(la0,la1,k):
  ik = pow(la0,k) - pow(la1,k) / (la0 -la1) # Binet's formula: (a^n-b^n)/(a-b)
  return round(ik)

def test():
  la0,la1 = find_fibonacci_eigenvalues()
  for i in range(3,30):
    a = fib(i)
    b = binet_fib_eig(la0,la1,i)
    print(i,a,b,a==b)


def test2():
  return

#if __name__ == "__main__":
#  test()
