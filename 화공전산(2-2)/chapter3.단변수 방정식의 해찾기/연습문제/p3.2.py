#####조건#####
# 278.68K < T < 562.7K
##오차조건
# 1. e1 1mmHg(=1/760 atm)
# 2. e2 0.1K
# 반복 계산 횟수 kmax = 20
##증기압 공식의 상수값
# c0:83.107
# c1:-6,486.20
# c2:-9.2194
# c3:6.98E-06
# c4:2
import math

def f_benzene(T):
	c0,c1,c2,c3,c4 = 83.107, -6486.20, -9.2194, 6.98E-6, 2
	p_vap = math.exp(c0 + c1/T + c2*math.log(T) + c3*(T**c4))/101325 - 1
	return p_vap

# print(f_benzene(562))
Ta = 278.68
pa = f_benzene(Ta)
k = 1
Tb = 562.5
pb = f_benzene(Tb)
k = 2

kmax = 20
T_before = Ta
e1 = (1/760) * 101325 #unit : Pa
e1 = 133.322
e2 = 0.1 #unit : K
while (k < kmax):
	Tc = (Ta + Tb)/2
	pc = f_benzene(Tc)
	# print("%f %f %f" %(Ta,Tc,Tb))
	print("k : %d Tc : %f pc : %f" %(k, Tc, pc))
	print(abs(pc))
	print(abs(T_before-Tc))
	print("-----------------------------")
	if ((abs(pc) <= e1) and (abs(T_before-Tc) <= e2)):
		break
	else:
		if pa * pc > 0:
			pa, Ta = pc, Tc
		else:
			pb, Tb = pc, Tc
	T_before = Tc
	k = k + 1
print("End")
# print("%f" % 6.98E-6)