def gas_nitrogen():
	x = [29105, 8614.9, 1701.6, 103.47]
	return x


def Cp_gas(C,T):

	Tc = 655
	t = 1 - (T/Tc)
	# Cp = C1 + C2*T + C3*T**2 * C4*T**3 * C5*T**4
	print(C[0],C[1],C[2],C[3], C[4])
	# Cp = C1**2/t + C2 - 2*C1*C3*t - C1*C4*t**2 - (C3**2)*t**3/3 - C3*C4*t**4/2 - (C4**2)*(t**5)/5
	return 
	
Cp_gas(gas_nitrogen(),20)