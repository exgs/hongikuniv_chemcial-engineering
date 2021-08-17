ya, yb, n = 1, 0, 10
h = (ya - yb) / n
AB =[[-1] * (n-1),
	[2 - h ** 2] * (n-1),
	[-1] * (n-1)]
AB[0][0], AB[2][-1] = 0, 0
b = [0] * (n - 1)
b[0], b[-1] = ya, yb

from scipy.linalg import solve_banded
x = solve_banded([1,1], AB, b)
print(x)
