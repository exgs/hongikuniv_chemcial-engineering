from math import cos, sin, log
from numpy.linalg import norm

def g1(x1, x2):
	return 4 - cos(x1) - sin(x2)
def g2(x1, x2):
	return beta * log(x1 + x2)

beta, ebar2, kmax = 1.067, 1e-6, 50
fmt = "%3d %10.6f %10.6f"
k = 1
x1new, x2new = 2, 1
print(fmt %(k, x1new, x2new))
while k < kmax:
	k = k + 1
	x1old, x2old = x1new, x2new
	x1new = g1(x1old, x2old)
	x2new = g2(x1old, x2old)
	#x2new = g2(x1new, x2old) gauss-seidel
	print(fmt %(k, x1new, x2new))
	e2 = norm([x1new-x1old, x2new-x2old])
	if e2 <= ebar2:
		break
