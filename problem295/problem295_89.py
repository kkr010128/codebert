import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,l = list(map(int, input().split()))
from collections import defaultdict
ns = defaultdict(set)
for i in range(m):
    a,b,c = map(int, input().split())
    a-=1
    b-=1
    if c<=l:
        ns[a].add((c,b))
        ns[b].add((c,a))

def wf(ns):
    """全頂点間距離
    """
    d = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        for t,j in ns[i]:
            d[i][j] = t
        d[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
dist = wf(ns)
ns2 = defaultdict(set)
for i in range(n):
    for j in range(i+1,n):
        if dist[i][j]<=l:
            ns2[i].add((1,j))
            ns2[j].add((1,i))
ddist = wf(ns2)
q = int(input())
ans = [None]*q
for i in range(q):
    s,t = map(int, input().split())
    s-=1
    t-=1
    if dist[s][t]==float("inf"):
        ans[i] = -1
    else:
        ans[i] = ddist[s][t] - 1
write("\n".join(map(str, ans)))