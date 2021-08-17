T1 = 130; V1 = 0.4; p2 = 60; R = 0.0820574; Cv = 1.5*R
a = 1.337; b=3.2*10**-2

from math import log
def f(x):
	[T2, V2] = x
	# f1 = Cv / R * log(abs(T2/T1)) + log(abs((V2-b)/(V1-b)))
	f1 = Cv / R * log(T2/T1) + log((V2-b)/(V1-b))
	f2 = R*T2/(V2-b) - a/V2**2 - p2
	return [f1,f2]
	
def jacobian(x):
	[T2, V2] = x
	j11 = Cv / R * (1/T2)
	j12 = 1/(V2-b)
	j21 = R/(V2-b)
	j22 = -R*T2/(V2-b)**2 + 2*a/(V2**3)
	return([[j11,j12],[j21,j22]])
	
from scipy.optimize import root
sol = root(f, [201, 0.22])
print("scipy.optimize root")
print(sol.x)
print("-"*20)

ebar1, ebar2, kmax = 1e-3, 1e-3, 30
from numpy.linalg import norm, solve
print("numpy.linalg solve, jacobian")
k = 1
x = [200, 0.2]
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
