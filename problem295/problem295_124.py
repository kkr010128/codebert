def resolve():
    from scipy.sparse.csgraph import floyd_warshall
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m, l = map(int, input().split())
    inf = 10 ** 20
    ar = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        ar[a - 1][b - 1] = c
    x = floyd_warshall(ar, directed=False)
    br = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if x[i, j] <= l:
                br[i][j] = 1
    y = floyd_warshall(br, directed=False)
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        print(int(y[s - 1, t - 1]) - 1 if y[s - 1, t - 1] < inf else -1)


if __name__ == "__main__":
    resolve()
