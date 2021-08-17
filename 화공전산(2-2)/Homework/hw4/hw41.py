import numpy as np
from scipy.integrate import solve_ivp

def f(x,y):
	[y0, y1] = y
	f0 = y1
	f1 = (2*x-6*y0)/(1-x**2)
	return f0, f1
	
def exact_f(x):
	return 1-3*x**2

def solve_differential_by_RK4(xe):
	tj = np.arange(x0,xe+h/2,h)
	sol = solve_ivp(f, [x0,xe], y, t_eval = tj)	
	return sol

def solve_differential_by_LSODA(xe):
	tj = np.arange(x0,xe+h/2,h)
	sol = solve_ivp(f, [x0,xe], y, t_eval = tj, method = 'LSODA')	
	return sol
	

h = 0.1
y = [1, 0]
x0, xe1, xe2, xe3 = 0, 0.9, 1.1, 1
r1 = solve_differential_by_RK4(xe1)
r2 = solve_differential_by_RK4(xe2)
# r3 = solve_differential_by_RK4(xe3)에서는 해답을 찾지 못한다.
r3 = solve_differential_by_LSODA(xe3)
print("xe = 0.9 일때, y(xe) = %5.2f" %r1.y[0,-1])
print("xe = 1.1 일때, y(xe) = %5.2f" %r2.y[0,-1])


from matplotlib import pyplot as plt
fig, ax = plt.subplots(3, figsize=(7,8))
fig.suptitle("hw4.1")
ax[0].set_title("xe = 0.9")
ax[0].plot(r1.t, r1.y[0], 'ko', markerfacecolor = 'w', label = "numerical soluton")
ax[0].plot(r1.t, list(map(exact_f, r1.t)), 'r', label = "exact solution")
ax[0].legend()
ax[0].set_xticks(np.arange(x0,xe1+h/2,h))
# ax[0].set_xabel("x")
ax[0].set_ylabel("y(x)")

ax[1].set_title("xe = 1.1")
ax[1].plot(r2.t, r2.y[0], 'ko', markerfacecolor = 'w', label = "numerical soluton")
ax[1].plot(r2.t, list(map(exact_f, r2.t)), 'r', label = "exact solution")
ax[1].legend()
# ax[1].set_xlabel("x")
ax[1].set_xticks(np.arange(x0,xe2+h/2,h))
ax[1].set_ylabel("y(x)")

ax[2].set_title("xe = 1")
ax[2].plot(r3.t, r3.y[0], 'ko', markerfacecolor = 'w', label = "numerical soluton")
ax[2].plot(r3.t, list(map(exact_f, r3.t)), 'r', label = "exact solution")
ax[2].legend()
# ax[2].set_xlabel("x")
ax[2].set_xticks(np.arange(x0,xe3+h/2,h))
ax[2].set_ylabel("y(x)")
plt.tight_layout()
plt.show()