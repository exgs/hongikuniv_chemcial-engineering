a11, a13, b1 = 2, 1, 10
a21, a22, b2 = -1, 4, 11
a32, a33, b3 = 2, 6, 18
a43, a44, b4 = 3, 8, 19

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
	x1new = (b1 - a13*x3old) / a11
	x2new = (b2 - a21*x1old) / a22
	x3new = (b3 - a32*x2old) / a33
	x4new = (b4 - a43*x3old) / a44
	#x3new = (b3 - a31*x1new) / a33
	#x4new = (b4 - a42*x2new) / a44 gauss-sedial법
	print(fmt %(k, x1new, x2new, x3new, x4new))
	e2 = norm([x1new-x1old, x2new-x2old, x3new-x3old, x4new-x4old])
	if (e2 <= ebar2):
		break