def f(t, y):
	y0p = y[1]
	y1p = - (y[1] + 1.5 ) * y[0]
	return y0p, y1p

def F(z0):
	r = solve_ivp(f, [0,3], [0, z0])
	return r.y[0, -1]

za, zb = 3, 7 # y'(0) = 3 ~ 7 까지의 범위로 한정한다.
kmax, eps1 = 10, 1e-4

from scipy.integrate import solve_ivp
fmt = "%3d %10.5f %10.5f"
print("   k      y'(0)      y(3)")
print("   k        z0       y(3)")
k = 1
Fa = F(za)
print(fmt %(k, za, Fa))
k = 2
Fb = F(zb)
print(fmt %(k, zb, Fb))

while k < kmax:
	zc = zb - (zb - za) * Fb / (Fb - Fa)
	Fc = F(zc)
	k = k + 1
	print(fmt %(k, zc, Fc))
	if (abs(Fc) <= eps1):
		break
	za, Fa = zb, Fb
	zb, Fb = zc, Fc

