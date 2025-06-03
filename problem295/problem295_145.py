def solve():
    INF = float('inf')

    def WarshallFloyd(adjList):
        numV = len(adjList)
        D = [[INF]*numV for _ in range(numV)]
        for u, adj in enumerate(adjList):
            for v, wt in adj:
                D[u][v] = wt
            D[u][u] = 0
        for k in range(numV):
            Dk = D[k]
            for i in range(numV):
                Di = D[i]
                Dik = Di[k]
                for j in range(numV):
                    D2 = Dik + Dk[j]
                    if D2 < Di[j]:
                        D[i][j] = D2
        return D

    N, M, L = map(int, input().split())
    adjL = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A, B = A-1, B-1
        adjL[A].append((B, C))
        adjL[B].append((A, C))

    D = WarshallFloyd(adjL)

    adjL2 = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if D[i][j] <= L:
                adjL2[i].append((j, 1))
                adjL2[j].append((i, 1))

    D = WarshallFloyd(adjL2)

    Q = int(input())
    anss = []
    for _ in range(Q):
        s, t = map(int, input().split())
        s, t = s-1, t-1
        if D[s][t] == INF:
            anss.append(-1)
        else:
            anss.append(D[s][t]-1)

    print('\n'.join(map(str, anss)))


solve()
