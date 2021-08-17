from math import sin
from scipy.integrate import solve_ivp
import numpy as np

def f(t,y):
	[y0,y1] = y
	k0 = y1
	k1 = -sin(y0)
	return k0,k1

def solve_initial(xy):
	sol = solve_ivp(f,[t0,te], xy, t_eval= tj)
	return sol
h = 0.1
t0, te = 0, 50
xy1 = [0, 1.99]
xy2 = [0, 2.00]
xy3 = [0, 2.01]
tj = np.arange(t0,te+h/2, h)
sol1 = solve_initial(xy1)
sol2 = solve_initial(xy2)
sol3 = solve_initial(xy3)

from matplotlib import pyplot as plt
fig, ax = plt.subplots(3,1, figsize=(7,7)) #1차원이 되버렸어
fig.suptitle("problem 7.4")
# ax[0].plot(sol1.y[0], sol1.y[1])
ax[0].plot(sol1.t, list(map(sin, sol1.y[0])))
ax[0].grid()
ax[0].set_xlabel('θ')
ax[0].set_ylabel('θ\'')

# ax[1].plot(sol2.y[0], sol2.y[1])
ax[1].plot(sol2.t, list(map(sin, sol2.y[0])))
ax[1].grid()
ax[1].set_xlabel('θ')
ax[1].set_ylabel('θ\'')
ax[1].set_yticks(np.arange(-1.5,1.5,0.5))

# ax[2].plot(sol3.y[0], sol3.y[1])
ax[2].plot(sol3.t, list(map(sin, sol3.y[0])))
ax[2].grid()
ax[2].set_xlabel('θ')
ax[2].set_ylabel('θ\'')
ax[2].set_yticks(np.arange(-1.5,1.5,0.5))
plt.tight_layout()
plt.show()
