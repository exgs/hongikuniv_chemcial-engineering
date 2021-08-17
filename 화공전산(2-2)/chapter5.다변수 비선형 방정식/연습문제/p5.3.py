from math import log, sqrt, sin, cos, exp
# x는 리스트 : x[0] = x1, x[1] = x2 
def p_gas(x):
	[T,a,b,c,d] = x
	a, b, c ,d = a, b*(10**3), c, d*(10**-6)
	p_gas = exp(a-(b/T)-c*log(T)+d*(T**2))
	# p_gas = exp(a-b/(T+c)+d*T)
	return p_gas

def f(y):
	[y1, y2, y3, T] = y
	x1, x2, x3 = 1/7, 2/7, 4/7 #몰 비율 꼭 변경할 것
	# global pt
	pt = 1
	pt_local = pt
	f1 = x1*p_gas([T,71.581,6.4862,9.2194,6.9844])-y1 * pt_local
	f2 = x2*p_gas([T,65.419,6.7298,8.1790,5.3017])-y2 * pt_local
	f3 = x3*p_gas([T,77.194,7.7412,9.8693,6.0770])-y3 * pt_local
	f4 = 1 - (y1 + y2 + y3)
	return [f1,f2,f3,f4]


from scipy.optimize import root
# pt = 1
sol = root(f, [0.1, 0.1, 0.8, 400])
print(sol)