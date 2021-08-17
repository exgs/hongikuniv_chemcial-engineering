from math import sin
from scipy.integrate import solve_ivp
import numpy as np

def f(t,y):
	[y0,y1] = y
	k0 = y1
	k1 = m *(1-y0**2)*y1 -y0
	return k0,k1

def solve_initial(xy):
	sol = solve_ivp(f,[t0,te], xy, t_eval= tj)
	return sol
h = 0.1
m = 1
t0, te = 0, 50
xy1 = [0, 1]
xy2 = [2,-2]
tj = np.arange(t0,te+h/2, h)
sol1 = solve_initial(xy1)
sol2 = solve_initial(xy2)
print(sol1.y[0,0], sol1.y[1,0])
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2,1, figsize=(7,7)) #1차원이 되버렸어
fig.suptitle("problem 7.5")
ax[0].plot(sol1.y[0], sol1.y[1])
ax[0].plot(sol1.y[0,0], sol1.y[1,0],'ro')
ax[0].grid()
ax[0].set_xlabel('θ')
ax[0].set_ylabel('θ\'')

ax[1].plot(sol2.y[0], sol2.y[1])
ax[1].plot(sol2.y[0,0], sol2.y[1,0],'ro')
ax[1].grid()
ax[1].set_xlabel('θ')
ax[1].set_ylabel('θ\'')

plt.tight_layout()
plt.show()
