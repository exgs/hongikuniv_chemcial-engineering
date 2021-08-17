a11, a14, b1 = 2, 1, 5
a22, a24, b2 = 2, 1, 4
a31, a33, b3 = 1, 2, 3
a42, a44, b4 = 1, 2, 2

ebar2, kmax = 1e-4, 20
print("%3s %8s %8s %8s %8s" %('k','x1','x2','x3','x4'))
fmt = "%3d %8.4f %8.4f %8.4f %8.4f"
from numpy.linalg import norm
k = 1
x1new, x2new, x3new, x4new = \
	[b1/a11, b2/a22, b3/a33, b4/a44] #초기값 설정
print(fmt %(k, x1new, x2new, x3new, x4new))

while k < kmax:
	x1old, x2old, x3old, x4old = x1new, x2new, x3new, x4new
	k = k + 1
	x1new = (b1 - a14*x4old) / a11
	x2new = (b2 - a24*x4old) / a22
	x3new = (b3 - a31*x1old) / a33
	x4new = (b4 - a42*x2old) / a44
	#x3new = (b3 - a31*x1new) / a33
	#x4new = (b4 - a42*x2new) / a44 gauss-sedial법
	print(fmt %(k, x1new, x2new, x3new, x4new))
	e2 = norm([x1new-x1old, x2new-x2old, x3new-x3old, x4new-x4old])
	if (e2 <= ebar2):
		break