from scipy.integrate import solve_ivp
import numpy

def f(t,y):
	k0 = y[1] + 3*y[0]**2
	k1 = y[0] - 3*y[1]**2
	return k0,k1

t0, y = 0, [0, 0.8]
te, h = 1, 0.1

tj = numpy.arange(t0,te+h/2,h)
result = solve_ivp(f, [t0, te], y, t_eval=tj)
print(result)

j = 0
print("%3s %10s %10s" %("t","y0","y1"))
for t in tj:
	print("%5.1f %10.5f %10.5f" %(result.t[j], result.y[0,j], result.y[1,j]))
	j = j + 1
