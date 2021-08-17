from math import exp

def f(x):
	return exp(x)

a,b = 1,4
exact = exp(b)-exp(a)
m = 4
R =[]
print("%3c %10c Romberg extraploation R[k, j]" %('k','h'))
k = 0
h = b-a
print("%3d %10.5f" %(k,h), end= '')
S = f(a) + f(b)
Rk = [S * h / 2]
print("%11.7f" %Rk[0])
R.append(Rk)

for k in range(1, m):
	h = h/2
	print("%3d %10.5f" %(k,h), end= ' ')
	x = a + h
	while x < b:
		S = S + 2 * f(x)
		x = x + 2 * h
	Rk = [S * h / 2]
	print("%11.7f" %Rk[0], end = ' ')
	
	for j in range(1, k+1):
		n = 2 ** (2*j)
		Rk.append((n*Rk[j-1] -R[k-1][j-1]) / (n-1))
		print("%11.7f" %Rk[-1], end =' ')
	print()
	R.append(Rk)
print("-"*40)
print(R)