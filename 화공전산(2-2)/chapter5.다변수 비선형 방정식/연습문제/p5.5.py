def f(x):
	[x,y,z] = x
	f1 = 10*(y-x)
	f2 = x*(28-z) - y
	f3 = x*y -8/3*z
	return [f1,f2,f3]


from scipy.optimize import root
sol = root(f, [5.361, 5.361, 5.361])
sol = root(f, [5.362, 5.362, 5.362])
sol = root(f, [8, 8,27])
print("scipy.optimize root")
print(sol.x)
print("-"*20)

def jacobian(x):
	[x,y,z] = x
	j11, j12, j13 = -10, 10, 0
	j21, j22, j23 = 28-z, -1, -x
	j31, j32, j33 = y, x, -8/3
	return ([[j11,j12,j13], [j21, j22, j23], [j31, j32, j33]])

from numpy.linalg import norm, solve
print("numpy.linalg solve, jacobian(1)")
ebar1, ebar2, kmax = 1e-5, 1e-5, 30
k = 1
x = [5.361,5.361,5.361]
y = f(x)
while k < kmax:
	J = jacobian(x)
	dx = solve(J,y)
	k = k + 1
	x = x - dx
	y = f(x)
	# print(x)
	e1, e2 = norm(y), norm(dx)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
print(x)

print("numpy.linalg solve, jacobian(2)")
ebar1, ebar2, kmax = 1e-5, 1e-5, 30
k = 1
x = [5.362,5.362,5.362]
y = f(x)
while k < kmax:
	J = jacobian(x)
	dx = solve(J,y)
	k = k + 1
	x = x - dx
	y = f(x)
	# print(x)
	e1, e2 = norm(y), norm(dx)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
print(x)

print("numpy.linalg solve, jacobian")
ebar1, ebar2, kmax = 1e-5, 1e-5, 30
k = 1
x = [5.363,5.363,5.363]
y = f(x)
while k < kmax:
	J = jacobian(x)
	dx = solve(J,y)
	k = k + 1
	x = x - dx
	y = f(x)
	# print(x)
	e1, e2 = norm(y), norm(dx)
	if (e1 <= ebar1 and e2 <= ebar2):
		break
print(x)