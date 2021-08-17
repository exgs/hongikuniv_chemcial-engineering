A = [[0.4, -1.1, 1.4, 0.5],
	[0.6, -1.3, 1.2, 0.3],
	[-0.9, 0.2, 0.7, 1.6],
	[-1.5, 0.8 ,0.1 ,1.0]]
b = [1.6, 1.1, 2.8, 2.3]

from scipy.linalg import lu, solve_triangular
P,L,U = lu(A)
for i in range(4):
	for j in range(4):
		print("%10.3f" %U[i][j], end=" ")
	print()
input("Press Enter")