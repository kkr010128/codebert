import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, k = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))


def dfs(i):
    if 0 <= visited[i]:
        return
    visited[i] = idx
    cycle.append(i)
    global csum
    csum += C[i]
    dfs(P[i])


visited = [-1]*n
idx = 0
cycles = []
for i in range(n):
    if 0 <= visited[i]:
        continue
    cycle = []
    csum = 0
    dfs(i)
    cycles.append((cycle, csum))
    idx += 1


INF = 10**18
ans = -INF
for i in range(n):
    cycle, csum = cycles[visited[i]]
    cmem = len(cycle)

    if 0 < csum:
        a, b = divmod(k, cmem)
        scoreA = csum*(a-1)
        b += cmem
        score = 0
        scoreB = 0
        for _ in range(b):
            i = P[i]
            score += C[i]
            if scoreB < score:
                scoreB = score
        X = scoreA+scoreB
    else:
        b = min(k, cmem)
        score = 0
        INF = 10**18
        X = -INF
        for _ in range(b):
            i = P[i]
            score += C[i]
            if X < score:
                X = score

    if ans < X:
        ans = X
print(ans)
