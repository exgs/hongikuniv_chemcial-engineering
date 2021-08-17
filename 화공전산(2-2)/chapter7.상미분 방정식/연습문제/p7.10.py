from math import exp
import numpy as np
from scipy.integrate import solve_ivp

def r(y):
	[C, T] = y
	return C*exp(-10/(273+T))


def f(t, y):
	[C, T] = y
	f0 = -r(y)
	f1 = 1000*r(y) + 10*(20 -T)
	return f0,f1

t0,te = 0,3
y = [1, 16]
sol = solve_ivp(f, [t0, te], y)
print(sol.success)

from matplotlib import pyplot as plt
fig,ax = plt.subplots(2)
fig.suptitle("problem 7.10")
ax[0].set_title("C")
ax[0].plot(sol.t, sol.y[0], 'b')
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_ylabel('C(t)')

ax[1].set_title("T")
ax[1].plot(sol.t, sol.y[1], 'k')
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('T(t)')
plt.tight_layout()
plt.show()
