def fun(d):
	cnt = 0
	for i in d:
		cnt+= i*d[i]
	return cnt

from collections import defaultdict
d = defaultdict(int)
n = int(input())
A = list(map(int,input().split()))
for i in range(n):
	d[A[i]]+=1
q = int(input())
cnt = sum(A)
for i in range(q):
	b,c = map(int,input().split())
	if b in d:
		cnt+=(-b*d[b] + c*d[b])
		d[c]+=d[b]
		d[b]=0
		#print(cnt,d)
	print(cnt)

