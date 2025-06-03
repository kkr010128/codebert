def resolve():
    from scipy.sparse.csgraph import floyd_warshall
    import numpy as np
    import sys
    input = sys.stdin.readline
    n, m, l = map(int, input().split())
    inf = 10 ** 20
    ar = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        ar[a - 1][b - 1] = c
        ar[b - 1][a - 1] = c
    x = floyd_warshall(ar)
    br = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if x[i, j] <= l:
                br[i][j] = 1
                br[j][i] = 1
    y = floyd_warshall(br)
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        p = y[s - 1, t - 1]
        print(int(p) - 1 if p < inf else -1)


if __name__ == "__main__":
    resolve()
