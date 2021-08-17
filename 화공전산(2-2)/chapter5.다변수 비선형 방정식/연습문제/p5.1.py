from math import log, sqrt, sin, cos, exp
# x는 리스트 : x[0] = x1, x[1] = x2 
def f(x):
	[x1,x2] = x
	f1 = 0.5*x1**2 + 0.08*x2 - 0.5*sin(x1*x2)
	f2 = 5.2*x1 -0.87*x2 - 0.92*exp(2*x1) + 2.5
	return [f1,f2]

from scipy.optimize import root
sol = root(f, [0,0])
print(sol)
print("-"*30)
print(sol.x)
