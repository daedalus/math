"""
https://en.wikipedia.org/wiki/Newton%27s_method
"""
def f(x):             
	return x**2 - 2   # f(x) = x^2 - 2

def f_prime(x):
	return 2*x        # f'(x) = 2x

def newtons_method(
    x0,               # The initial guess
    f,                # The function whose root we are trying to find
    f_prime,          # The derivative of the function
    tolerance,        # 7-digit accuracy is desired
    epsilon,          # Do not divide by a number smaller than this
    max_iterations,   # The maximum number of iterations to execute
    ):
	for _ in range(max_iterations):
		y = f(x0)
		yprime = f_prime(x0)
		if abs(yprime) < epsilon:       # Stop if the denominator is too small
		    break
		x1 = x0 - y / yprime            # Do Newton's computation
		if abs(x1 - x0) <= tolerance:   # Stop when the result is within the desired tolerance
		    return x1                   # x1 is a solution within tolerance and maximum number of iterations
		x0 = x1                         # Update x0 to start the process again
	return None
