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
'''
참고
http://allman84.blogspot.com/2018/10/sympy.html
https://studymake.tistory.com/32
'''