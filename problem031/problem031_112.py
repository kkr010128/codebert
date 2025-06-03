import math
n=int(input())
while n != 0 :
	sums = 0.0
	s = list(map(float,input().split()))
	m = sum(s)/n
	for i in range(n):
		sums += ((s[i]-m)**2)/n
	print(math.sqrt(sums))
	n = int(input())
