import sys
sys.setrecursionlimit(10**9)
from collections import deque

n = int(input())
u = [[] for i in range(n+1)] #隣接リスト
for i in range(n):
    v = list(map(int, input().split()))
    u[v[0]] = v[1:] #v = [次数, 頂点...]

d = [-1] * (n+1)
f = [-1] * (n+1)
visited = [False] * (n+1)
visited[0] = True
time = 1

#再帰
def dfs(c):
    global time
    d[c] = time
    time += 1
    visited[c] = True
    for i in range(1, u[c][0]+1):
        if not visited[u[c][i]]:
            dfs(u[c][i])
    f[c] = time
    time += 1
"""
探索は元の始点から到達可能なすべての頂点を発見するまで続き、
未発見の頂点が残っていれば、
その中の番号が一番小さい１つを新たな始点として探索を続けます。
"""
while False in visited:
    dfs(visited.index(False))

for i in range(1, n+1):
    print(i, d[i], f[i])
