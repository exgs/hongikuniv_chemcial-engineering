def f(T):
	Tc = 647.096
	r = 1 - T/Tc
	p = 17.863 + 58.606 * r**0.35 -95.396 * r**(2/3) + 213.89*r -141.26*r**(4/3)
	return p 
T = [297, 298, 299]
h = 1

FD = (f(299) - f(298))/h
a = -1/f(298) * FD
print("FD : %f" %a)

BD = (f(298) - f(297))/h
a = -1/f(298) * BD
print("BD : %f" %a)

CD = (f(299) - f(297)) / (2*h)
a = -1/f(298) * CD
print("CD : %f" %a)

error = (BD-CD)/2*1
print("error : %f" %error)