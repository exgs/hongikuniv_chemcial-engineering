from scipy.optimize import minimize_scalar, minimize
from numpy.linalg import norm
def f(x):
	[x1, x2] = x
	result = x1**2 + 2*x1*x2 + 3*x2**2 - 4*x1 -5*x2 + 6
	return result

def nabula_f(x):
	[x1, x2] = x
	f1 = 2*x1 + 2*x2 - 4
	f2 = 2*x1 + 6*x2 - 5
	return f1, f2
	
def g(s,x):
	[delta_s0, delta_s1] = nabula_f(x)
	s0 = x[0] - 1*delta_s0*s
	s1 = x[1] - 1*delta_s1*s
	return f([s0, s1])

kmax, eps1, eps2 = 20, 1e-6, 1e-3
k = 1
x = [0,0]
while k < kmax:
	s = minimize(g, [0], args=(x))
	[delta_s0, delta_s1] = nabula_f(x)
	x_new = [x[0] - 1*delta_s0*s.x, x[1] - 1*delta_s1*s.x]
	print("f : %.3f" %f(x_new))
	if (abs(f(x_new)-f(x)) < eps1 and norm([x[0]-x_new[0], x[1]-x_new[1]]) < eps2):
		break
	x = x_new
	k += 1
