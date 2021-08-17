import datetime
from math import log10, sqrt
def f(t, y):
	k1, k2, k3 = 0.04, 10**4, 3*10**7
	f0 = -k1 * y[0] + k2 * y[1] * y[2]
	f1 = k1 * y[0] - k2 * (y[1] * y[2]) - k3 * (y[1] ** 2)
	f2 = k3 * (y[1] ** 2)
	return f0, f1, f2

def g(t,z):
	k1, k2, k3 = 0.04, 10**4, 3*10**7
	g0 = -k1*z[0] + k2*CB*z[1]
	g1 = k3*CB**2
	return g0,g1

from scipy.integrate import solve_ivp
import numpy

t0, te = 0, 40

CB = 2/sqrt(3)*10**-4.5
z = [1, 0]
print("hw4.3")
print(datetime.datetime.now())
rc = solve_ivp(g, [t0, te], z, method='Radau')
print(datetime.datetime.now())
print(rc.success)
print(rc.nfev)
print("-"*20)
print("hw4.2")
y = [1, 0, 0]
print(datetime.datetime.now())
rb = solve_ivp(f, [t0, te], y, method='Radau')
print(rb.success)
print(datetime.datetime.now())
print(rb.nfev)

from matplotlib import pyplot as plt
fig, ax = plt.subplots(3, figsize=(7,8))
fig.suptitle("hw4.3")
ax[0].set_title("CA")
ax[0].plot(rb.t, rb.y[0], label = "hw4.2")
ax[0].plot(rc.t, rc.y[0], label = "hw4.3")
ax[0].set_xticks(numpy.arange(0,5,1))
ax[0].legend()
ax[0].set_xlabel("t")
ax[0].set_ylabel("CA")

ax[1].set_title("CB")
ax[1].plot(rb.t, rb.y[1], label = "hw4.2")
ax[1].plot(rc.t, len(rc.t)*[CB], label = "hw4.3")
ax[1].legend()
ax[1].set_ylabel("t")
ax[1].set_ylabel("CB")

ax[2].set_title("CC")
ax[2].plot(rb.t, rb.y[2], label = "hw4.2")
ax[2].plot(rc.t, rc.y[1], label = "hw4.3")
ax[2].set_xticks(numpy.arange(0,5,1))
ax[2].legend()
ax[2].set_xlabel("t")
ax[2].set_ylabel("CC")
plt.tight_layout()
plt.show()