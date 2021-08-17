import numpy
from scipy.linalg import solve_banded

#전방차분
ya,yb,n=1, 0, 10
h=1/n

beta_forward=2 + 4*h - h**2
gamma_forward=1 + 4*h
AB=[[-gamma_forward]*(n-1),
	[beta_forward]*(n-1),
	[-1]*(n-1)]
b=[0] * (n-1)
AB[0][0], AB[2][-1] = 0, 0
b[0], b[-1] = ya, gamma_forward*yb
x=solve_banded([1,1],AB,b)

#중앙차분
yac,ybc,n=1,0,10
h=1/n

alpha_center=1 - 2*h
beta_center=2 - h**2
gammac=1 + 2*h
ABc=[[-gammac]*(n-1),
	[beta_center]*(n-1),
	[-alpha_center]*(n-1)]
bc=[0] * (n-1)
ABc[0][0], ABc[2][-1] = 0, 0
bc[0],bc[-1]=yac*alpha_center, gammac*ybc
xc=solve_banded([1,1],ABc,bc)

# #후방차분
yab,ybb,n=1,0,10
h=1/n

alpha_back=1-4*h
beta_back=2-4*h-h**2
ABb=[[-1]*(n-1),[beta_back]*(n-1),[-alpha_back]*(n-1)]
bb=[0]*(n-1)
ABb[0][0],ABb[2][-1]=0,0
bb[0], bb[-1] = yab * alpha_back, yb
xb=solve_banded([1,1],ABb,bb)

t=numpy.linspace(0,1,(n + 1))

from matplotlib import pyplot as plt
plt.figure(figsize=(4,3))
x = numpy.insert(x, 9, 0)
x = numpy.insert(x, 0, 1)
xb = numpy.insert(xb, 0, 1)
xb = numpy.insert(xb, 9, 0)
xc = numpy.insert(xc, 9, 0)
xc = numpy.insert(xc, 0, 1)

plt.plot(t,x,'b',label = "Forward")
plt.plot(t,xb,'k',label= 'Back')
plt.plot(t,xc,'r',label ="Center")
plt.legend()

plt.xlabel('t')
plt.ylabel('y(t)')
plt.tight_layout()
plt.show()
