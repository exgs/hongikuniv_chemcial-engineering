from math import exp, log

def f(x):
	y = (exp(x) - log(x))
	return y


ebar1, ebar2, kmax = 1e-6, 1e-3, 30
xa, xb, xc = 0.55, 0.85, 1.15

k = 1; ya = f(xa)
print("%3d %7.4f %10.7f" %(k, xa, ya))
k = 2; yb = f(xb)
print("%3d %7.4f %10.7f" %(k, xb, yb))
k = 3; yc = f(xc)
print("%3d %7.4f %10.7f" %(k, xc, yc))

x_old, y_old = xb, yb
while k < kmax:
	k+=1
	p1 = (xa**2 - xb**2) * yc \
		+ (xb**2 - xc**2) * ya \
		+ (xc**2 - xa**2) * yb
	p2 = (xa - xb)*yc + (xb -xc)*ya + (xc -xa)*yb
	x_new = p1/(2*p2)
	y_new = f(x_new)
	print("%3d %7.4f %10.7f" %(k, x_new, y_new), end = " ")
	if (x_new < xb):
		if (y_new < yb):
			xb, xc = x_new, xb
			yb, yc = y_new, yb
			print("Case 1(a)")
		else:
			xa = x_new
			ya = y_new
			print("Case 1(b)")
	else:
		if (y_new < yb):
			xa, xb = xb, x_new
			ya, yb = yb, y_new
			print("Case 2(a)")
		else:
			xc = x_new
			yc = y_new
			print("Case 2(b)")
	if (abs(y_new - y_old) < ebar1 and (abs(x_new - x_old)) < ebar2):
		break
	x_old, y_old = x_new, y_new
