def f(t, z):
	[x, y] = z
	f0 = -x + x*y
	f1 = y - x*y
	return f0, f1

def F(z0):
	r = solve_ivp(f, [0,1], [0.5, z0])
	return r.y[1, -1]

za, zb = 0, 50 # y'(0) = 3 ~ 7 까지의 범위로 한정한다.
kmax, eps1 = 40, 1e-4

from scipy.integrate import solve_ivp
fmt = "%3d %10.5f %10.5f"
print("   k      y'(0)      y(1)")
print("   k        z0       y(1)")
k = 1
Fa = F(za)
print(fmt %(k, za, Fa))
k = 2
Fb = F(zb)
print(fmt %(k, zb, Fb))

while k < kmax:
	zc = (zb + za) / 2
	Fc = F(zc)
	Gc = Fc - 1  # f(1) = 1 이니깐 Fc = Fc - 1 하면, Fc(x)=0일때 x를 찾는다.
	k = k + 1
	print(fmt %(k, zc, Fc))
	if (abs(Gc) <= eps1):
		break
	if (Fa * Gc > 0):
		za, Fa = zc, Gc
	else:
		zb, Fb = zc, Gc 