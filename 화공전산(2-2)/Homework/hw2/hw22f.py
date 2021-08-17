A = [[0.4, -1.1, 1.4, 0.5],
	[0.6, -1.3, 1.2, 0.3],
	[-0.9, 0.2, 0.7, 1.6],
	[-1.5, 0.8 ,0.1 ,1.0]]
b = [1.6, 1.1, 2.8, 2.3]

from numpy.linalg import solve
x = solve(A,b)
for i in range(4):
	print("x[%d] : %10.3f" %(i,x[i]))
input("Press Enter")