import math
while True:
	n = int(input())
	if n == 0:
		break
	Student=list(map(float,input().split()))
	#print(n)
	#print(Student)
	#m=average
	average=sum(Student)/n
	#print(m)
	#a^2=dispersion
	s=0.0
	for i in Student:
		s+=(i-average)**2
	dispersion=s/n
	print("%.6f"%(math.sqrt(dispersion)))