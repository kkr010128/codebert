import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

INF = 10**12
N, M, L = map(int, readline().split())

ABCQST = np.array(read().split(), dtype=np.int64)
ABC = ABCQST[:3*M]
A = ABC[::3]; B = ABC[1::3]; C = ABC[2::3]

Q = ABCQST[3*M]

ST = ABCQST[3*M + 1:]
S = ST[::2]; T = ST[1::2]

graph = csr_matrix((C, (A, B)), (N + 1, N + 1))
d = floyd_warshall(graph, directed=False)

d[d <= L] = 1
d[d > L] = INF

d = floyd_warshall(d, directed=False).astype(int)
d[d == INF] = 0

d -= 1
print('\n'.join(d.astype(str)[S, T]))
