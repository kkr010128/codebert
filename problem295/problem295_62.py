import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.buffer.readline
INF = 10**12

N, M, L = map(int, input().split())
G = np.zeros((N, N), dtype=np.int64)
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = c
    G[b][a] = c
Q = int(input())
ST = [list(map(int, input().split())) for _ in range(Q)]

fw = floyd_warshall(G)
path = np.full((N, N), INF, dtype=np.int64)
path[fw <= L] = 1
path_fw = (floyd_warshall(path) + 0.5).astype(np.int64)

ans = []
for s, t in ST:
    s -= 1
    t -= 1
    if path_fw[s][t] >= INF:
        ans.append(-1)
        continue
    ans.append(path_fw[s][t]-1)

print(*ans, sep="\n")
