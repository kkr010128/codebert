#ごり押し

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np
from collections import Counter

N, X, Y = map(int, input().split())

start = list(range(0, N-1)) + list(range(1, N)) + [X-1, Y-1] 
end = list(range(1, N)) + list(range(0, N-1)) + [Y-1, X-1]
cost = [1] * len(start)

graph = csr_matrix((cost, (start, end)))
lengths = dijkstra(graph, directed = False)

c = Counter(lengths.astype(np.int64).reshape(-1))
for k in range(1, N):
    print(c[k]//2)
