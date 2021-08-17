from math import sqrt
from scipy.integrate import solve_ivp
import numpy as np
def f(t,y):
	k0 = y[1]
	k1 = -abs(y[1])*y[1]-y[0]
	return k0,k1


t0, te = 0,10
h = 0.1
y_0 = [1,0]
tj = np.arange(t0, te+h/2, h)
sol = solve_ivp(f,[t0,te], y_0, t_eval= tj)
x = sol.t
y = sol.y[0]
y_2 = sol.y[1]
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2,1) #1차원이 되버렸어...
fig.suptitle("problem 7.1(c)")
ax[0].plot(x, y)
ax[0].grid()
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

ax[1].plot(x, y_2)
ax[1].grid()
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
plt.show()