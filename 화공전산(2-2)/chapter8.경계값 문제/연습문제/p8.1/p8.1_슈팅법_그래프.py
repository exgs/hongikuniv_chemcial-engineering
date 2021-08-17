# y(1) = 0 일때, 만 슛팅법이 가능한건가.
def f(t, y):
	f1 = y[1]
	f2 = 1.5*(y[0]**2)
	return f1, f2

def F(z0):
	r = solve_ivp(f, [0,1], [4, z0])
	return r.y[0, -1]
	
#경우에 따라 바꾸시오
z_a = 0, 1000
z_b = -16, 0
z_c = -40, -16
kmax, eps1 = 100, 1e-4

from scipy.integrate import solve_ivp
fmt = "%3d %10.5f %10.5f"

za, zb = z_c[0], z_c[1] #문제 조건에 따라서 이 부분을 수정해준다.

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

print("-----------------------")
import numpy
from matplotlib import pyplot as plt
tj = numpy.linspace(0,1, 21)
sol_z_b = solve_ivp(f, [0,1], [4, -7.9918], t_eval = tj)
sol_z_c = solve_ivp(f, [0,1], [4, -35.89404], t_eval = tj)

fig, ax = plt.subplots(2)
ax[0].plot(sol_z_b.t, sol_z_b.y[0])
ax[1].plot(sol_z_c.t, sol_z_c.y[0])
plt.show()
