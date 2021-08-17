from math import exp, log

def f(x):
	value = (exp(x) - log(x))
	return value

x0 = 0.05
y0 = f(x0)
h0 = 0.1
k = 0
kmax = 10
print("x : %.2f y : %.2f" %(x0, y0))
x_old, y_old = x0, y0
while (k < kmax):
	x0 = x0 + h0
	y0 = f(x0)
	print("x : %.2f y : %.2f" %(x0, y0))
	if (y_old < y0):
		break
	h0 = 2*h0
	k += 1
#0.05 <= x_min <= 1.15
