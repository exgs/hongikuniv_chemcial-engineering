import datetime
from math import log10
def f(t, y):
	k1, k2, k3 = 0.04, 10**4, 3*10**7
	f0 = -k1 * y[0] + k2 * y[1] * y[2]
	f1 = k1 * y[0] - k2 * (y[1] * y[2]) - k3 * (y[1] ** 2)
	f2 = k3 * (y[1] ** 2)
	return f0, f1, f2

from scipy.integrate import solve_ivp
import numpy
y = [1, 0, 0]
t0 , te = 0, 40
h = 0.01
a = [1e-4,1e-3,1e-2, 1e-1, 1, 10, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]
rb = solve_ivp(f, [a[0], a[-1]], [1,0,0], t_eval=a, method='Radau')


print(rb.success)
print(rb.t)

from matplotlib import pyplot as plt
t = list(map(log10,a))
fig, ax = plt.subplots(3, figsize=(7,8))
fig.suptitle("hw4.2")
ax[0].set_title("CA")
ax[0].plot(t, rb.y[0], label = "CA")
ax[0].legend()
ax[0].set_xlabel("t")
ax[0].set_ylabel("CA")

ax[1].set_title("CB")
ax[1].plot(t, rb.y[1], label = "CB")
ax[1].legend()
ax[1].set_ylabel("t")
ax[1].set_ylabel("CB")

ax[2].set_title("xe = 1")
ax[2].plot(t, rb.y[2], label = "CC")
ax[2].legend()
ax[2].set_xlabel("t")
ax[2].set_ylabel("CC")
plt.tight_layout()
plt.show()