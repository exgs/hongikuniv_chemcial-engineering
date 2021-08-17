from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t,y,a,b,w):
	[y0, y1] = y 
	k0 = y1
	k1 = -2*a*y1-y0-b*y0**3 + cos(w*t)
	return k0,k1

def solve_initial(c):
	[y0, y1, a, b, w, te] = c
	tj = np.arange(t0,te+h/2, h)
	sol = solve_ivp(f,[t0,te], [y0, y1], t_eval= tj, args = (a,b,w))
	return sol
h = 0.1
t0 = 0
c1 = [0, 0, 0.01, 320, 5, 10]
c2 = [0, 0, 0.01, -320, 5, 3]
c3 = [1/sqrt(320), 0, 0.01, -320, 5, 1]
c4 = [-1/sqrt(320), 0, 0.01, -320, 5, 10]

sol1 = solve_initial(c1)
sol2 = solve_initial(c2)
sol3 = solve_initial(c3)
sol4 = solve_initial(c4)

from matplotlib import pyplot as plt
fig, ax = plt.subplots(2,2) #1차원이 되버렸어
fig.suptitle("problem 7.7")
ax[0][0].plot(sol1.t, sol1.y[0])
ax[0][0].grid()
ax[0][0].set_xlabel('t')
ax[0][0].set_ylabel('y')

ax[0][1].plot(sol2.t, sol2.y[0])
ax[0][1].grid()
ax[0][1].set_xlabel('t')
ax[0][1].set_ylabel('y')

ax[1][0].plot(sol3.t, sol3.y[0])
ax[1][0].grid()
ax[1][0].set_xlabel('t')
ax[1][0].set_ylabel('y')

ax[1][1].plot(sol4.t, sol4.y[0])
ax[1][1].grid()
ax[1][1].set_xlabel('t')
ax[1][1].set_ylabel('y')

plt.tight_layout()
plt.show()
