from math import erf, exp, sqrt, pi

def delta_f(x):
	return 2/sqrt(pi) * exp(-(x**2))

def three_point_gauss(a,b):
	k1 = (float)(b-a)/2
	k2 = (float)(b+a)/2
	sol = k1 * (5/9*delta_f(k1*-sqrt(3/5)+k2) + 8/9*delta_f(k1*0+k2) + 5/9*delta_f(k1*sqrt(3/5)+k2))
	return sol

print("error function real value ")
print("erf(1) : %f" %erf(1))
print("erf(2) - erf(1) : %f" %(erf(2)-erf(1)))
print("erf(3) - erf(2) : %f" %(erf(3)-erf(2)))
print("Gauss 3point integration method")
f_0 = 0
f_1 = three_point_gauss(0,1) + f_0
f_2 = three_point_gauss(1,2) + f_1
f_3 = three_point_gauss(2,3) + f_2
f_4 = three_point_gauss(3,4) + f_3
print("f(0) : 0")
print("f(1) - f(0) : %.10f" %(three_point_gauss(0,1)))
print("f(2) - f(1) : %.10f" %(three_point_gauss(1,2)))
print("f(3) - f(2) : %.10f" %(three_point_gauss(2,3)))
print("f(4) - f(3) : %.10f" %(three_point_gauss(3,4)))
print("%10s %10s %10s %10s %10s" %("f(0)", "f(1)", "f(2)", "f(3)", "f(4)"))
print("%10s %10.8f %10.8f %10.8f %10.8f %10.8f" %("Gauss", f_0,f_1,f_2,f_3,f_4))
print("%10s %10.8f %10.8f %10.8f %10.8f %10.8f" %("Exact", erf(0), erf(1), erf(2), erf(3), erf(4)))