import math
from statistics import mean
ans = []
while True:
	n = int(input())
	if n == 0:
		break
	s = list(map(int,input().split()))
	ss = []
	for i in s:
		ss.append(i**2)
	sd = math.sqrt(mean(ss)-mean(s)**2)
	ans.append(sd)
for k in ans:
	print(k)
