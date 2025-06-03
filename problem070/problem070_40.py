import sys
sys.setrecursionlimit(10**9)
n,m = list(map(int,input().split()))

d = {}
for i in range(m):
    fr, to = list(map(int,input().split()))
    d[fr] = d.get(fr, []) + [to]
    d[to] = d.get(to, []) + [fr]
    
visited = [0 for i in range(n+1)]

def connect(node, i):
    visited[node] = i
    
    if node in d:
        for neig in d[node]:
            if visited[neig] == 0:
                connect(neig, i)
ans = 1
for key in range(1,n+1):
    if visited[key] == 0:
        connect(key, ans)
        ans += 1

print(max(visited)-1)

