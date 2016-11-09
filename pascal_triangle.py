import math

def nk(n,k):
	return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def hexify(i):
	return hex(i).replace('0x','').replace('L','').zfill(64)

for i in range(0,257):
	print bin(nk(256,i))
