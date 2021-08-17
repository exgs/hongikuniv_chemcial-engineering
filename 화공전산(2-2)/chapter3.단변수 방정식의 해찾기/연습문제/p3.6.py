import math

def f(pb,L):
	Di = 40
	f = 0.0035
	C = 4*f*L/Di
	# print(C)
	G = 1770
	M_g = 16.04
	M_kg = 0.01604
	pa_atm = 100
	pa_Pa = pa_atm * 101325
	R = 8.314
	T = 300
	front = M_kg*(pa_Pa**2)
	Front = front/((G**2)*R*T)
	# Front = M_kg*(pa_Pa**2)/((G**2)*R*T)
	print(Front)
	y = Front*(1-(pb/pa_atm)**2)+2*math.log(pb/pa_atm)-C
	return y

from scipy.optimize import newton
from scipy.optimize import bisect
L = 14000*100/2.54
p_L14_newton = newton(f, 25, None, (L,))
p_L14_bisect = bisect(f, 1,100, (L,))
L = 12000*100/2.54
p_L12_newton = newton(f, 40, None, (L,))
p_L12_bisect = bisect(f, 1,100, (L,))

print('------------------------n')
print(p_L14_newton)
print(p_L12_newton)
print(p_L14_bisect)
print(p_L12_bisect)
# print(x0, x1)
# print(x00, x11)