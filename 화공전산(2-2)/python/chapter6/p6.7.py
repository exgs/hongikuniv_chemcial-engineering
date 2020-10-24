def Nitric_oxide():
	x = [34980, -35.32, 0.07729, -0.000057357, 1.4526E-13]
	return x

def Nitrous_oxide():
	x = [29338, 32360, 1123.8, 21770, 479.4]
	return x

from math import erf, exp, sqrt, pi, sinh, cosh

def delta_f(x):
	return 2/sqrt(pi) * exp(-(x**2))

def three_point_gauss(a,b):
	k1 = (float)(b-a)/2
	k2 = (float)(b+a)/2
	sol = k1 * (5/9*delta_f(k1*-sqrt(3/5)+k2) + 8/9*delta_f(k1*0+k2) + 5/9*delta_f(k1*sqrt(3/5)+k2))
	return sol

def Cp_gas(T, C):
	[C1,C2,C3,C4,C5] = C
	Cp = C1 + C2*((C3/T)/(sinh(C3/T)))**2 + C4*((C5/T)/(cosh(C5/T)))**2
	# Cp = C1 + C2*T + C3*(T**2) + C4*(T**3) + C5*(T**4)
	return Cp
Tmin = 100
Tmax = 1500
max_value = 0
min_value = 40000
for i in range(100,1500,1):
	f_test = Cp_gas(i, Nitric_oxide())
	if (max_value < f_test):
		max_value = f_test
	elif (min_value > f_test):
		min_value = f_test
print(max_value, min_value)

#문제풀기
Ta = 150
Tb = 1500
# h = (Tb-Ta) / 2
# Tc = (Ta + Tb) / 2 #C : center
# fa = Cp_liquid(Ta, octanol_1())
# fb = Cp_liquid(Tb, octanol_1())
# fc = Cp_liquid(Tc, octanol_1())
# Cp_liq_1_octanol = h/3 * (fa + 4*fc + fb)
# error = 0
# print("simpson : %.15f" %Cp_liq_1_octanol)
from scipy.integrate import quad
import numpy as np
r = quad(Cp_gas, Ta, Tb, args=Nitric_oxide())
print("quad : %.15f" %r[0])
