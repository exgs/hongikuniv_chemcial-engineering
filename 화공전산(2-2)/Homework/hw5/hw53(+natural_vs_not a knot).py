from math import pi, sqrt, factorial, sin
from scipy.interpolate import CubicSpline
import numpy

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

def notaknot_spline(x):
	f = CubicSpline(xd, sind)
	return f(x)

## 표1 사인 함수의 값
xd = [0, pi/6, pi/4, pi/3, pi/2]
sind = [0, 0.5, 1/sqrt(2), sqrt(3)/2, 1]
tj = numpy.linspace(0, pi/2, 50)

# 자연 스플라인
y1 = make_listOf_diff_sin(tj, natural_spline)
# not a knot 보간법
y2 = make_listOf_diff_sin(tj, notaknot_spline)

# 다항식 보간법
y3 = make_listOf_diff_sin(tj, newton_interpolation)

from matplotlib import pyplot as plt

plt.plot(tj, y1, ':', label = '3th natural spline')
plt.plot(tj, y2, label = '3th not a knot spline')
plt.plot(tj, y3, '--', label = 'newton interpolation')
plt.legend()
plt.xlabel("0 <= x <= pi/2")
plt.ylabel("difference")
plt.show()
