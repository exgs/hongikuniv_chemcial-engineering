from math import exp, log

def f(x):
	y = (exp(x) - log(x))
	return y

from scipy.optimize import minimize_scalar, minimize
bracket = [0.55, 0.8]
# bracket 범위가 커지면 해를 찾지 못함 math domain error
x = minimize_scalar(f, bracket)
print(x)

con = {'type':'ineq','fun':lambda x: x}
x = minimize(f, 0.6, constraints=con)
# 마찬가지로 추정치가 최적해(0.56)에 근접해야 해를 찾아 준다.
print(x)
