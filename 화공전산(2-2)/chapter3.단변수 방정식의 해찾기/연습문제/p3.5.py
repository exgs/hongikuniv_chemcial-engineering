from sympy import *
import math

G =1350 #kg/s-m^2
p0 = 25*101325 #Pa
r = 1.4
density = 15.9 #kg/m^3
C = G * ((r-1)/(2*density * p0 * r))**0.5
print(C)
def f(x, C, r):
	y = x**(1/r)*(1-x**(1-1/r))**0.5 - C
	return y
	
x = Symbol('x')
y = x**(5/7)*((1-x**(1-1/1.4)))**0.5
#(a)
# print(y.subs(x,0))
# print(y.subs(x,1))

#(b)
c = solve(diff(y),x)
print("f'(x) = 0 인 x값 : %f" %c[0])
print("f(%f) = %f " %(c[0], y.subs(x,c[0])))

#(c)
from scipy.optimize import bisect
x1 = bisect(f, 0, c[0], (C,r))
print(x1)
x2 = bisect(f, c[0], 1, (C,r))
print(x2)

## 그래프 점검
# https://www.desmos.com/calculator?lang=ko에서 밑의 함수식 복붙해서 확인!
# x^{\frac{1}{1.4}}\cdot\left(1-x^{\left(1-\frac{1}{1.4}\right)}\right)^{0.5}-0.0804003