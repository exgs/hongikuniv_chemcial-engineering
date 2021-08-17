import math

def g(Ma, r):
	y = 1/Ma**2 - (r+1)/2*math.log((r-1)/2 + 1/Ma**2)
	return y

def func(Ma, L): #관설비에 상수값들 함수 내부에서 정의하고 있음
	r = 1.32
	Ma_a = 0.06
	Ma_b = Ma
	L = L*100/2.54
	f = 0.0035
	Di = 40
	y = (g(Ma_a,r)-g(Ma_b,r))/r - 4*f*L/Di
	return y

from scipy.optimize import newton	
L=14000
Ma_b = newton(func, 0.06, None, (L,))
print(Ma_b)
L=12000
Ma_b = newton(func, 0.06, None, (L,))
print(Ma_b)