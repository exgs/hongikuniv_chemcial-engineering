from math import exp

def f(x):
	y = x**3 * exp((-x**2)/2)
	return y

a, b = 1, 2.6
hmin, eps = 1e-2, 1e-2
h = b-a
TA = f(a) + f(b)
TB = 0
print("%10s %10s" %("hk", "I"))
I_T = 0.5*h*TA
print("%10.5f %10.8f" %(h,I_T))
h = h/2
while h > hmin:
	ITold = I_T
	x = a+h
	while x < b:
		TB = TB + f(x)
		x = x + 2*h
	I_T = h/2 * (TA + 2*TB)
	err = (I_T - ITold)/3
	print("%10.5f %10.8f" %(h,I_T))
	if (abs(err) < eps):
		break
	h = h/2
if (h > hmin):
	print("값을 구했습니다.")
	print("A: %10.8f" %I_T)
else:
	print("값을 구하지 못했습니다.")
input("Press Enter")