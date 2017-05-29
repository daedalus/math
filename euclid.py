def gcd1(a, b)
	while b != 0
    		t = b 
		b = a % b 
		a = t 
	return a

def gcd2(a,b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a

def gcd3(a, b):
	if b = 0
       		return a; 
	else
		return gcd(b, a % b)
