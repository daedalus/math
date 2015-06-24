# derivative of f(x)

def __df(f,x,h): 
	r = (f(x + h/2) - f(x-h/2)) / h 
    	return r 

def derivative(f):
	h = 1e-8
	def dx(x): return __df(f,x,h)
	return dx

def g(x):
	return x**2

dg = derivative(g)

# definite integral of f(x)

def integral(f):
	h = 1e-4
	def intf(b,a=0):
		sum = 0
		x = a
		while x<=b:
			sum += h * __df(f,x,h) / 2.0
			x += h
		return sum
	return intf


print 'g(x)=',[g(x) for x in range(11)]

print 'df g(x)=',[dg(x) for x in range(11)]

inv1 = integral(derivative(g))

print 'integral(df g(x))=',[inv1(x) for x in range(11)]

