from scipy.optimize import newton
import math


def g(Ma, r):
	y = 1/Ma**2 - (r+1)/2*math.log((r-1)/2 + 1/Ma**2)
	return y
	
def h(Ma):
	r = 1.32 #여기서 정의했음
	y = 1+(r-1)/2*Ma
	return y
	
def adiabatic_f(Ma, L): #관설비에 상수값들 함수 내부에서 정의하고 있음
	r = 1.32
	Ma_a = 0.06
	Ma_b = Ma
	L = L*100/2.54
	f = 0.0035
	Di = 40
	y = (g(Ma_a,r)-g(Ma_b,r))/r - 4*f*L/Di
	return y

def adiabatic_p(pa,Ma_a,Ma_b):
	pb = (Ma_a/Ma_b*(h(Ma_a)/h(Ma_b))**0.5)*pa
	return pb

def adiabatic_T(Ta,Ma_a,Ma_b):
	Tb = h(Ma_a)/h(Ma_b)*Ta
	return Tb

def isothermal_f(pb,L):
	Di = 40
	f = 0.0035
	G = 1770
	M = 16.04
	pa = 100*101325
	R = 8.314
	T = 300
	L = L * 100 / 2.54
	y = M*(pa**2)/(G**2*R*T)*(1-(pb/pa)**2)+2*math.log(pb/pa)-4*f*L/Di
	return y #atm을 return
	
import numpy as np
L = np.arange(0, 14.5, 0.5)
L = list(map(lambda x: x*1000, L))

y_isothermal_atm = []
y_adiabatic_atm = []
y_isothermal_T = []
y_adiabatic_T = []

pa = 100 #atm
T = 300 #K

print("등온 마찰 흐름")
for i in L:
	y_Pa = newton(isothermal_f, 101325, None, (i,))
	y_atm = y_Pa/101325
	y_isothermal_atm.append(y_atm)
	print(y_atm)	
print("--------------\n")
for i in L:
	y_isothermal_T.append(T)
	
print("==============\n")
print("--------------\n")
print("==============\n")
print("단열 마찰 흐름")
for i in L:
	Ma_a = 0.06
	Ma_b = newton(adiabatic_f, 0.06, None, (i,))
	y_atm = adiabatic_p(pa,Ma_a,Ma_b)
	y_temperature = adiabatic_T(T,Ma_a,Ma_b)
	y_adiabatic_atm.append(y_atm)
	y_adiabatic_T.append(y_temperature)
	print(y_atm)
	print(y_temperature)
print("-------------그래프---------------")
import math
import numpy as np
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2,1, squeeze=False, figsize=(7,7))
fig.suptitle("problem 3.8")
ax[1][0].set_title("About Pressure")
ax[0][0].plot(L,y_adiabatic_atm, label = "adiabatic")
ax[0][0].plot(L,y_isothermal_atm, label = "isothermal")
ax[0][0].legend()

ax[1][0].set_title("About Temperature")
ax[1][0].plot(L,y_adiabatic_atm, label = "adiabatic")
ax[1][0].plot(L,y_isothermal_atm, label = "isothermal")
ax[1][0].legend()
plt.show()