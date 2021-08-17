from math import sqrt, log

# def E_mixed_gibbs(x):
# 	# margules coefficient 바꿔주기
# 	ksi = [2, 3]
# 	n, R, T = 1, 8.314, 400
# 	r= n*R*T*margules(x, ksi)
# 	return r

def margules(x, ksi):
	xa, xb = x, 1-x
	y = xa*log(xa) + xb*log(xb) + xa*xb*(ksi[0]*xa + ksi[1]*xb)
	return y

xa, xd = 0.7, 0.79
ksi = [2, 3]

from scipy.optimize import minimize_scalar
r = minimize_scalar(margules, [xa, xd], args = (ksi))
print(r.x)
