from math import exp, log

def f(x):
	y = (exp(x) - log(x))
	print("%3d %7.4f %10.7f" %(k, x, y))
	return y

from math import sqrt
tau = sqrt(1.25) - 0.5
r = 1 - tau

ebar1, ebar2, kmax = 1e-6, 1e-3, 30
xa, xd = 0.05, 1.15
dx = xd - xa

k = 1; ya = f(xa)
k = 2; yd = f(xd)
k = 3; xb = xa + r * dx; yb = f(xb)
k = 4; xc = xd - r * dx; yc = f(xc)

x_old, y_old = xc, yc #error를 판단하는 기준점 xb,yb 상관없음
while k < kmax:
	k = k + 1
	dx = dx * tau
	if (yb < yc):
		x_new = xa + dx * r; y_new = f(x_new)
		xb ,xc ,xd = x_new, xb, xc
		yb, yc, yd = y_new, yb, yc
	else:
		x_new = xd - dx * r; y_new = f(x_new)
		xa, xb, xc = xb, xc, x_new
		ya, yb, yc = yb ,yc, y_new
	e1 = abs(y_new - y_old); e2 = abs(x_new - x_old)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
	x_old, y_old = x_new, y_new
