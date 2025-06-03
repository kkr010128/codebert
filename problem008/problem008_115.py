n=int(input())

next=[[] for i in range(n)]
for i in range(n):
	l=list(map(int,input().split()))
	u=l[0]
	k=l[1]
	for j in range(2,k+2):
		next[u-1].append(l[j]-1)

stk=[]
stk.append(0)
time=1
d=[0 for i in range(n)]
f=[0 for i in range(n)]
know=[0 for i in range(n)]

def dfs(x):
	global time
	know[x]=1
	d[x]=time
	time+=1
	for n in next[x]:
		if know[n]==0:
			dfs(n)
	f[x]=time
	time+=1
	
for i in range(n):
	if know[i]==0:
		dfs(i)

for i in range(n):
	out=[]
	out.append(i+1)
	out.append(d[i])
	out.append(f[i])
	print(*out)
