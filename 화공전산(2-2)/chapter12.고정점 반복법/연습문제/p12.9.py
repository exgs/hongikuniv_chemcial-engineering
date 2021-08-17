from numpy.linalg import norm

def g1(x,y):
    return 1-a*x**2+y

def g2(x,y):
    return b*x

a,b=1.4,0.3
ebar2,kmax=1e-6,500
fmt='%3d %10.4f %10.4f'

xk = []; yk = []

k=1
x1new,y1new=0,0
print(fmt %(k,x1new,y1new))
xk.append(x1new);yk.append(y1new)
while k<kmax:
	k=k+1
	x1old,y1old=x1new,y1new
	x1new=g1(x1old,y1old)
	y1new=g2(x1old,y1old)
	xk.append(x1new);yk.append(y1new)
	print(fmt %(k,x1new,y1new))
	e2=norm([x1new-x1old,y1new-y1old])
	if e2<=ebar2:
		break
	
k_array = list(range(1,k+1))
from matplotlib import pyplot as plt
fig, ax = plt.subplots(3, figsize=(12,12))
# plt.figure(figsize=(12,12))
ax[0].plot(k_array, xk, 'o', markersize=1)
ax[1].plot(k_array, yk, 'o', markersize=1)
ax[2].plot(xk, yk, 'o', markersize=1)
#ax[2].plot(xk[300:], yk[300:], 'o', markersize=1) (c)번
plt.show()