import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n, m = map(int, input().split())
    E = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        E[u].append(v)
        E[v].append(u)


    cnt = 0
    color = [-1] * n
    def dfs(v):
        if color[v] != -1:
            return False
        color[v] = cnt
        queue = [v]
        for v in queue:
            for nv in E[v]:
                if color[nv] == -1:
                    color[nv] = cnt
                    queue.append(nv)
        return True

    for v in range(n):
        cnt += dfs(v)

    print(Counter(color).most_common()[0][1])
resolve()