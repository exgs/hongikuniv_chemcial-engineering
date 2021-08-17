from math import exp

def f(t,y):
	return y*exp(t)
def ft(t,y):
	return y*exp(t)
def ff(t,y):
	return ft(t,y) + fy(t,y)*f(t,y)
def fy(t,y):
	return exp(t)
def fty(t,y):
	return exp(t)
def fyy(t,y):
	return 0
def ftt(t,y):
	return y*exp(t)
def fff(t,y):
	return ftt(t,y) + 2*fty(t,y)*f(t,y) + fyy(t,y)*f(t,y)**2 +fy(t,y)*ft(t,y)+ fy(t,y)**2*f(t,y)
initial_y = 1 #initial

def PrintOfHead(s):
	print("%10s %5s %10s" %(s, "ti", " y(ti)"))
	return 
def	PrintOfValue(i,t,y):
	print("%10d %5.1f %10.8f" %(i, t, y))
	return


h = 0.2
def euler(t,y):
	i = 0
	PrintOfHead("Euler")
	PrintOfValue(i, t, y)
	while (t < 1):
		y += f(t,y) * h
		t = t + h
		i += 1
		PrintOfValue(i,t,y)

def taylor_2th(t,y):
	i = 0
	PrintOfHead("Taylor 2th")
	PrintOfValue(i, t, y)
	while (t < 1):
		y += f(t,y) * h + h**2/2*ff(t,y)
		t = t + h
		i += 1
		PrintOfValue(i,t,y)

def taylor_3th(t,y):
	i = 0
	PrintOfHead("Taylor 3th")
	PrintOfValue(i, t, y)
	while (t < 1):
		y += f(t,y) * h + h**2/2*ff(t,y) + h**3/6*fff(t,y)
		t = t + h
		i += 1
		PrintOfValue(i,t,y)


t = 0
y = 1
euler(t,y)
taylor_2th(t,y)
taylor_3th(t,y)
