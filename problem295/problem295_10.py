
def resolve():
    INF = 10 ** 18
    N, M, L = map(int, input().split())
    G = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a][b] = G[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    Cost = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if G[i][j] <= L:
                Cost[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                Cost[i][j] = min(Cost[i][j], Cost[i][k] + Cost[k][j])

    Q = int(input())
    for _ in range(Q):
        a, b = map(lambda x: int(x) - 1, input().split())
        if Cost[a][b] == INF:
            print(-1)
        else:
            print(Cost[a][b] - 1)


if __name__ == "__main__":
    resolve()
