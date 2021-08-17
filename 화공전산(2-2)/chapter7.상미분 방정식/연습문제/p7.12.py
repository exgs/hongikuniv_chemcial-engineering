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
from math import cos, sin, sqrt
from scipy.integrate import solve_ivp
import numpy as np
def f(t, z):
	[C_A, T, T_c] = z
	k0 = (F*(C_Ai - C_A) - V * r_A(z))/V
	k1 = (p*C_p*F*(T_i - T)- H_R*V*r_A(z)-U*A*(T-T_c))/(p*C_p*V)
	k2 = (p_c*C_pc*F_c*(T_ci-T_c)+U*A*(T-T_c))/(p_c*C_pc*V_c)
	return k0,k1,k2
h = 0.1
t0, te = 0, 3600
z = [0, 25, 25]
tj = np.arange(t0, te+h/2, h)
sol1 = solve_ivp(f,[t0,te], z, t_eval=tj)

print(sol1.success)
from matplotlib import pyplot as plt
fig, ax = plt.subplots(2)
fig.suptitle("problem 7.12")
ax[0].plot(sol1.t, sol1.y[0], 'k')
ax[0].grid()
ax[0].set_xlabel('t')
ax[0].set_ylabel('CA')

ax[1].plot(sol1.t, sol1.y[1], 'r-', label = "T")
ax[1].plot(sol1.t, sol1.y[2], 'b-', label = "Tc")
ax[1].legend()
ax[1].grid()
ax[1].set_xlabel('t')
ax[1].set_ylabel('T,Tc')
plt.tight_layout()
plt.show()
