def f(x):
	x1 = x/10000 #x1는 만원 단위
	if x1 <= 1200:
		return (x * 0.06)
	elif x1 > 1200 and x1 <= 4600:
		return (720000 + (x - 12000000) * 0.15)
	elif x1 > 4600 and x1 <= 8800:
		return (5820000 + (x - 46000000) * 0.24)
	else:
		return (15900000 + (x - 88000000) * 0.35)

print("과세표준액 1천만원 -> 세액 : %d 만원" %(f(10000000)/10000))
print("과세표준액 4천만원 -> 세액 : %d 만원" %(f(40000000)/10000))
print("과세표준액 7천만원 -> 세액 : %d 만원" %(f(70000000)/10000))
print("과세표준액 1억원   -> 세액 : %d 만원" %(f(100000000)/10000))

import numpy
xs = numpy.linspace(0, 1e8, 101)
print(xs)
ys = [f(x) for x in xs]
from matplotlib import pyplot as plt
plt.figure(figsize = (6, 4.5))
plt.title("income tax by B419111's python code")
# plt.figure(figsize = (4, 3))
plt.plot(xs, ys, 'k')
plt.xlabel('Income, krw')
plt.ylabel('Tax, krw')
plt.tight_layout()
plt.savefig('income_tax.png')
plt.show()