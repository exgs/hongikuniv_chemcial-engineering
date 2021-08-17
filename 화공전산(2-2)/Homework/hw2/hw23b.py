def f(x):
	c = 0.3
	y = 1/x**12 - 1/x**6 - c/x**4
	return y
	
x1, x2 = 0.9, 2
e1 = 1E-4
kmax = 40
k = 1
xa = x1
ya =f(xa)
print("%5s|%10s|%10s|%10s|" %("k", "xk", "yk", "xk-x(k-1)"))
print("%5d %10.4f %10.4f" %(k, xa, ya))
k = 2
xb = x2
yb =f(xb)
x_old = xa
print("%5d %10.4f %10.4f %10.4f" %(k, xb, yb, xb-x_old))
while(k < kmax):
	k = k + 1
	# xc = xb - (xb-xa) * f(xb) / (f(xb)-f(xa)) : 시작지점이 다른 것 뿐이지, 둘 중 아무거나 사용해도 된다.
	xc = xa - (xb-xa) * f(xa) / (f(xb)-f(xa)) #가위치법
	yc = f(xc)
	dx = xc - x_old
	print("%5d %10.4f %10.4f %10.4f" %(k, xc, yc, dx))
	if (abs(yc) <= e1):
		break
	if (ya * yc > 0):
		xa, ya = xc, yc
	else:
		xb, yb = xc, yc
	x_old = xc
input("Press Enter")