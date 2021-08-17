##1.3.1
# Vb에 대한 브라켓이 적절하지않다.(이상기체로 계산하면, 0.76587)
# Nist의 데이터에 따르면 에탄이 (온도,압력) = (280K 27.708atm)에서 부피 0.078481L/mol의 액체상태이다. 따라서 이상기체를 기준으로 하면 액체의 부피값을 얻을 수 없다.
# 또한, 세근을 가진다면, 가장 왼쪽에 위치한 근이 에탄올 액체부피에 근접할 것이라고 예측할 수 있다.
# 반더발스 방정식은 실제로 공업적으로 오차가 많다는 것을 알고 있기 때문에, 외부데이터에서 기준으로 반더발스방정식을 해석하거나 기준잡으면 안된다고 생각했다.(예를들면 이상기체, Nist의 table 값)
# 따라서 반더발스의 개념에서 분자 자체의 부피에 해당하는 b = 0.0651L/mol 보다 부피가 클 것이라고 생각하여, e1오차 만큼 큰 값을 기준으로 삼았다.
# 브라켓 범위는 0.0661L ~ 0.1322L로 잡고자한다.
# Nist값을 참고해서 이 범위를 해석하면 액체의 부피(0.078481 L/mol)가 이 범위내에 존재하고, 280K에서 실제기체의 부피(0.53 L/mol)는 보다 크기때문에,
# 반더발스방정식내에서 액체의 부피를 구할 수 있을 것이라고 해석된다.
# Nist 출처 : https://webbook.nist.gov/cgi/fluid.cgi?T=280&PLow=20&PHigh=35&PInc=&Applet=on&Digits=5&ID=C74840&Action=Load&Type=IsoTherm&TUnit=K&PUnit=atm&DUnit=mol%2Fl&HUnit=kJ%2Fmol&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&RefState=DEF
def f(v):
	return (0.0820574 * 280 / (v - 0.0651)) - (5.507 / (v**2)) - 30

e1, e2, kmax = 1e-3, 1e-5, 10000
k = 1
Va = 0.0661
f_va = f(Va)
k = 2
Vb = Va * 2
f_vb = f(Vb)

Vc_old = Vb
print("first f_va %f" % f_va)
print("first f_vb %f" % f_vb)
while (k < kmax):
	# Vc = (Va+Vb) / 2 # 이분법
	# Vc = Vb - (Vb- Va) * f(Vb) / (f(Vb)-f(Va)) : 브라켓 범위내에서 단조증가함수일 때 사용하는 식
	Vc = Va - (Vb-Va) * f(Va) / (f(Vb)-f(Va)) # : 브라켓 범위내에서 단조감소함수에서 사용하는 식
	print("Vc : %f" % Vc)
	f_vc = f(Vc) 
	print("k : %d Vc : %f f_Vc %f" %(k, Vc, f_vc))
	if (abs(f_vc) <= e1  and abs(Vc-Vc_old) <= e2):
		break
	if (f_va * f_vc > 0):
		Va, f_va = Vc, f_vc
	else:
		Vb, f_vb = Vc, f_vc 
	Vc_old = Vc
	k += 1
if (k == kmax):
	print("브라켓 범위내에 반복횟수를 kmax로 찾을 시에 해를 찾을 수 없습니다!")

## 결론
# 이 문제에서는 이분법이 k=15 , 가위치법이 k=4661로 반복해야한다.
# 이분법이 더 효율적이였다. 가위치법의 단점이 잘 드러나는 문제였다.