from scipy.integrate import solve_ivp

def f(t,y):
	return t+ y**2/2

#보폭을 알아서 설정해주는 경우
t_0, y_0 = 0, 1
te = 1
result = solve_ivp(f, [t_0, te], [y_0], method='RK45')
print(result)

#보폭을 내가 설정해주는 경우
import numpy

h = 0.1
ts = numpy.arange(t_0, te+h, h)
result = solve_ivp(f, [t_0, te], [y_0], t_eval= ts)
print(result)
