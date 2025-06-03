import math
N = input()
c = 0
p = [0 for i in range(N)]
for i in range(0,N):
	p[i] = input()
for i in range(N):
	s = math.sqrt(p[i])
	j = 2
	while(j <= s):
		if(p[i]%j == 0):
			break
		j += 1
	if(j > s):
		c += 1
print c