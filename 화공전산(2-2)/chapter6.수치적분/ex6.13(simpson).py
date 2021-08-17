#page137
from math import tan

def f(x):
	if (x == 0):
		return (1)
	y = tan(x)/x
	return y

a, b = 0, 1.4
hmin, eps = 1e-5, 1e-13
h = (b-a) / 2
SA = f(a) + f(b)
SB = 0
SC = f(a+h)
I_S = h/3*(SA + 2*SB + 4*SC)
h = h/2
while h > hmin:
	ISold = I_S
	SB = SB + SC
	x = a + h
	SC = 0
	while x < b:
		SC = SC + f(x)
		x = x + 2*h
	I_S = h/3 * (SA + 2*SB + 4*SC)
	err = (I_S - ISold)/15
	print("%10.5f   %.15f" %(I_S,err))
	if (abs(err) < eps):
		break
	h = h/2
print(I_S)