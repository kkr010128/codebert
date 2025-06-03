n=int(input())
a=[]
from collections import deque as dq
for i in range(n):
	aaa=list(map(int,input().split()))
	aa=aaa[2:]
	a.append(aa)
dis=[-1]*n
dis[0]=0
queue=dq([0])
while queue:
	p=queue.popleft()
	for i in range(len(a[p])):
		if dis[a[p][i]-1]==-1:
			queue.append(a[p][i]-1)
			dis[a[p][i]-1]=dis[p]+1
for i in range(n):
	print(i+1,dis[i])
		

