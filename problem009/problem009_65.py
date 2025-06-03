from collections import deque

def bfs():
	que=deque([])
	que.append(0)
	v[0]=0
	
	while que:
		p=que.popleft()
		for l in L[p]:
			if v[l-1]==-1:
				que.append(l-1)
				v[l-1]=v[p]+1
	
n=int(input())
L=[]
for i in range(n):
	A=[]
	A=list(map(int,input().split()))
	L.append(A[2:])
v=[-1]*n
bfs()
for i in range(n):
	print(i+1,v[i])

