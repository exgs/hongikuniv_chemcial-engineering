from math import cos, sin, log, exp, sqrt
from numpy.linalg import norm

def f1(x1):
	return x1-b*(x1**2-4)
	
ebar2, kmax = 1e-3, 10000
b = 0.7
fmt = "%3d %10.6f"
k = 1
xnew = 1
print(fmt %(k, xnew))
while k < kmax:
	k = k + 1
	xold = xnew
	xnew = f1(xold)
	# print(fmt %(k, xnew))
	e2 = norm([xnew-xold])
	if e2 <= ebar2:
		break
print(fmt %(k, xnew))
