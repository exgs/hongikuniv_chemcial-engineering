def f(x, n):
	sum = 0
	for i in range(n-1):
		sum += (100*(x[i+1] - x[i]**2) + (1 - x[i])**2)
	return (sum)


from scipy.optimize import minimize, minimize_scalar
cons = ({'type':'ineq','fun':lambda x : x[0] + 3},
		{'type':'ineq','fun':lambda x : -x[0] + 3},
		{'type':'ineq','fun':lambda x : x[1] + 3},
		{'type':'ineq','fun':lambda x : -x[1] + 3})

cons2 = ({'type':'ineq','fun':lambda x : x[0] + 3},
		{'type':'ineq','fun':lambda x : -x[0] + 3},
		{'type':'ineq','fun':lambda x : x[1] + 3},
		{'type':'ineq','fun':lambda x : -x[1] + 3},
		{'type':'ineq','fun':lambda x : x[2] + 3},
		{'type':'ineq','fun':lambda x : -x[2] + 3})
#(a)
n = 2
result = minimize(f, [0, 0], args=(n), constraints=cons)
print(result)
#(b)
n = 3
result = minimize(f, [0, 0, 0], args=(n), constraints=cons2)
print(result)

