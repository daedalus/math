# implementation acording to whikipedia: https://es.wikipedia.org/wiki/C%C3%A1lculo_de_la_ra%C3%ADz_cuadrada

def sqrt(x):
	r = x
	t = 0
	while (t != r):
		t = r
		r = 0.5 (x/r +r)
	return r

# given the x**2-2=0 condition we bruteforce an aproximation to sqrt(2)

def sqrttest():
	target = 2.0
        x = 2.0
        error = 1
        step = 0.5
        lower_error = 1
        i = 0
	c = 0
	last_aprox = None
        while (error != 0):
                i = i + 1
                error = ((x**target)-target)
                x = x - (error * step)

                if error < lower_error:
                        lower_error = abs(error)

                print "Count: %d, Aprox: %s, Error: %s, LowerError: %s" % (i,x,error,lower_error)


sqrttest()
