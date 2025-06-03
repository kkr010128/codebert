n,m,l=map(int,input().split())
abcs=[list(map(int,input().split())) for _ in range(m)]
for i in range(m):
	abcs[i][0]-=1
	abcs[i][1]-=1
inf =1234567890123456
dist = [[inf for i in range(n)] for j in range(n)]
for i in range(n):
	dist[i][i] = 0

for i in range(m):
	a=abcs[i][0]
	b=abcs[i][1]
	c=abcs[i][2]
	dist[a][b] = dist[b][a] = c

for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

ans = [[inf for i in range(n)] for j in range(n)]
for i in range(n):
	ans[i][i]=0
for i in range(n):
	for j in range(i+1,n):
		if dist[i][j]<=l:
			ans[i][j]=ans[j][i]=1
for k in range(n):
	for i in range(n):
		for j in range(n):
			ans[i][j] = min(ans[i][j],ans[i][k]+ans[k][j])


for _ in range(int(input())):
	f,t=map(int,input().split())
	f-=1
	t-=1
	print(ans[f][t]-1 if ans[f][t]!=inf else -1)