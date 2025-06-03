import sys
sys.setrecursionlimit(10**7) 

def dfs(G,v):
    global ptr
    first_order[v] = ptr
    ptr += 1
    seen[v] = True
    for next in G[v]:
        if seen[next]:
            continue
        dfs(G,next)

    last_order[v] = ptr
    ptr+=1

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n):
    a = list(map(int, input().split()))
    u = a[0]
    k = a[1]
    v = a[2:]
    for i in v:
        G[u-1].append(i-1)

seen = [False]*n
first_order = [0]*n
last_order = [0]*n
ptr = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(G,i)

for i in range(n):
    print('{} {} {}'.format(i+1,first_order[i]+1,last_order[i]+1))
