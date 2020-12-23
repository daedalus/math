from gmpy2 import fac,is_prime

def wilson_is_prime(n):
  return ((fac(n-1)+1) % n) == 0

for i in range(1,100):
  print(i,wilson_is_prime(i),is_prime(i))

