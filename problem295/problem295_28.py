#input
N, M, L = map(int, input().split())
A = [0] * M
B = [0] * M
C = [0] * M
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())
Q = int(input())
s = [0] * Q
t = [0] * Q
for i in range(Q):
    s[i], t[i] = map(int, input().split())

#output
from scipy.sparse.csgraph import floyd_warshall, shortest_path, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
import numpy as np

#便宜上A, Bを-1する。
for i in range(M):
    A[i] -= 1
    B[i] -= 1

#FW法で各経路の最短距離を計算する。
graph = csr_matrix((C, (A, B)), shape = (N, N))
dist_matrix = floyd_warshall(csgraph = graph, directed = False, return_predecessors = False)

graph2 = np.full((N, N), np.inf)
graph2[dist_matrix  <= L] = 1
graph2 = csr_matrix(graph2)
dist_matrix2 = floyd_warshall(csgraph = graph2, directed = False, return_predecessors = False)

for q in range(Q):
    if dist_matrix2[s[q]-1][t[q]-1] < 10000000:
        print(int(dist_matrix2[s[q]-1][t[q]-1]-1))
    else:
        print(-1)