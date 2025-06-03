import math
c = 0
n = int(input())
for _ in range(n):
	t = int(input())
	for i in range(2,int(math.sqrt(t)+1)):
		if t%i==0:
			break
	else:
		c+=1
print(c)