def f(z):
	[x,y] = z
	return u(x,y)*v(x,y)

def u(x,y):
	A = (x+y+1)**2
	B = (19-14*x -14*y +3*x**3 +6*x*y+3*y**2)
	return (1 + A*B)
def v(x,y):
	A = (2*x - 3*y)**2
	B = (18-32*x+48*y+12*x**2-36*x*y+27*y**2)
	return 30 + A*B

from scipy.optimize import minimize, minimize_scalar
cons = ({'type':'ineq','fun':lambda x : x[0] + 2},
		{'type':'ineq','fun':lambda x : -x[0] + 2},
		{'type':'ineq','fun':lambda x : x[1] + 2},
		{'type':'ineq','fun':lambda x : -x[1] + 2})
result = minimize(f, [0, 0], constraints=cons)
print(result)

