# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
import sys
input = sys.stdin.readline

N = int(input())
G = [[a-1 for a in list(map(int, input().split()))[2:]] for _ in [0]*N]
visited = [0]*N
history = [[] for _ in [0]*N]

k = 0


def dfs(v=0, p=-1):
    global k
    visited[v] = 1
    k += 1
    history[v].append(k)

    for u in G[v]:
        if u == p or visited[u]:
            continue
        dfs(u, v)

    k += 1
    history[v].append(k)


for i in range(N):
    if not visited[i]:
        dfs(i)

for i, h in enumerate(history):
    print(i+1, *h)

