from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t, z):
	[x0, x1, y] = z
	k0 = x1
	k1 = y**2 - x0
	k2 = x0**2 - y
	return k0,k1,k2


h = 0.1
t0, te = 0, 1
c1 = [1, -2, 1]
c2 = [1, -4, 1]
tj = np.arange(t0, te+h/2, h)
sol1 = solve_ivp(f,[t0,te], c1,t_eval=tj)
sol2 = solve_ivp(f,[t0,te], c2,t_eval=tj)

print(sol1.success)
print(sol2.success)
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2)
fig.suptitle("problem 7.14")
ax[0].set_title("x\'(0)=-2")
ax[0].plot(sol1.t, sol1.y[2], 'k')
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_ylabel('y(t)')

ax[1].set_title("x\'(0)=-4")
ax[1].plot(sol2.t, sol2.y[2], 'k')
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('y(t)')
plt.tight_layout()
plt.show()
