from math import pi, sqrt, factorial, sin
import numpy

def sin_taylor_0(x):
	result = 0 + (x-0)/factorial(1) - 0*(x-0)**2/factorial(2) \
				- (x-0)**3/factorial(3) + 0*(x-0)**4/factorial(4)
	return result
def sin_taylor_pi_4(x):
	result = 1/sqrt(2) + 1/sqrt(2)*(x-pi/4)/factorial(1) \
			- 1/sqrt(2)*(x-pi/4)**2/factorial(2) - 1/sqrt(2)*(x-pi/4)**3/factorial(3) \
				+ 1/sqrt(2)*(x-pi/4)**4/factorial(4)
	return result
def sin_taylor_pi_2(x):
	result = 1 + 0*(x-pi/2)/factorial(1) \
				- 1*(x-pi/2)**2/factorial(2) \
				- 0*(x-pi/2)**3/factorial(3) + 1*(x-pi/2)**4/factorial(4) 
	return result

tj = numpy.linspace(0, pi/2, 50)

def diff_sin(x, func):
	return func(x)-sin(x)

def make_listOf_diff_sin(tj, func):
	a = []
	for i in tj:
		a.append(diff_sin(i, func))
	return a

#x0 = 0
y0 = make_listOf_diff_sin(tj, sin_taylor_0)
#x0 = pi/4
y1 = make_listOf_diff_sin(tj, sin_taylor_pi_4)
#x0 = pi/2
y2 = make_listOf_diff_sin(tj, sin_taylor_pi_2)

from matplotlib import pyplot as plt

plt.plot(tj, y0, '--', label = 'x0 = 0')
plt.plot(tj, y1, label = 'x0 = pi/4')
plt.plot(tj, y2, '+', label = 'x0 = pi/2')
plt.legend()
plt.xlabel("0 <= x <= pi/2")
plt.ylabel("T(x,x0) - sin(x)")
print("x0* =  pi/4")
plt.show()
