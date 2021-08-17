from math import cos, pi

def f(x, A, n):
	return (A*n + sigma(x, A, n))

def sigma(x, A, n):
	sum = 0
	for i in range(n):
		sum += (x[i]**2 - A*cos(2*pi*x[i]))
	return (sum)

def g(x, A, n):
	return (A*n + x**2-A*cos(2*pi*x))

from scipy.optimize import minimize, minimize_scalar
#(a)
n, A = 1, 10
x = [-5.12, 5.12]
result = minimize_scalar(g, x, args=(A,n))
print(result)
print("-"*30)
#(b)
n, A = 2, 10
x = [-5.12, 5.12]
result = minimize(f, x, args=(A,n))
print(result)
