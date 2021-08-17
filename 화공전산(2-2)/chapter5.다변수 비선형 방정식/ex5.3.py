from math import log, sqrt
# x는 리스트 : x[0] = x1, x[1] = x2 
def f(x):
	[x1,x2] = x
	f1 = log(x1**2 + x2) + x2 -1
	f2 = sqrt(x1) + x1 * x2
	return [f1,f2]

from scipy.optimize import root
sol = root(f, [3.5,0])
print(sol)
print("-"*30)
print(sol.x)
