from math import cos, pi, sin, sqrt
#중력가속도, 밀도, 항력계수, 야구공의 직경, 질량
g, rho, Cd, Dp, m = 9.8, 1.2, 0.45, 0.074, 0.145
#투영면적
Ap = pi/4 * Dp**2

#항렬을 질량으로 나눈 것
c1 = Cd * Ap * rho / (2*m)

def f(t,z):
	[x,y,u,v] = z
	w = sqrt(u**2 + v**2)
	#x,y의 미분 값
	xp = u
	yp = v
	up = -c1 * w * u
	vp = -c1 * w * v -g
	return xp,yp,up,vp
#시간, x,y좌표, 공의 초기속도, 공의 초기 각도
t0, x0, y0, w0, q0 = 0, 0, 1, 50, pi/4
u0,v0 = w0 * cos(q0), w0 * sin(q0)
te, h = 6, 0.1

from scipy.integrate import solve_ivp
import numpy as np
t,x,y,u,v = t0,x0,y0,u0,v0
# print("Solution 1")
# print("%10s %10s" %("x", "y"))
# while t < te+h/2:
# 	r = solve_ivp(f,[t ,t + h],[x,y,u,v])
# 	t = r.t[-1]
# 	x,y,u,v = r.y[0,-1],r.y[1,-1],r.y[2,-1],r.y[3,-1]
# 	print("%10.5f %10.5f" %(x,y))
# 	if (x>100):
# 		break

print("Solution 2")
print("%10s %10s" %("x", "y"))
tj = np.arange(t0, te+h/2, h)
solve = solve_ivp(f, [t, te], [x,y,u,v], t_eval= tj)
x=[]
y=[]
for i in range(0,50):
	print("%10.5f %10.5f" %(solve.y[0,i], solve.y[1,i]))
	x.append(solve.y[0,i])
	y.append(solve.y[1,i])
	if (solve.y[0,i] > 100):
 		break
from matplotlib import pyplot as plt
plt.figure("Ex7.14",figsize=(8,5))
plt.title("baseball problem")
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()