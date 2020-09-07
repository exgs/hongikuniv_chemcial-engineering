from sympy import *

def taylor_nth_order(f, n, x0):
	x = Symbol('x')
	f_taylor = f.series(x, x0, n) # (독립변수, 기준점, n차)
	print(f_taylor)
	f_taylor = f_taylor.removeO()
	print(f_taylor)
	#계수 구하기
	p0 = f_taylor.subs(x, 0).evalf()
	p1 = diff(f_taylor).subs(x, 0).evalf() / factorial(1)
	p2 = diff(diff(f_taylor)).subs(x, 0).evalf() / factorial(2)
	p3 = diff(diff(diff(f_taylor))).subs(x, 0).evalf() / factorial(3)
	print("p0 : %f" %p0)
	print("p1 : %f" %p1)
	print("p2 : %f" %p2)
	print("p3 : %f" %p3)

#1.3
x = Symbol('x')
f = cos(x)
#1.3(a)
print("1.3(a)번")
taylor_nth_order(f, 4, 0)
print('-'*20)
#1.3(b)
print("1.3(b)번")
taylor_nth_order(f, 4, pi/3)


#심화학습 그래프그려보기
import numpy as np
from matplotlib import pyplot as plt

x_range = np.arange(-2*np.pi, 2*np.pi, 0.1*np.pi)
x = Symbol('x')
f_maclaurin = cos(x).series(x, 0, 4).removeO()
f_taylor = cos(x).series(x, np.pi/3, 4).removeO()
f_real = cos(x)
p1 = plot(f_maclaurin, label = 'Maclaurin',legend = True, show=False, line_color = 'black' , ylim= [-1,1], xlim = [-2,6])
p2 = plot(f_taylor, label = 'Taylor', legend = True,show=False, line_color = 'red' , ylim= [-1,1])
p3 = plot(f_real, label = 'cos(x)', legend = True,show=False)
p1.extend(p2)
p1.extend(p3)
p1.show()
# y = f_taylor.subs(x, x_range).evalf()
# print(type(y))
# print(y)
# for i in x_range:
# 	print(f_taylor.subs(x, i))
# fig, ax = 

'''
참고
http://allman84.blogspot.com/2018/10/sympy.html
https://studymake.tistory.com/32
'''