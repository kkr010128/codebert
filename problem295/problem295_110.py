from scipy.sparse.csgraph import floyd_warshall as fw

N, M, L = map(int, input().split())

S = [[float("inf") for i in range(N)] for i in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    S[a-1][b-1] = c
    S[b-1][a-1] = c

Sdist = fw(S)

Ssup_init = [[float("inf") for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if Sdist[i][j]<=L:
            Ssup_init[i][j] = 1

Ssup = fw(Ssup_init)

Q = int(input())

for i in range(Q):
    s, t = map(int, input().split())
    if Ssup[s-1][t-1]==float("inf"):
        print(-1)
    else:
        print(int(Ssup[s-1][t-1]-1))