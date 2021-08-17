from math import sqrt
from scipy.integrate import solve_ivp
import numpy as np
def f(t,y):
	return (2+3*t)*sqrt(y)


t0, te = 0,1
h = 0.1
y_0 = 1
tj = np.arange(t0, te+h/2, h)
sol = solve_ivp(f,[t0,te], [y_0], t_eval= tj)
x = sol.t
y = sol.y[0]
from matplotlib import pyplot as plt
plt.figure("p7.1(a)",figsize=(5,4))
plt.title("p7.1(a)")
plt.plot(x, y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()