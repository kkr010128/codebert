import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict
    n, m, l = map(int, readline().split())
    dist = [[INF] * n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, readline().split())
        a, b = a - 1, b - 1
        dist[a][b] = c
        dist[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dist2 = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                dist2[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist2[i][j] = min(dist2[i][j], dist2[i][k] + dist2[k][j])

    q = int(readline())

    for _ in range(q):
        s, t = map(int, readline().split())
        s, t = s - 1, t - 1
        if dist2[s][t] == INF:
            print(-1)
        else:
            print(dist2[s][t] - 1)


if __name__ == '__main__':
    main()
