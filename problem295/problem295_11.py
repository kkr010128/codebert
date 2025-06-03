def main():
    import sys
    input = sys.stdin.readline

    inf = 1 << 60

    N, M, L = map(int, input().split())

    dist = [[inf] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        dist[A][B] = dist[B][A] = C

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    g = [[inf] * N for _ in range(N)]  # 到達に必要な補充回数
    for A in range(N):
        for B in range(N):
            if dist[A][B] <= L:
                g[A][B] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(
                    g[i][j],
                    g[i][k] + g[k][j]
                )

    Q = int(input())
    for _ in range(Q):
        s, t = (int(x) - 1 for x in input().split())
        d = g[s][t]
        if d == inf:
            print(-1)
        else:
            print(d - 1)


if __name__ == '__main__':
    main()
