from math import pi, sqrt, factorial, sin
from scipy.interpolate import CubicSpline
import numpy

def sin_taylor_pi_4(x):
	result = 1/sqrt(2) + 1/sqrt(2)*(x-pi/4)/factorial(1) \
			- 1/sqrt(2)*(x-pi/4)**2/factorial(2) - 1/sqrt(2)*(x-pi/4)**3/factorial(3) \
				+ 1/sqrt(2)*(x-pi/4)**4/factorial(4)
	return result

tj = numpy.linspace(0, pi/2, 50)

def diff_sin(x, func):
	return func(x)-sin(x)

def make_listOf_diff_sin(tj, func):
	a = []
	for i in tj:
		a.append(diff_sin(i, func))
	return a

def newton_interpolation(x):
	n = 4
	coef = numpy.polyfit(xd, sind, 4)
	return coef[0] * x**4 + coef[1]* x**3 + coef[2]* x**2 + coef[3]* x + coef[4]

def natural_spline(x):
	f = CubicSpline(xd, sind, bc_type='natural')
	return f(x)

# T(x,x0) x0 = pi/4
y1 = make_listOf_diff_sin(tj, sin_taylor_pi_4)

## 표1 사인 함수의 값
xd = [0, pi/6, pi/4, pi/3, pi/2]
sind = [0, 0.5, 1/sqrt(2), sqrt(3)/2, 1]
# 다항식 보간법
y2 = make_listOf_diff_sin(tj, newton_interpolation)
# 자연 스플라인 보간법
y3 = make_listOf_diff_sin(tj, natural_spline)

from matplotlib import pyplot as plt

plt.plot(tj, y1, '-', label = 'T(x,x0*)-sin(x) | x0* = pi/4')
plt.plot(tj, y2, label = 'p4(x)-sin(x)')
plt.plot(tj, y3, ':', label = 'S(x)-sin(x)')
plt.legend()
plt.xlabel("0 <= x <= pi/2")
plt.ylabel("difference")
plt.show()
