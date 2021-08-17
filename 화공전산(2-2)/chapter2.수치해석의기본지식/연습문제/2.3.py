import numpy
import sys

a, b = 0.95 , 1.55
n, h = 7, 0.1
xa = [0.95, 1.05, 1.15, 1.25, 1.35, 1.45, 1.55]
xb = numpy.linspace(a, b, n)
xc = numpy.arange(a, b + h/2, h)
print(type(xa[0]), type(xb[0]), type(xc[0]) )
print(sys.getsizeof(xa[0]), sys.getsizeof(xb[0]), sys.getsizeof(xc[0]))
# if xa[3] == xc[3]:
# 	print(xa[0], xb[0], xa[0]-xb[0])
# 	print("yes")

print("각 요소값 기본으로 출력")
for j in range(0, n):
	print(xa[j], xb[j], xc[j])
print('-'*30)

print("각 요소값 정확도 55로 출력")
for j in range(0, n):
	print("%.55f %.55f %.55f" %(xa[j], xb[j], xc[j]))
print('-'*30)

for j in range(0, n):
	print(xa[j], round(xa[j],1), round(xb[j],1), round(xc[j],1))
	# print(xa[j], round(xa[j],1), round(float(xb[j]),1), round(float(xc[j]),1))
	print('-' * 30)