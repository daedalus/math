def legendre(a,p):
  ls = pow(a,(p-1)//2,p)
  if ls == p - 1:
     return -1
  else:
     return ls

for a in range(1,10):
  for p in range(1,10):
    print(a,p,legendre(a,p))
