
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
def resolve():
    INF = 10 ** 18
    N, M, L = map(int, input().split())
    G = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a][b] = G[b][a] = c

    G = csr_matrix(G)
    dist = floyd_warshall(G, directed=False)

    G2 = np.full((N, N), np.inf)  # 値をINFにした配列
    np.fill_diagonal(G2, 0)  # G[i][i]は動いていない状態なのでコスト0
    G2[dist <= L] = 1

    dist2 = floyd_warshall(G2, directed=False)

    Q = int(input())
    for _ in range(Q):
        a, b = map(lambda x: int(x) - 1, input().split())
        if dist2[a][b] == np.inf:
            print(-1)
        else:
            print(int(dist2[a][b]) - 1)


if __name__ == "__main__":
    resolve()
