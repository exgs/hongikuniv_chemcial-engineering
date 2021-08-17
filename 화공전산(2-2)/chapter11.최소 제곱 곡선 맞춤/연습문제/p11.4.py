from math import log, exp

def f_absolute(T, a, b, c):
	sol = 10**(a - b/(T-c))
	return sol
def f_relative(T, a, b, c):
	sol = (a - b/(T-c))
	return sol

def fun(coef, Td, pd):
	evec = []
	for i in range(0, n):
		ei = coef[0] - coef[1] / (Td[i] - coef[2]) - log(pd[i])
		evec.append(ei)
	return evec
n = 10
Td = [-73.8, -54.3, -44.7, -34.3, -22.5, -15.3, -5.1, 10.4, 28, 46.5]
pd = [1, 5, 10, 20, 40, 60, 100, 200, 400, 760]
coef = [0, 0, 0]
from scipy.optimize import least_squares
r = least_squares(fun, coef, args = (Td, pd))
a = r.x[0]; b = r.x[1]; c = r.x[2]

import numpy
tj1 = numpy.linspace(50, 400, 51)
from matplotlib import pyplot as plt
# plt.plot(Td, list(map(lambda x : log(x), pd)))
# plt.plot(tj1, [f_relative(i,a,b,c) for i in tj1], '+')
# plt.yscale('log')
# plt.show()

fig, ax = plt.subplots(2)
ax[0].plot(Td, pd)
ax[0].plot(tj1, [f_absolute(i,a,b,c) for i in tj1], '+')

ax[1].plot(Td, list(map(lambda x : log(x), pd)))
ax[1].plot(tj1, [f_relative(i,a,b,c) for i in tj1], '+')
ax[1].set_yscale('log')
plt.show()