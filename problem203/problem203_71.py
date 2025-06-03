import math

A,B=map(int, input().split())

for i in range(1,1001):
	if math.floor(i*0.08)==A and math.floor(i*0.1)==B:
		print(i)
		break
	if i==1000:
		print(-1)