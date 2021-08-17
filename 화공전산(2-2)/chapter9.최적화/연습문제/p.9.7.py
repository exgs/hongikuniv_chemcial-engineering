def f(z):
	[x,y] = z
	part1 = (1.5 -x + x*y)**2
	part2 = (2.25-x+x*y**2)**2
	part3 = (2.625 -x +x*y**3)**2
	return  part1 + part2 + part3

from scipy.optimize import minimize, minimize_scalar
cons = ({'type':'ineq','fun':lambda x : x[0] + 4.5},
		{'type':'ineq','fun':lambda x : -x[0] + 4.5},
		{'type':'ineq','fun':lambda x : x[1] + 4.5},
		{'type':'ineq','fun':lambda x : -x[1] + 4.5})
result = minimize(f, [0, 0], constraints=cons)
print(result)

