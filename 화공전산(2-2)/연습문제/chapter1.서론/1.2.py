def real_func(n : float)->float:
	result = n**0.5
	return(result)
	
def taylor_func(n : float)->float:
	result = 1 + 0.5*(n-1)-0.125*(n-1)**2+(1/16)*((n-1)**3) 
	#실제 계산을 통해 게수를 구했다. 1.3번에서는 sympy 라이브러리를 이용해서 구해본다.
	return(result)

def print_def(n : float)->None:
	result1 = real_func(n)
	print(f"when x is {n}")
	print('실제함수의 값 : %.5s' % result1) #소수 5번째자리까지만 출력
	result2 = taylor_func(n)
	print('테일러함수의 값 = %.5s' % result2)
	print('실제값 - 테일러함수의 값 = %.8s' % (result1-result2)) 
	print("-"*30)

a = 0.5
print_def(a)
b = 0.75
print_def(b)
c = 1.25
print_def(c)
d = 1.5
print_def(d)

#기준을 잡았던 x0=1 에서 멀어질수록 값의 오차가 커지는 것을 확인할 수 있다.