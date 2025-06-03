import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
G = [list(map(lambda x: int(x)-1, input().split()))[2:] for _ in range(N)]
D = [-1]*N
D2 = [-1]*N
def dfs(cur, now):
    if D[cur] != -1: return now
    now += 1
    D[cur] = now
    for nex in G[cur]:
        now = dfs(nex,now)
    now += 1
    D2[cur] = now
    return now
now = 0
for i in range(N):
    now = dfs(i,now)
for i in range(N):
    print(i+1,D[i],D2[i])

