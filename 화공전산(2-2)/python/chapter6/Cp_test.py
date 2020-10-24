def gas_nitrogen():
	x = [29105, 8614.9, 1701.6, 103.47, 909.79]
	return x


def Cp_gas(C,T):
	[C1,C2,C3,C4,C5] = 0
	[C1,C2,C3,C4,C5] = C
	Tc = 655
	t = 1 - (T/Tc)
	Cp = C1 + C2*T + C3*T**2 * C4*T**3 * C5*T**4
	# Cp = C1**2/t + C2 - 2*C1*C3*t - C1*C4*t**2 - (C3**2)*t**3/3 - C3*C4*t**4/2 - (C4**2)*(t**5)/5
	return Cp
