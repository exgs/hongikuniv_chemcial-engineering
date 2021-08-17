from scipy.optimize import minimize_scalar, minimize

def f(x):
	return x + 1 / x - 1

bracets = [0.55, 1.75]
result = minimize_scalar(f, bracets)
print(result)
print(result.x)

print("---\n")
result = minimize(f, [0.7])
print(result)