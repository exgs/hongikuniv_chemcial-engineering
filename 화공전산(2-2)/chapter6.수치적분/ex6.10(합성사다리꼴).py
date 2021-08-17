#page137
from math import exp

def f(x):
	y = x**2*exp(x)
	return y

a, b = 0,3
hmin, eps = 1e-5, 1e-4
h = b-a
TA = f(a) + f(b)
TB = 0
I_T = 0.5*h*TA
h = h/2
while h > hmin:
	ITold = I_T
	x = a+h
	while x < b:
		TB = TB + f(x)
		x = x + 2*h
	I_T = h/2 * (TA + 2*TB)
	err = (I_T - ITold)/3
	print(I_T)
	if (abs(err) < eps):
		break
	h = h/2