from math import log, sqrt

# x는 리스트 : x[0] = x1, x[1] = x2 
def f(x):
	[x1,x2] = x
	f1 = log(x1**2 + x2) + x2 -1
	f2 = sqrt(x1) + x1 * x2
	return [f1,f2]

def jacobian(x):
	[x1,x2] = x
	j11 = 2*x1/(x1**2 + x2)
	j12 = 1/(x1**2 + x2) + 1
	j21 = x2 + 1/(2*x1**0.5)
	j22 = x1
	return [[j11,j12],[j21,j22]]

ebar1, ebar2, kmax = 1e-6, 1e-3, 10
from numpy.linalg import norm, solve
k = 1
x = [3.5, 0]
y = f(x)
while k < kmax:
	J = jacobian(x)
	dx = solve(J,y)
	k = k + 1
	x = x - dx
	y = f(x)
	print(x)
	e1, e2 = norm(y), norm(dx)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
