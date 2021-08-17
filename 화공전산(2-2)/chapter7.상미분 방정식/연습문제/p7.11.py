from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t, z, tau, k):
	[CA1, CB1, CA2, CB2] = z
	k0 = (CA0 - CA1)/tau - k*CA1
	k1 = -CB1/tau + k*CA1
	k2 = (CA1-CA2)/tau - k*CA2
	k3 = (CB1-CB2)/tau + k*CA2
	return k0,k1,k2,k3

tau = 5
k = 0.25
h = 1
t0, te = 0, 40
CA0 = 20
c1 = [0,0,0,0]

tj = np.arange(t0, te+h/2, h)
sol1 = solve_ivp(f, [t0,te], c1, t_eval=tj, args=(tau, k))
print(sol1.success)

from matplotlib import pyplot as plt
fig, ax = plt.subplots(1)
fig.suptitle("problem 7.11")
ax.set_title("y\'(0)=0")
ax.plot(sol1.t, sol1.y[0], 'r', label= "CA1")
ax.plot(sol1.t, sol1.y[1], 'b--', label= "CB1")
ax.plot(sol1.t, sol1.y[2], 'k:', label= "CA2")
ax.plot(sol1.t, sol1.y[3], 'y', label= "CB2")
ax.legend()
ax.grid()
ax.set_xlabel('t')
ax.set_ylabel('CA1, CA2, CB1, CB2\'')

plt.tight_layout()
plt.show()
