from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t, z, b1, d1, b2, d2):
	[x, y] = z
	k0 = b1*x - d1*x*y
	k1 = b2*x*y -d2*y
	return k0,k1

def solve_initial(c):
	[z, b1, d1, b2, d2] = c
	tj = np.arange(t0,te+h/2, h)
	sol = solve_ivp(f,[t0,te], z, t_eval= tj, args = (b1, d1, b2, d2))
	return sol
h = 0.1
t0, te = 0, 20
c1 = [[4, 3], 0.16, 0.08, 0.9, 4.5]

sol1 = solve_initial(c1)
print(sol1.success)
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2)
fig.suptitle("problem 7.8")
ax[0].plot(sol1.y[0], sol1.y[1])
ax[0].plot(4, 3, 'o')
ax[0].plot(5, 2, 'o')
ax[0].grid()
ax[0].set_xlabel('x(t)')
ax[0].set_ylabel('y(t)')

ax[1].plot(sol1.t, sol1.y[0], 'b', label = "x(t)")
ax[1].plot(sol1.t, [5]*201, 'b--')
ax[1].plot(sol1.t, sol1.y[1], 'r', label = "y(t)")
ax[1].plot(sol1.t, [2]*201, 'r--')
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('x(t),y(t)')

plt.tight_layout()
plt.show()
