from math import exp
def f(x):
	[C_A, T, T_c] = x
	f1 = F*(C_Ai - C_A) - V * r_A(x)
	f2 = p*C_p*F*(T_i - T)- H_R*V*r_A(x)-U*A*(T-T_c)
	f3 = p_c*C_pc*F_c*(T_ci-T_c)+U*A*(T-T_c)
	return ([f1,f2,f3])
	
def r_A(x):
	[C_A, T, T_c] = x
	r = k0 * exp(-(E/R)/(T + 273.15)) * C_A**2
	return (r)

def r_A_delx(x):
	[C_A, T, T_c] = x
	r = k0 * exp(-(E/R)/(T + 273.15)) * 2*C_A
	return (r)

def r_A_delT(x):
	[C_A, T, T_c] = x
	r = r_A(x) * E/R * (1/(T+273.15))**2
	return (r)

#상수 정리
A = 5.4
C_p = 1.815 * (10**5)
C_pc = 4184
E = 1.182 * (10**7)
F = 7.5 * (10**-3)
F_c = 7.32 * (10**-3)
k0 = 0.0744
R = 8314.39
U = 3550
V = 7.08
V_c = 1.82
H_R = -9.86*(10**7)
p = 19.2
p_c = 1000

#초기 추정치
C_Ai = 3
T_ci = 25
T_i = 66
from scipy.optimize import root
sol = root(f, [3,25,66])
print(sol.x)

#반복문으로 풀어보기

def jacobian(x_list):
	[x,y,z] = x_list
	j11, j12, j13 = -F-V*r_A_delx(x_list), -V*r_A_delT(x_list), 0
	j21, j22, j23 = -H_R*V*r_A_delx(x_list), -p*C_p*F - H_R*V*r_A_delT(x_list)-U*A, U*A
	j31, j32, j33 = 0, U*A, -p_c*C_pc*F_c - U*A, 
	return ([[j11,j12,j13], [j21, j22, j23], [j31, j32, j33]])

from numpy.linalg import norm, solve
print("numpy.linalg solve, jacobian(1)")
ebar1, ebar2, ebar3, kmax = 0.005, 0.1, 0.1, 10
k = 1
# C_Ai = 3, T_ci = 25, T_i = 66
x = [3, 25, 66]
y = f(x)
while k < kmax:
	J = jacobian(x)
	dx = solve(J,y)
	k = k + 1
	x = x - dx
	y = f(x)
	print(x)
	e1, e2, e3 = dx[0], dx[1], dx[2]
	if (e1 <= ebar1 and e2 <= ebar2 and e3 <= ebar3):
		break
print(x)
