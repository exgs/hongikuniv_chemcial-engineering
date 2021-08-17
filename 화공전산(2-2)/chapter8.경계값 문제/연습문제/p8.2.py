# y(1) = 0 일때, 만 슛팅법이 가능한건가.
def f(t, y):
	f1 = y[1]
	f2 = y[2]
	f3 = -y[2] * y[0]
	return f1, f2, f3

def G(z0):
	r = solve_ivp(f, [0,1], [0, 0, z0])
	return r.y[0, -1]

za, zb = 0.3, 0.7
kmax, eps1 = 100, 1e-3

from scipy.integrate import solve_ivp
fmt = "%3d %10.5f %10.5f"
print("   k      y'(0)      y(1)")
print("   k        z0       y(1)")
k = 1
Fa = G(za)
print(fmt %(k, za, Fa))
k = 2
Fb = G(zb)
print(fmt %(k, zb, Fb))

while k < kmax:
	zc = (zb + za) / 2
	Fc = G(zc)
	k = k + 1
	print(fmt %(k, zc, Fc))
	if (abs(Fc) <= eps1):
		break
	if (Fa * Fc > 0):
		za, Fa = zc, Fc
	else:
		zb, Fb = zc, Fc 
