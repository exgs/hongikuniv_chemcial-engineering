from math import sqrt
from scipy.integrate import solve_ivp
import numpy as np
def f(t,y):
	k0 = y[1] 
	k1 = -y[0]-y[0]**3
	return k0,k1


t0, te = 0,6
h = 0.1
y = [2,0]
tj = np.arange(t0, te+h/2, h)
sol = solve_ivp(f,[t0,te], y, t_eval= tj)
x = sol.t
y0 = sol.y[0]
y1 = sol.y[1]
from matplotlib import pyplot as plt
plt.figure("p7.1(b)",figsize=(5,4))
plt.title("p7.1(b)")
plt.plot(x, y0)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, y1)
plt.show()