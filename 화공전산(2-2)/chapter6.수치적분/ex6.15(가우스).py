from math import tan, sqrt, exp
def f_ex6_15(x):
	if x ==0:
		return(1)
	else:
		return (tan(x)/x)
		
def f_hw3(x):
	return x**3 * exp((-x**2)/2),
	
x1 = -sqrt(3/5)
x2 = 0
x3 = sqrt(3/5)
#3점 구적법
a1,a2,a3 = 5/9, 8/9, 5/9

ex6_15 =0.7 * (a1 * f_ex6_15(0.7*x1+0.7)+ a2* f_ex6_15(0.7*x2+0.7) + a3*f_ex6_15(0.7*x3+0.7))
print(ex6_15)

hw3 = 0.8 * (a1 * f_hw3(0.8*x1 + 1.8)+ a2* f_hw3(0.8*x2 + 1.8) + a3*f_hw3(0.8*x3 + 1.8))
print(hw3)