import math
x = 0
for n in range(1, 20):
	x = x + 0.1
	y = x * 10
	# if n == y:
	# #실수에서는 "같다"는 조건식을 쓸 때 주의해야한다. 대게 e < 0.001 오차를 이용해서 같음을 증명한다.
	# 	print("%5d is %12.5f" %(n,y))
	# else:
	# 	print("%5d is not %8.5f" %(n,y))
	
	## if n == y : 대체하기
	if abs(n - y) < 0.0001 :
		print("%5d is %12.5f" %(n,y))
	else:
		print("%5d is not %8.5f" %(n,y))
		
		
#무리수의 실수표현
print("%.30f" % math.pi)