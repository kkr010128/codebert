import math
while(1):
	a=0
	n=int(input())
	if n==0: break;
	s=list(map(int,input().split()))
	m=sum(s)/len(s)
	for i in range(n):
		a=a+pow(s[i]-m,2)
	print(math.sqrt(a/n))