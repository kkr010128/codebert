import sys
from collections import deque
input = sys.stdin.readline

h, w = list(map(int, input().split()))
t = h * w

s = ""
for i in range(h):
    s += input().replace( '\n' , '' )

#print(s)

adj = [[] for _ in range(t)]

for i in range(t):
    #よこ
    if i % w != 0 and s[i-1] == ".":
        adj[i].append(i-1)
    if i % w != w-1 and s[i+1] == ".":
        adj[i].append(i+1)
    #たて
    if i - w >= 0 and s[i-w] == ".":
        adj[i].append(i-w)
    if i + w < t and s[i+w] == ".":
        adj[i].append(i+w)

#print(adj)

m = 0
for i in range(t):
    if s[i] == "#":
        pass
    else:
        #BFS
        depth = [0] * t
        visited = [False] * t
        q = deque([i])
        visited[i] = True
        while len(q) > 0:
            v = q.popleft()
            for w in adj[v]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = True
                    depth[w] = depth[v] + 1
        
        #print(depth)
        
        m = max(m, max(depth))

print(m)


