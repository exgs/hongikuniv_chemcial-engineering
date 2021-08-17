from math import cos
from scipy.integrate import solve_ivp
import numpy

def f(t, y):
	y0 = y[1]
	y1 = -y[1] - cos(y[0])
	return y0, y1

def F(z0):
	r = solve_ivp(f, [0,3], [0, z0])
	return r.y[0, -1]

za, zb = 1, 2 # y'(0) = 1 ~ 2 까지의 범위로 한정한다.
kmax, eps1, eps2 = 20, 1e-6, 1e-6
fmt = "%3d %10.5f %10.5f"
print("   k      y'(0)      y(3)")
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

# 슈팅법으로 구한 y'(0)값을 이용해서 미분방정식을 초기값으로 푼다.
tj = numpy.linspace(0,3,31)
result = solve_ivp(f, [0,3], [0, zc], t_eval = tj)

from matplotlib import pyplot as plt
plt.plot(result.t, result.y[0])
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
