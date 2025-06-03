from math import *
from collections import defaultdict
GLOBAL = {}
def roots(n):
	res = set()
	for i in range(1,int(sqrt(n))+1):
		if n%i == 0:
			res.add(i)
			res.add(n//i)
	return len(res)

n = int(input())
cnt = 0
for i in range(1,n+1):
	y = n//i
	cnt+=((y)*(y+1)*(i))//2
print(cnt)
