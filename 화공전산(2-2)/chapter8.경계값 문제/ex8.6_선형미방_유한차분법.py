import numpy

ya, yb, n = 1, 0, 10
h = (ya - yb) / n
beta = 2 + 4*h - h**2
gamma = 1 + 4*h
AB =[[-gamma] * (n-1),
	[beta] * (n-1),
	[-1] * (n-1)]
AB[0][0], AB[2][-1] = 0, 0
b = [0] * (n - 1)
b[0], b[-1] = ya, yb * gamma #gamma값을 꼭 넣어줘야함!

from scipy.linalg import solve_banded
x = solve_banded([1,1], AB, b)
x = numpy.insert(x, 9, 0)
x = numpy.insert(x, 0, 1)

print(x)
