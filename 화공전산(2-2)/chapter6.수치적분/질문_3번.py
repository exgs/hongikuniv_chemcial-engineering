def Nitric_oxide():
	x = [34980, -35.32, 0.07729, -5.7357E-5, 1.4526E-13]
	return x

def Nitrous_oxide():
	x = [29338, 32360, 1123.8, 21770, 479.4]
	return x
	
def Nitromethane():
	x = [38782, -48.39, 0.413]
	return x

def Hydrogen():
	x = [64979, -788.17, 5.8287, -0.01846, 2.16E-5]
	return x

from math import erf, exp, sqrt, pi, sinh, cosh

def Cp_gas(T, C):
	[C1,C2,C3,C4,C5] = C
	# print(C1,C2,C3,C4,C5)
	# equation1
	# Cp = C1 + C2*((C3/T)/(sinh(C3/T)))**2 + C4*((C5/T)/(cosh(C5/T)))**2
	# equation2
	Cp = C1 + C2*T + C3*(T**2) + C4*(T**3) + C5*(T**4)
	return Cp

print("Hydrogen의 기체 비열")
#Hydrogen의 Tmin = 50 -> 37970 Tmax : 250 -> 28340
max_value = 0
min_value = 80000
for i in range(50,250,1):
	f_test = Cp_gas(i, Hydrogen())
	if (max_value < f_test):
		max_value = f_test
	if (min_value > f_test):
		min_value = f_test
print("Cpmax : %.3f Cpmin : %.3f" %(max_value, min_value))
print("T=50일때, Cp : %.3f" %Cp_gas(50, Hydrogen()))
print("T=250일때, Cp : %.3f" %Cp_gas(250, Hydrogen()))
print('-'*30)
print("Nitric oxide의 기체 비열")
#Nitric oxide NO  Tmin :100K->32170  Tmax:1500K ->35860
max_value = 0
min_value = 80000
for i in range(100,1500,1):
	f_test = Cp_gas(i, Nitric_oxide())
	if (max_value < f_test):
		max_value = f_test
	if (min_value > f_test):
		min_value = f_test
print("Cpmax : %.3f Cpmin : %.3f" %(max_value, min_value))
print("T=100일때, Cp : %.3f" %Cp_gas(100, Nitric_oxide()))
print("T=1500일때, Cp : %.3f" %Cp_gas(1500, Nitric_oxide()))
