from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np

def f(t, c):
	[x, y, z] = c
	k0 = 10*(y-x)
	k1 = x*(28-z) - y
	k2 = x*y -8/3*z
	return k0, k1, k2

h = 0.1
t0, te = 0, 30
c1 = [5, 0, -5]
c2 = [0, 0, 27]
c3 = [0, 0.01, 27]
tj = np.arange(t0, te+h/2, h)
sol1 = solve_ivp(f,[t0,te], c1, t_eval=tj)
sol2 = solve_ivp(f,[t0,te], c2, t_eval=tj)
sol3 = solve_ivp(f,[t0,te], c3, t_eval=tj)

print(sol1.success)
print(sol2.success)
print(sol3.success)

def print_graph(problem_number, sol):
	if (problem_number == "(a)"):
		i = 0
	elif(problem_number == "(b)"):
		i = 1
	elif(problem_number == "(c)"):
		i = 2
	ax[i][0].plot(sol.t, sol.y[0], 'k', label = "x(t)")
	ax[i][1].plot(sol.t, sol.y[1], 'k', label = "y(t)")
	ax[i][2].plot(sol.t, sol.y[2], 'k', label = "z(t)")
	for j in range(3):
		ax[i][j].set_title(problem_number)
		ax[i][j].legend()
		ax[i][j].grid()

from matplotlib import pyplot as plt
fig, ax = plt.subplots(3,3, figsize=(13,13))
fig.suptitle("problem 7.9")
print_graph("(a)", sol1)
print_graph("(b)", sol2)
print_graph("(c)", sol3)
plt.tight_layout()
plt.show()
