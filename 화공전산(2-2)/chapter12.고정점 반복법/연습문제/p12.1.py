from math import cos, sin, log, exp, sqrt
from numpy.linalg import norm

def f1(x1):
	return cos(x1)
def f2(x1):
	return exp(2-x1)
def f22(x1):
	return 2-log(x1)
def f3(x1):
	return 1-x1**2
def f33(x1):
	return sqrt(1-x1)
def f333(x1):
	return -sqrt(1-x1)
def f4(x1):
	return 4-exp(1-x1)
def f44(x1):
	return 1-log(4-x1)
	
def f5(x1):
	b = 2
	return (x1-b*(x1**2-3*x1+2))
	
ebar2, kmax = 1e-3, 1000000
fmt = "%3d %10.6f"
k = 1
xnew = 1.3
print(fmt %(k, xnew))
while k < kmax:
	k = k + 1
	xold = xnew
	xnew = f5(xold)
	print(fmt %(k, xnew))
	e2 = norm([xnew-xold])
	if e2 <= ebar2:
		break
print(fmt %(k, xnew))
