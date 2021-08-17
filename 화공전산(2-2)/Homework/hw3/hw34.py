from math import exp
from math import inf
def f(x):
	y = x**3 * exp((-x**2)/2)
	return y

from scipy.integrate import quad
r = quad(f, 0, inf)
print("Answer : %10.8f" %r[0])
input("Press Enter")
