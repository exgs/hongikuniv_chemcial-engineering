from math import sqrt
from scipy.integrate import solve_ivp
import numpy as np

#(a번)
# a,b,p,q = 1,1,1,-1
#(b번)
a,b,p,q = 1,1,1,1
def f(t,z):
	[x,y] = z
	r = sqrt(x**2+y**2)
	k0 = a*x-b*y-0.5*(p*x-q*y)*r**2 
	k1 = b*x+a*y-0.5*(q*x+p*y)*r**2
	return k0,k1
h = 0.1
t0, te = 0, 7
xy = [0.1, 0]
tj = np.arange(t0,te+h/2, h)
sol = solve_ivp(f,[t0,te], xy, t_eval= tj)
y0 = sol.y[0]
y1 = sol.y[1]
from matplotlib import pyplot as plt
fig, ax = plt.subplots(3,1, figsize=(7,7)) #1차원이 되버렸어...
fig.suptitle("problem 7.3")
ax[0].plot(sol.t, y0)
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_ylabel('x')

ax[1].plot(sol.t , y1)
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('y')
ax[1].set_yticks(np.arange(-1.5,1.5,0.5))

ax[2].plot(y0, y1)
ax[2].grid()
ax[2].set_xlabel('x')
ax[2].set_ylabel('y')
ax[2].set_yticks(np.arange(-1.5,1.5,0.5))
plt.tight_layout()
plt.show()
