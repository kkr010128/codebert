time=1
n=int(input())

A=[[] for i in range(n)]
d=[0 for i in range(n)]
f=[0 for i in range(n)]

for i in range(n):
	a=list(map(int,input().split()))
	for j in range(a[1]):
		A[i].append(a[2+j]-1)

def dfs(q,num):
	global d,f,time
	d[num]=time
	for nx in q[num]:
		if d[nx]==0:
			time+=1
			dfs(q,nx)
	time+=1
	f[num]=time
	
for i in range(n):
	if d[i]==0:#unvisit
		dfs(A,i)
		time+=1

for i in range(n):
	print(i+1,d[i],f[i])
