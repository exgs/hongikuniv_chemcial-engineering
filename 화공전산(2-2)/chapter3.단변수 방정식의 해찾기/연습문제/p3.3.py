import math

def f_ethane(v, T_star, p_star):
	R = 0.0820574 #atm-L/mol-K
	a = 5.507 #atm-(L/mol)^2
	b = 0.0651 #L/mol
	p = (R*T_star)/(v-b) - a/(v**2) - p_star
	return p

def delta_f_ethane(v, T_star, p_star):
	R = 0.0820574 #atm-L/mol-K
	a = 5.507 #atm-(L/mol)^2
	b = 0.0651 #L/mol
	p = -(R*T_star)/(v-b)**2 + 2 * a/(v**3)
	return p
	
e1, kmax = 1e-3, 20
T, p = 280,30
V_init = 0.1

while(V_init <= 0.4):
	k = 1
	V = V_init
	while (k < kmax):
		if (abs(f_ethane(V,T,p)) <= e1):
			print("초기 추정치 : %f k횟수 : %d 해 : %f" %(V_init, k, V))
			break
		V = V - f_ethane(V,T,p)/delta_f_ethane(V,T,p)
		k = k + 1
	V_init = V_init + 0.05

if (k == kmax):
	print("kmax로 반복횟수를 설정했을 시에해를 찾을 수 없습니다!")
