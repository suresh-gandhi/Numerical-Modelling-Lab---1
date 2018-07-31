## Deals with trapezoidal and simpson13 integration techniques

import numpy as np
import math

def f(x):
	return 4 * math.exp(4 * x) + 3 * math.exp(3 * x) + 2 * math.exp(2 * x) + math.exp(x)

def g(x):
	return x**(3) + 2 * x + x**(-1)

def trapezoidalIntegration(F, a, b, n):
	h = float(b - a) / n
	ans = F(a) + F(b)
	for i in range(1, n):
		ans += 2 * F(a + i * h)
	ans = ans * (h / 2)
	return ans
	
def simpson13Integration(F, a, b, n):
	h = float(b - a) / n
	ans = F(a) + F(b)
	isOdd = True
	for i in range(1, n):
		if(isOdd):
			coefficient = 4
		else:
			coefficient = 2
		ans += coefficient * F(a + i * h)
		isOdd = not isOdd
	ans = ans * (h / 3)
	return ans

def main():
	print 'using trapezoidal rule for 1st function with n = 10 -> ' + str(trapezoidalIntegration(f, 1, 2, 10))
	print 'using simpson13 rule for 1st function with n = 10 -> ' + str(simpson13Integration(f, 1, 2, 10))
	print 'using trapezoidal rule for 2nd function with n = 10 -> ' + str(trapezoidalIntegration(g, math.e, 5, 10))
	print 'using simpson13 rule for 2nd function with n = 10 -> ' + str(simpson13Integration(g, math.e, 5, 10))
	

if __name__ == '__main__':
	main()
