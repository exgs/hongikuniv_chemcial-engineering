def octanol_1():
	x = [571370, -4849, 19.725, -0.021532]
	return x

def Cp_liquid(T, C):
	[C1,C2,C3,C4] = C
	# Tc = 655
	# t = 1 - (T/Tc)
	# Cp = C1**2/t + C2 - 2*C1*C3*t - C1*C4*t**2 - (C3**2)*t**3/3 - C3*C4*t**4/2 - (C4**2)*(t**5)/5
	Cp = C1 + C2*T + C3*T**2 + C4*T**3
	return Cp

def Cp_liquid_test(T, C1,C2,C3,C4):
	Cp = C1 + C2*T + C3*T**2 + C4*T**3
	return Cp

Tk = 273.15
Ta = 0 +Tk
Tb = 100 +Tk
h = (Tb-Ta) / 2
Tc = (Ta + Tb) / 2 #C : center
fa = Cp_liquid(Ta, octanol_1())
fb = Cp_liquid(Tb, octanol_1())
fc = Cp_liquid(Tc, octanol_1())
Cp_liq_1_octanol = h/3 * (fa + 4*fc + fb)
error = 0
print("simpson : %.15f" %Cp_liq_1_octanol)
from scipy.integrate import quad
import numpy as np
r = quad(Cp_liquid_test, Ta, Tb, args=(571370, -4849, 19.725, -0.021532))
r = quad(Cp_liquid, Ta, Tb, args=(octanol_1()))
print("quad : %.15f" %r[0])
print("Error : %.15f" %(r[0]-Cp_liq_1_octanol))
