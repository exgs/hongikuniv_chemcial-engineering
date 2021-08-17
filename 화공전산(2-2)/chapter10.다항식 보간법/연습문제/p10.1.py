def f(x):
	return (1/(1+25*x**2))

def p(x, xd, coef, n): #interpolating polynomial
	y, xx = 0, 1
	for j in range(0, n):
		y = y + coef[0, j] * xx
		xx = xx * (x - xd[j])
	return y


import numpy
tj = numpy.linspace(-1, 1, 11)
n = 11

x = tj
f_x = [f(i) for i in tj]
coef = numpy.zeros((n, n))
for i in range(0, n):
	coef[i,0] = f_x[i]
for j in range(1, n): # newton's divided difference
	for i in range(0, n - j):
		num = coef[i + 1, j - 1] - coef[i, j -1]
		delta_x = x[i + j] - x[i]
		coef[i,j] = num/delta_x

from scipy.interpolate import interp1d
interpol_f = interp1d(tj, [f(i) for i in tj], kind = 'cubic')

from matplotlib import pyplot as plt

plt.plot(tj, [f(i) for i in tj], 'o', label = "real function")
plt.plot(tj, [p(i, tj, coef, n) for i in tj], 'r--', label = "(a) newton")
plt.plot(tj, [interpol_f(i) for i in tj], 'b:', label = "(b) spline")
plt.legend()
plt.tight_layout()
plt.show()
