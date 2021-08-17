from scipy.linalg import solve_banded
import numpy
def linear_differential_problem(n):
	ya, yb = 1, 0
	h = (ya - yb) / n
	AB =[[-1] * (n-1),
		[2 - h ** 2] * (n-1),
		[-1] * (n-1)]
	AB[0][0], AB[2][-1] = 0, 0
	b = [0] * (n - 1)
	b[0], b[-1] = ya, yb
	y = solve_banded([1,1], AB, b)
	y = numpy.insert(y, 0, 1)
	y = numpy.insert(y, len(y), 0)
	x = numpy.linspace(0, 1, n+1) 
	return x,y

from matplotlib import pyplot as plt

fig, ax = plt.subplots(3)
ax[0].plot(linear_differential_problem(10)[0],linear_differential_problem(10)[1])
ax[1].plot(linear_differential_problem(30)[0],linear_differential_problem(30)[1])
ax[2].plot(linear_differential_problem(100)[0],linear_differential_problem(100)[1])
plt.show()
