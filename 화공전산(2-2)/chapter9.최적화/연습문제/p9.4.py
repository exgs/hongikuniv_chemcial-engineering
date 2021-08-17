from scipy.optimize import minimize_scalar, minimize
from numpy.linalg import norm
def f(x):
	[x1, x2] = x
	result = (x1**2 + x2 -11)**2 + (x1 + x2**2 -7)**2
	return result

def nabula_f(x):
	[x1, x2] = x
	f1 = (4*x1**3 + 4*x1*x2 - 44*x1) + 2*(x1 + x2**2 -7)
	f2 = 2*(x1**2 + x2 -11) + 4*x2*(x1 + x2**2 -7)
	return f1, f2
	
def g(s,x):
	[delta_s0, delta_s1] = nabula_f(x)
	s0 = x[0] - 1*delta_s0*s
	s1 = x[1] - 1*delta_s1*s
	return f([s0, s1])

def optimize_variables(x):
	kmax, eps1, eps2 = 20, 1e-6, 1e-3
	k = 1
	while k < kmax:
		s = minimize(g, [0], args=(x))
		[delta_s0, delta_s1] = nabula_f(x)
		x_new = [x[0] - 1*delta_s0*s.x, x[1] - 1*delta_s1*s.x]
		print("x1: %.3f x2: %.3f f : %.3f" %(x_new[0], x_new[1], f(x_new)))
		if (abs(f(x_new)-f(x)) < eps1 and norm([x[0]-x_new[0], x[1]-x_new[1]]) < eps2):
			break
		x = x_new
		k += 1

x = [0, 0]
optimize_variables(x)
x = [0, -1]
optimize_variables(x)
x = [-1, 0]
optimize_variables(x)
x = [-1, -1]
optimize_variables(x)

# from scipy.optimize import minimize
# result = minimize(f, [0,0])
# print(result)
# print(f(result.x))
