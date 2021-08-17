from scipy.optimize import minimize

def f(x):
	return 2*x[0]**2 + x[1]**2 + x[2]**2

cons = ({'type' : 'eq', 'fun': lambda x: x[0] + 2*x[1] + x[2] - 16},
		{'type' : 'ineq', 'fun': lambda x: x[0] + x[1] + 2*x[2] - 17})

result = minimize(f, [0,0,0], constraints=cons)
print(result)