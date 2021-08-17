import math

def Fanning_func(f,Re):
	v = 2.5*math.log(Re * (f/8)**0.5) + 1.75 - (2/f)**0.5
	return v

Re = 1E+5 # 1e+4 < Re < 1e+6
x_a = 0.001
k = 1
y_a = Fanning_func(x_a, Re)
x_b = 0.9
y_b = Fanning_func(x_b, Re)
k = 2 
kmax = 200
x_c_old = x_a
while (k < kmax):
	x_c = (x_a + x_b) / 2
	y_c = Fanning_func(x_c, Re)
	print("%f %f" %(x_a,x_b))
	if (abs(y_c)< 0.01 and abs(x_c - x_c_old) < 0.01):
		print("k : %d f : %f" %(k,x_c))
		break
	if (y_a * y_c > 0):
		x_a, y_a = x_c, y_c
	else:
		x_b, y_b = x_c, y_c
	k = k + 1
	x_c_old = x_c
if (k==kmax):
	print("Can't find the answer\nTake more kmax value into loop")