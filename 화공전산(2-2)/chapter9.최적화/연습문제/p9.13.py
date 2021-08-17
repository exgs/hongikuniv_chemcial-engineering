from math import sqrt, log

# def E_mixed_gibbs(x):
# 	# margules coefficient 바꿔주기
# 	ksi = [2, 3]
# 	n, R, T = 1, 8.314, 400
# 	r= n*R*T*margules(x, ksi)
# 	return r

def margules(x, ksi):
	xa, xb = x, 1-x
	y = xa*log(xa) + xb*log(xb) + xa*xb*(ksi[0]*xa + ksi[1]*xb)
	print("%3d %7.4f %7.4f %10.7f" %(k, xa, xb, y))
	return y

tau = sqrt(1.25) - 0.5
r = 1 - tau

ebar1, ebar2, kmax = 1e-6, 1e-3, 30
xa, xd = 0.03, 0.3
ksi = [2, 3]
dx = xd - xa

k = 1; ya = margules(xa, ksi)
k = 2; yd = margules(xd, ksi)
k = 3; xb = xa + r * dx; yb = margules(xb, ksi)
k = 4; xc = xd - r * dx; yc = margules(xc, ksi)

x_old, y_old = xc, yc #error를 판단하는 기준점 xb,yb 상관없음
while k < kmax:
	k = k + 1
	dx = dx * tau
	if (yb < yc):
		x_new = xa + dx * r; y_new = margules(x_new, ksi)
		xb ,xc ,xd = x_new, xb, xc
		yb, yc, yd = y_new, yb, yc
	else:
		x_new = xd - dx * r; y_new = margules(x_new, ksi)
		xa, xb, xc = xb, xc, x_new
		ya, yb, yc = yb ,yc, y_new
	e1 = abs(y_new - y_old); e2 = abs(x_new - x_old)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
	x_old, y_old = x_new, y_new
