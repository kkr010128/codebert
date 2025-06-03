import collections
n,x,y = map(int,input().split())
h = [[] for _ in range(n+1) ]
for i in range(1,n+1):
    if i+1<n+1:
        h[i].append(i+1)
    if i-1>0:
        h[i].append(i-1)
h[x].append(y)
h[y].append(x)

k = [0]*n
for i in range(1,n+1):
    q = collections.deque([i])
    step = [-1]*(n+1)
    step[i] = 0
    while q:
        now = q.popleft()
        for hh in h[now]:
            if step[hh] == -1:
                q.append(hh)
                step[hh] = step[now]+1
                k[step[now]+1] += 1
for i in range(1,n):
    print(k[i]//2)