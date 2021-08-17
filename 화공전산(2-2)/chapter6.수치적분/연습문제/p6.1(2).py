from math import log

def f(x):
	return 1/x

h = 0.01
hh = 0.005
f_135 = []
f_135.append((log(1.36)-log(1.35))/h)
f_135.append((log(1.355)-log(1.35))/hh)
a = (0.145*f_135[0]-0.005*f_135[1])/(0.145-0.005)
f_15 = []
f_15.append((log(1.51)-log(1.5))/h)
f_15.append((log(1.505)-log(1.5))/(hh))
b = (2*f_15[1]-f_15[0])/(2-1)

print("1.35에서 h=0.1, h= 0.05으로 구한 전방차분으로 Richardson을 적용하여, f(1.5)에서 1차 미분계수값을 구함")
print("%5.4f" %a)
print("1.5에서 h=0.1, h= 0.05으로 구한 전방차분으로 Richardson을 적용하여, f(1.5)에서 1차 미분계수값을 구함")
print("%5.4f" %b)
print("엄밀해 1/x의 실제값")
print("%5.4f" %(1/1.5))