from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t, z):
	[x, y0, y1] = z
	k0 = y0 - x
	k1 = y1
	k2 = 1-x*y0
	return k0,k1,k2


h = 0.1
t0, te = 0, 2
c1 = [0, 1, 0]
c2 = [0, 1, -1]
tj = np.arange(t0, te+h/2, h)
sol1 = solve_ivp(f,[t0,te], c1,t_eval=tj)
sol2 = solve_ivp(f,[t0,te], c2,t_eval=tj)

print(sol1.success)
print(sol2.success)
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2)
fig.suptitle("problem 7.13")
ax[0].set_title("y\'(0)=0")
ax[0].plot(sol1.t, sol1.y[0], 'r', label = "x(t)")
ax[0].plot(sol1.t, sol1.y[1], 'b--', label = "y(t)")
ax[0].plot(sol1.t, sol1.y[2], 'k:', label = "y'(t)")
ax[0].legend()
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_ylabel('x,y,y\'')

ax[1].set_title("y\'(0)=-1")
ax[1].plot(sol2.t, sol2.y[0], 'r', label = "x(t)")
ax[1].plot(sol2.t, sol2.y[1], 'b--', label = "y(t)")
ax[1].plot(sol2.t, sol2.y[2], 'k:', label = "y'(t)")
ax[1].legend()
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('y')
plt.tight_layout()
plt.show()
