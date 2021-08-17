def non_linear_differential_problem(n):
	a, ya = 0, 1
	b, yb = 1, 1.5
	# n = 100
	eps1, eps2 = 1e-3, 1e-2
	kmax = 100
	h =  1/n
	import numpy
	tj = numpy.linspace(a, b, n + 1)
	yk = numpy.linspace(ya, yb, n + 1)
	print(tj)
	print(yk)

	from scipy.linalg import solve_banded
	k = 0
	while k < kmax:
		fk, JU, JD, JL = [], [], [], []
		# for j in range(0, n-1):
		for j in range(1, n):
			if j == 1:
				y0, y1, y2 = ya, yk[j], yk[j+1]
			else:
				y0, y1, y2 = y1, y2, yk[j+1]
			# y0, y1, y2 = yk[j], yk[j+1], yk[j+2]
			fk.append(-y0 + h*y0*y1 + (2-h**2) *y1 - h*y1*y2 -y2)
			JU.append(-1 + h*y1)
			JD.append(h*y0 + 2 - h**2 - h*y2)
			JL.append(-h*y1 - 1)
		JU[0], JL[-1] = 0, 0
		dy = solve_banded([1, 1], [JU, JD, JL], fk)
		for j in range(1, n):
			yk[j] = yk[j] -dy[j - 1]
		e1 = numpy.linalg.norm(fk)
		e2 = numpy.linalg.norm(dy)
		if e1 < eps1 and e2 < eps2:
			break
		k = k + 1
	return tj, yk
# print("k = ", k, '\n', yk)


from matplotlib import pyplot as plt

fig, ax = plt.subplots(3)
result = non_linear_differential_problem(20)
ax[0].plot(result[0], result[1])
result1 = non_linear_differential_problem(50)
ax[1].plot(result1[0], result1[1])
result2 = non_linear_differential_problem(200)
ax[2].plot(result2[0], result2[1])
plt.show()
print("n횟수에 상관없이 동일한 해를 가진다.")
