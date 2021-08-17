import numpy as np
import math

a = 1.2
b = a + 1 #default
# a,b = map(int, input("숫자 입력 a b:").split())

x = list(np.linspace(a, b, 50))
y = list(map(math.ceil, x))
for i in range(50):
	print(" %f <= %d < %f" %(x[i], y[i], x[i]+1))