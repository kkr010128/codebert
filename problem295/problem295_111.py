import sys

N,M,L=map(int, sys.stdin.readline().split())

d=[  [ float("inf") for j in range(N+1) ]  for i in range(N+1) ]

for _ in range(M):
    a,b,c=map(int, sys.stdin.readline().split())
    d[a][b]=c
    d[b][a]=c
    d[a][a]=0
    d[b][b]=0

for k in range(1,N+1):
	for i in range(1,N+1):
		for j in range(1,N+1):
			d[i][j]=min(d[i][j], d[i][k]+d[k][j])

e=[  [ float("inf") for j in range(N+1) ]  for i in range(N+1) ]
for i in range(1,N+1):
    for j in range(i,N+1):
        if i==j:
            e[i][j]=0
            e[j][i]=0
        elif d[i][j]<=L:
            e[i][j]=1
            e[j][i]=1

for k in range(1,N+1):
	for i in range(1,N+1):
		for j in range(1,N+1):
			e[i][j]=min(e[i][j], e[i][k]+e[k][j])


Q=input()
for _ in range(Q):
    s,t=map(int, sys.stdin.readline().split())
    if e[s][t]==float("inf"):
        print -1
    else:
        print e[s][t]-1
