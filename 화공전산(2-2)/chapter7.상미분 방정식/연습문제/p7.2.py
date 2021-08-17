from math import sqrt
from scipy.integrate import solve_ivp
import numpy as np
def f(t,y):
	k0 = y[1]
	k1 = t*y[0]
	return k0,k1


t0, te = -8, 3
h = 0.1
y_0 = [0,0]
tj = np.arange(t0, te+h/2, h)
sol = solve_ivp(f,[t0,te], y_0, t_eval= tj)
print(sol.success)
x = sol.t
y0 = sol.y[0]
y1 = sol.y[1]
from matplotlib import pyplot as plt
fig, ax = plt.subplots(3,1) #1차원이 되버렸어...
fig.suptitle("problem 7.1(c)")
ax[0].plot(x, y0)
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_xticks(np.arange(-8,3,2))
ax[0].set_ylabel('y')

ax[1].plot(x, y1)
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_xticks(np.arange(-8,3,2))
ax[1].set_yticks(np.arange(-13,3,5))
ax[1].set_ylabel('y\'')

ax[2].plot(y0, y1)
ax[2].grid()
ax[2].set_xticks(np.arange(-8,3,2))
ax[2].set_xlabel('y')
ax[2].set_ylabel('y\'')
plt.tight_layout()
plt.show()