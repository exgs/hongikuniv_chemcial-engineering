from math import log

def f(x):
	return 1/x

h = 0.01
f_1 = (-log(1)+log(1.01))/h
f_135 = (-log(1.35)+log(1.36))/h
f_15 = (-log(1.5)+log(1.51))/h
f_2 = (-log(2)+log(2.1))/h
print("%5.4f %5.4f %5.4f %5.4f" %(f_1,f_135,f_15,f_2))
print("%5.4f %5.4f %5.4f %5.4f" %(f(1),f(1.35),f(1.5),f(2)))

from matplotlib import pyplot as plt
# plt.figure()
# plt.show()