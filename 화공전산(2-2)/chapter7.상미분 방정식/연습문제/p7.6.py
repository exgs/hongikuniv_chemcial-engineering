from math import sin
from scipy.integrate import solve_ivp
import numpy as np

def f(t,y):
	[y0,y1] = y
	k0 = y1
	k1 = 6*y0**2+t
	return k0,k1

def solve_initial(xy):
	sol = solve_ivp(f,[t0,te], xy, t_eval= tj)
	return sol
h = 0.1
t0, te = 0, 2
xy1 = [0, 0]
tj = np.arange(t0,te+h/2, h)
sol1 = solve_initial(xy1)
from matplotlib import pyplot as plt
fig, ax = plt.subplots(1,1, figsize=(7,7)) #1차원이 되버렸어
fig.suptitle("problem 7.6")
ax.plot(sol1.t, sol1.y[0], 'k')
ax.grid()
ax.set_xlabel('t')
ax.set_ylabel('y')
plt.tight_layout()
plt.show()
