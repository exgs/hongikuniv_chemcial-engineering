x10,x20,x30 = 1,1,1
b11,b22,b33 = 4,1,9

a11, a12, a13, b1 = 1, 2, -2, b11
a21, a22, a23, b2 = 1, 1, 1, b22
a31, a32, a33, b3 = 2, 2, 1, b33

ebar2, kmax = 1e-3, 30
print("%3s %8s %8s %8s" %('k','x1','x2','x3'))
fmt = "%3d %8.4f %8.4f %8.4f"
from numpy.linalg import norm
k = 1
x1new, x2new, x3new = \
	[x10, x20, x30] #초기값 설정
print(fmt %(k, x1new, x2new, x3new))

while k < kmax:
	x1old, x2old, x3old = x1new, x2new, x3new
	k = k + 1
	# x1new = (b1 - (a12*x2old + a13*x3old)) / a11
	# x2new = (b2 - (a21*x1old + a23*x3old)) / a22
	# x3new = (b3 - (a31*x1old + a32*x2old)) / a33
	x1new = (b1 - (a12*x2old + a13*x3old)) / a11
	x2new = (b2 - (a21*x1new + a23*x3old)) / a22
	x3new = (b3 - (a31*x1new + a32*x2new)) / a33
	print(fmt %(k, x1new, x2new, x3new))
	e2 = norm([x1new-x1old, x2new-x2old, x3new-x3old])
	if (e2 <= ebar2):
		break