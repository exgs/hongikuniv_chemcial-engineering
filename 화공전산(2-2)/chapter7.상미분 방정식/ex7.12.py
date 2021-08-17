from math import sqrt
import numpy as np
from scipy.integrate import solve_ivp

def f(t, z): #t는 solve_ivp에 쓰기 위해서 있어야하는 파라미터
	[x,y] = z
	r = sqrt(x ** 2 + y ** 2)
	xp = vr - vd * x/r
	yp = -vd *y/r
	return xp, yp

vr, vd = 1,2
t0, te, h = 0, 0.8, 0.01
yeps = [0, 0]
eps = 1e-3
tj = np.arange(t0, te+h/2, h)
result = solve_ivp(f, [t0,te], [0,1], t_eval=tj)
print("%5s %10s %10s" %("t", "x(t)", "y(t)"))
for i in range(0, 81, 10):
	print("%5.1f %10.5f %10.5f" %(result.t[i], result.y[0, i], result.y[1,i]))
	if ( sqrt( (yeps[0]-result.y[0,i])**2 + (yeps[1]-result.y[1,i])**2) < eps):
		break
