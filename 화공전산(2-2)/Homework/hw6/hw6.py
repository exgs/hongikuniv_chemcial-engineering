from math import cos, sin, log, exp, sqrt
from numpy.linalg import norm

def f(x):
	return (exp(x)-2) * (exp(x)-3) * (exp(x)-4) + 0.2
def f_prime(x):
	return (3*exp(3*x)-18*exp(2*x)+26*exp(x))
def f1(x):
	return log(1/26)+log(23.8 + 9*exp(2*x) - exp(3*x)) - f(x)/6.05
def f1_prime(x):
	return (18*exp(2*x)-3*exp(3*x))/(23.8+9*exp(2*x)-exp(3*x)) - f_prime(x)/6.05
	
ebar2, kmax = 1e-6, 100
fmt = "%3d %10.10f"
k = 1
xnew = 0
print(fmt %(k, xnew))
while k < kmax:
	k = k + 1
	xold = xnew
	xnew = f1(xold)
	print(fmt %(k, xnew))
	e2 = norm([xnew-xold])
	if e2 <= ebar2:
		break
print("%.10f" %f1_prime(xnew))
print("%.10f" %f_prime(xnew))