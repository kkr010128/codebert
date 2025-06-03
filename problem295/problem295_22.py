import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
inpl = lambda: list(map(int,input().split()))
N, M, L = inpl()
road = [[] for _ in range(N)]
ABC = []
for i in range(M):
    A, B, C = inpl()
    if C <= L:
        road[A-1].append((B-1,C))
        road[B-1].append((A-1,C))
        ABC.append((A-1,B-1,C))

INF = 10**12
cur1 = [[INF]*N for _ in range(N)]
for a, b, c in ABC:
    cur1[a][b] = cur1[b][a] = c
for k in range(N):
    prev1 = cur1
    cur1 = [[INF]*N for _ in range(N)] 
    for j in range(N):
        for i in range(N):
            cur1[j][i] = min(prev1[j][i], prev1[k][i]+prev1[j][k])

cur2 = [[INF]*N for j in range(N)]
for j in range(N):
    for i in range(N):
        if cur1[j][i] <= L:
            cur2[j][i] = 1
for k in range(N):
    prev2 = cur2
    cur2 = [[INF]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            cur2[j][i] = min(prev2[j][i], prev2[k][i]+prev2[j][k])

Q = int(input())
ST = [inpl() for _ in range(Q)]
for s,t in ST:
    if cur2[s-1][t-1] >= INF:
        print(-1)
    else:
        print(cur2[s-1][t-1]-1)