n = int(input())
g = [[]for i in range(n)]
for i in range(n):
    v = list(map(int,input().split()))
    u = v[0]-1
    k = v[1]
    for j in range(k):
        g[u].append(v[j+2]-1)
time = 1
ans = []
d = [0]*n
f = [0] *n
visited = [0]*n

def dfs(now,last = -1):
    global time
    
    visited[now] = 1
    d[now] = time
    time += 1
    for next in g[now]:
        if visited[next]:continue
        dfs(next,now)
    f[now] = time
    time +=1
    
for i in range(n):
    if not visited[i]:dfs(i)
for i in range(n):
    print(i+1,d[i],f[i])
    
    
        
        
