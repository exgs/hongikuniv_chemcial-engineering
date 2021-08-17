def f(y0,y1):
	k0 = y1 + 3*y0**2
	k1 = y0 - 3*y1**2
	return k0,k1

t, y0, y1 = 0, 0, 0.8
te, h = 1, 0.1
print("%5.1f %10.5f %10.5f" %(t, y0, y1), end = '')
while t < te-h/2:
	k0, k1 = f(y0, y1)
	print(" %10.5f %10.5f" %(k0,k1))
	t = t+h
	y0 = y0 + k0 * h
	y1 = y1 + k1 * h
	print("%5.1f %10.5f %10.5f" %(t, y0, y1), end = '')
print()
